import os
import json
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory, render_template_string
from werkzeug.exceptions import NotFound

from database import get_db_connection, init_db, seed_db
from file_manager import init_file_directories, save_local_file, is_allowed_file, DIRECTORIES, UPLOAD_DIR

app = Flask(__name__, static_folder='public', static_url_path='')

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024  # 64 MB limit for artwork/templates

# Ensure database and local storage are initialized on startup
init_file_directories()
init_db()
seed_db()

@app.route('/uploads/<category>/<filename>')
def serve_uploaded_file(category, filename):
    folder = DIRECTORIES.get(category)
    if not folder:
        raise NotFound("Upload category not found.")
    return send_from_directory(folder, filename)

# ----------------- API ROUTES ----------------- #

@app.route('/api/categories', methods=['GET'])
def get_categories():
    conn = get_db_connection()
    categories = conn.execute("SELECT * FROM categories ORDER BY id ASC").fetchall()
    conn.close()
    return jsonify([dict(c) for c in categories])

@app.route('/api/products', methods=['GET'])
def get_products():
    category_id = request.args.get('category_id')
    featured = request.args.get('featured')
    
    query = "SELECT p.*, c.name as category_name, c.slug as category_slug FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE 1=1"
    params = []
    
    if category_id:
        query += " AND (p.category_id = ? OR c.parent_id = ?)"
        params.extend([category_id, category_id])
    if featured:
        query += " AND p.is_featured = 1"
        
    query += " ORDER BY p.id ASC"
    
    conn = get_db_connection()
    products = conn.execute(query, params).fetchall()
    conn.close()
    
    result = []
    for p in products:
        item = dict(p)
        item['sizes'] = json.loads(item['sizes_json']) if item['sizes_json'] else []
        item['colors'] = json.loads(item['colors_json']) if item['colors_json'] else []
        result.append(item)
    return jsonify(result)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute("SELECT p.*, c.name as category_name FROM products p LEFT JOIN categories c ON p.category_id = c.id WHERE p.id = ?", (product_id,)).fetchone()
    conn.close()
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    res = dict(product)
    res['sizes'] = json.loads(res['sizes_json']) if res['sizes_json'] else []
    res['colors'] = json.loads(res['colors_json']) if res['colors_json'] else []
    return jsonify(res)

@app.route('/api/templates', methods=['GET'])
def get_templates():
    conn = get_db_connection()
    templates = conn.execute("SELECT t.*, c.name as category_name FROM templates t LEFT JOIN categories c ON t.category_id = c.id ORDER BY t.id ASC").fetchall()
    conn.close()
    
    res = []
    for t in templates:
        row = dict(t)
        row['zones'] = json.loads(row['zones_json']) if row['zones_json'] else {}
        row['cdr_metadata'] = json.loads(row['cdr_metadata_json']) if row['cdr_metadata_json'] else {}
        res.append(row)
    return jsonify(res)

@app.route('/api/orders', methods=['GET'])
def list_orders():
    status = request.args.get('status')
    conn = get_db_connection()
    if status:
        orders = conn.execute("SELECT * FROM orders WHERE status = ? ORDER BY id DESC", (status,)).fetchall()
    else:
        orders = conn.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(o) for o in orders])


@app.route('/api/track/<order_number>', methods=['GET'])
def track_order_alias(order_number):
    return get_order_detail(order_number)

@app.route('/api/orders/<order_number>', methods=['GET'])
def get_order_detail(order_number):
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE order_number = ?", (order_number.upper(),)).fetchone()
    if not order:
        conn.close()
        return jsonify({'error': f'Order {order_number} not found'}), 404
    
    order_dict = dict(order)
    order_id = order['id']
    
    items = conn.execute("SELECT * FROM order_items WHERE order_id = ?", (order_id,)).fetchall()
    order_dict['items'] = []
    for item in items:
        item_dict = dict(item)
        item_dict['design_config'] = json.loads(item_dict['design_config_json']) if item_dict['design_config_json'] else {}
        order_dict['items'].append(item_dict)
        
    invoice = conn.execute("SELECT * FROM invoices WHERE order_id = ?", (order_id,)).fetchone()
    if invoice:
        inv_dict = dict(invoice)
        inv_dict['line_items'] = json.loads(inv_dict['line_items_json']) if inv_dict['line_items_json'] else []
        order_dict['invoice'] = inv_dict
    else:
        order_dict['invoice'] = None
        
    slips = conn.execute("SELECT * FROM payment_slips WHERE order_id = ? ORDER BY id DESC", (order_id,)).fetchall()
    order_dict['payment_slips'] = [dict(s) for s in slips]
    
    files = conn.execute("SELECT * FROM order_files_assets WHERE order_id = ? ORDER BY id DESC", (order_id,)).fetchall()
    order_dict['files'] = [dict(f) for f in files]
    
    logs = conn.execute("SELECT * FROM audit_status_logs WHERE order_id = ? ORDER BY timestamp DESC", (order_id,)).fetchall()
    order_dict['status_logs'] = [dict(l) for l in logs]
    
    conn.close()
    return jsonify(order_dict)

@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Accepts customer order data, creates next ZAM-xxx-26 ID,
    inserts order, order_items, generates initial invoice, and handles design assets.
    """
    data = request.json or {}
    customer_name = data.get('customer_name', 'Customer Athlete').strip()
    customer_email = data.get('customer_email', 'athlete@example.com').strip()
    customer_phone = data.get('customer_phone', '+1 555-0100').strip()
    notes = data.get('notes', 'Direct order from ZamForward landing portal.')
    items_data = data.get('items', [])
    
    if not items_data:
        return jsonify({'error': 'Order must contain at least one item'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Generate sequential order number in format ZAM-xxx-26
    cursor.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    next_seq = 400 + (last_row['id'] + 1 if last_row else 1)
    current_year_suffix = datetime.now().strftime('%y')
    order_number = f"ZAM-{next_seq}-{current_year_suffix}"
    
    # Calculate totals
    subtotal = sum(float(it.get('unit_price', 50)) * int(it.get('quantity', 1)) for it in items_data)
    total_amount = subtotal
    
    cursor.execute('''
    INSERT INTO orders (order_number, user_id, customer_name, customer_email, customer_phone, status, total_amount, paid_amount, production_deadline, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order_number,
        None,
        customer_name,
        customer_email,
        customer_phone,
        'Confirmed',
        total_amount,
        0.0,
        'Pending Review',
        notes
    ))
    order_id = cursor.lastrowid
    
    # Insert order items
    invoice_lines = []
    for it in items_data:
        p_id = it.get('product_id')
        p_name = it.get('product_name', 'Custom Combat Item')
        qty = int(it.get('quantity', 1))
        size = it.get('size', 'L')
        color = it.get('color', 'Standard')
        unit_price = float(it.get('unit_price', 50))
        item_sub = unit_price * qty
        design_cfg = it.get('design_config', {})
        
        cursor.execute('''
        INSERT INTO order_items (order_id, product_id, product_name, quantity, size, color, unit_price, subtotal, design_config_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (order_id, p_id, p_name, qty, size, color, unit_price, item_sub, json.dumps(design_cfg)))
        
        invoice_lines.append({
            'desc': f"{qty}x {p_name} ({size}, {color})",
            'total': item_sub
        })
    
    # Generate initial invoice
    deposit_required = round(total_amount * 0.50, 2)
    inv_num = f"INV-{order_number}"
    cursor.execute('''
    INSERT INTO invoices (order_id, invoice_number, subtotal, tax_rate, tax_amount, discount, total, deposit_required, status, line_items_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (order_id, inv_num, subtotal, 0.0, 0.0, 0.0, total_amount, deposit_required, 'Pending 50% Deposit', json.dumps(invoice_lines)))
    
    # Record initial audit status log
    cursor.execute('''
    INSERT INTO audit_status_logs (order_id, previous_status, new_status, changed_by, comments)
    VALUES (?, ?, ?, ?, ?)
    ''', (order_id, None, 'Confirmed', 'Customer Order Portal', 'Order placed & file registered in ZamForward system.'))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        'message': 'Order successfully created',
        'order_number': order_number,
        'order_id': order_id,
        'status': 'Confirmed',
        'total_amount': total_amount,
        'deposit_required': deposit_required
    }), 201

@app.route('/api/orders/<order_number>/status', methods=['POST'])
def update_order_status(order_number):
    """
    Admin updates order status:
    Confirmed -> Received by ZAM -> Invoice Sent -> Invoice Cleared -> In Progress -> Production -> Dispatched -> Completed
    """
    data = request.json or {}
    new_status = data.get('status')
    deadline = data.get('deadline')
    tracking_number = data.get('tracking_number')
    courier = data.get('courier', 'DHL Express')
    comments = data.get('comments', '')
    changed_by = data.get('changed_by', 'ZamForward Staff')
    
    if not new_status:
        return jsonify({'error': 'New status required'}), 400
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    order = cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number.upper(),)).fetchone()
    if not order:
        conn.close()
        return jsonify({'error': 'Order not found'}), 404
        
    old_status = order['status']
    order_id = order['id']
    
    update_fields = ["status = ?", "updated_at = CURRENT_TIMESTAMP"]
    params = [new_status]
    
    if deadline is not None:
        update_fields.append("production_deadline = ?")
        params.append(deadline)
    if tracking_number is not None:
        update_fields.append("tracking_number = ?")
        params.append(tracking_number)
    if courier is not None:
        update_fields.append("courier = ?")
        params.append(courier)
        
    params.append(order_id)
    cursor.execute(f"UPDATE orders SET {', '.join(update_fields)} WHERE id = ?", params)
    
    # Audit log
    cursor.execute('''
    INSERT INTO audit_status_logs (order_id, previous_status, new_status, changed_by, comments)
    VALUES (?, ?, ?, ?, ?)
    ''', (order_id, old_status, new_status, changed_by, comments or f"Status shifted from {old_status} to {new_status}"))
    
    # If status is cleared or in progress, record to order_history for 1-click reordering
    if new_status in ['In Progress', 'Production', 'Completed']:
        existing_history = cursor.execute("SELECT id FROM order_history WHERE order_id = ?", (order_id,)).fetchone()
        if not existing_history:
            items = cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (order_id,)).fetchall()
            reorder_payload = [dict(i) for i in items]
            cursor.execute('''
            INSERT INTO order_history (order_id, user_id, reorder_payload_json)
            VALUES (?, ?, ?)
            ''', (order_id, order['user_id'], json.dumps(reorder_payload)))
            
    conn.commit()
    conn.close()
    
    return jsonify({
        'message': f'Order {order_number} status updated to {new_status}',
        'previous_status': old_status,
        'new_status': new_status
    })

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """
    Handles local file upload for designs, payment slips, and CDR templates.
    """
    category = request.form.get('category', 'designs')
    order_number = request.form.get('order_number')
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if not is_allowed_file(category, file.filename):
        return jsonify({'error': f'File extension not allowed for category {category}'}), 400
        
    try:
        saved_meta = save_local_file(category, file, custom_prefix=order_number)
        
        # If order_number provided, register asset in database
        if order_number:
            conn = get_db_connection()
            order = conn.execute("SELECT id FROM orders WHERE order_number = ?", (order_number.upper(),)).fetchone()
            if order:
                order_id = order['id']
                if category == 'payment_slips':
                    amount = float(request.form.get('amount', 0.0))
                    bank_ref = request.form.get('bank_reference', 'Local Slip Upload')
                    conn.execute('''
                    INSERT INTO payment_slips (order_id, slip_file_path, relative_url, amount, bank_reference, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (order_id, saved_meta['local_path'], saved_meta['relative_url'], amount, bank_ref, 'Submitted - Pending Review'))
                    
                    conn.execute('''
                    INSERT INTO audit_status_logs (order_id, previous_status, new_status, changed_by, comments)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (order_id, 'Invoice Sent', 'Slip Uploaded', 'Customer', '50% deposit payment proof slip uploaded.'))
                else:
                    conn.execute('''
                    INSERT INTO order_files_assets (order_id, file_type, original_name, stored_name, local_path, relative_url, file_size, mime_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        order_id,
                        category,
                        saved_meta['original_name'],
                        saved_meta['stored_name'],
                        saved_meta['local_path'],
                        saved_meta['relative_url'],
                        saved_meta['file_size'],
                        file.content_type
                    ))
                conn.commit()
            conn.close()
            
        return jsonify({
            'message': 'File uploaded and stored locally successfully',
            'file': saved_meta
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json or {}
    email = data.get('email', '').strip().lower()
    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()
    country_code = data.get('country_code', '+1').strip()
    phone = data.get('phone', '').strip()
    password = data.get('password', 'zam123')
    
    if not email or not first_name or not last_name:
        return jsonify({'error': 'Email, First Name, and Last Name are required'}), 400
        
    conn = get_db_connection()
    try:
        conn.execute('''
        INSERT INTO users (email, first_name, last_name, country_code, phone, password_hash, email_verified, role)
        VALUES (?, ?, ?, ?, ?, ?, 1, 'customer')
        ''', (email, first_name, last_name, country_code, phone, password))
        conn.commit()
        user_id = conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()['id']
        conn.close()
        return jsonify({
            'message': 'Account created and verified successfully',
            'user': {'id': user_id, 'email': email, 'name': f"{first_name} {last_name}", 'role': 'customer'}
        }), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Email already registered'}), 409

@app.route('/api/stats', methods=['GET'])
def get_stats():
    conn = get_db_connection()
    total_orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    in_production = conn.execute("SELECT COUNT(*) FROM orders WHERE status = 'Production'").fetchone()[0]
    confirmed = conn.execute("SELECT COUNT(*) FROM orders WHERE status = 'Confirmed'").fetchone()[0]
    total_revenue = conn.execute("SELECT COALESCE(SUM(total_amount), 0) FROM orders").fetchone()[0]
    conn.close()
    return jsonify({
        'total_orders': total_orders,
        'in_production': in_production,
        'confirmed_orders': confirmed,
        'total_volume': total_revenue
    })

# ----------------- MAIN LANDING PAGE ----------------- #

@app.route('/')
def index():
    # Serves the enriched landing page
    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public', 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Fallback to code.html if public/index.html not created yet
        code_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'code.html')
        with open(code_path, 'r', encoding='utf-8') as f:
            return f.read()

if __name__ == '__main__':
    print("=" * 60)
    print(" ZamForward Combat Apparel Platform (ZamOne) Engine")
    print(" Local SQLite DB: zamforward.db")
    print(" Local Storage: uploads/ (designs, payment_slips, templates)")
    print(" Local Server running at: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host='127.0.0.1', port=5000, debug=False)
