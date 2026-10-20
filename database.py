import sqlite3
import os
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zamforward.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        country_code TEXT NOT NULL DEFAULT '+1',
        phone TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        email_verified INTEGER DEFAULT 1,
        role TEXT DEFAULT 'customer',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Categories Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        slug TEXT UNIQUE NOT NULL,
        parent_id INTEGER,
        description TEXT,
        badge TEXT,
        image_url TEXT,
        FOREIGN KEY (parent_id) REFERENCES categories (id) ON DELETE SET NULL
    )
    ''')

    # 3. Products Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        name TEXT NOT NULL,
        sku TEXT UNIQUE NOT NULL,
        description TEXT,
        base_price REAL NOT NULL,
        gsm_weight TEXT,
        sizes_json TEXT NOT NULL,
        colors_json TEXT NOT NULL,
        image_url TEXT,
        is_featured INTEGER DEFAULT 0,
        FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE SET NULL
    )
    ''')

    # 4. Templates Table (Ready for CDR Template Markup)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS templates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        name TEXT NOT NULL,
        template_code TEXT UNIQUE NOT NULL,
        file_path TEXT,
        preview_image TEXT,
        zones_json TEXT,
        cdr_metadata_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE SET NULL
    )
    ''')

    # 5. Orders Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_number TEXT UNIQUE NOT NULL,
        user_id INTEGER,
        customer_name TEXT NOT NULL,
        customer_email TEXT NOT NULL,
        customer_phone TEXT,
        status TEXT NOT NULL DEFAULT 'Confirmed',
        total_amount REAL DEFAULT 0.0,
        paid_amount REAL DEFAULT 0.0,
        production_deadline TEXT,
        tracking_number TEXT,
        courier TEXT,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
    )
    ''')

    # 6. Order Items Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        size TEXT NOT NULL,
        color TEXT NOT NULL,
        unit_price REAL NOT NULL,
        subtotal REAL NOT NULL,
        design_config_json TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE SET NULL
    )
    ''')

    # 7. Order Files & Assets (Local File Management)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_files_assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        file_type TEXT NOT NULL,
        original_name TEXT NOT NULL,
        stored_name TEXT NOT NULL,
        local_path TEXT NOT NULL,
        relative_url TEXT NOT NULL,
        file_size INTEGER,
        mime_type TEXT,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE
    )
    ''')

    # 8. Invoices Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER UNIQUE NOT NULL,
        invoice_number TEXT UNIQUE NOT NULL,
        subtotal REAL NOT NULL,
        tax_rate REAL DEFAULT 0.0,
        tax_amount REAL DEFAULT 0.0,
        discount REAL DEFAULT 0.0,
        total REAL NOT NULL,
        deposit_required REAL NOT NULL,
        status TEXT DEFAULT 'Unpaid',
        line_items_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        due_date TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE
    )
    ''')

    # 9. Payment Slips Table (50% deposit clearance)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment_slips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        slip_file_path TEXT NOT NULL,
        relative_url TEXT,
        amount REAL,
        bank_reference TEXT,
        status TEXT DEFAULT 'Pending Review',
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        verified_at TIMESTAMP,
        verified_by TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE
    )
    ''')

    # 10. Audit / Status Logs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_status_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        previous_status TEXT,
        new_status TEXT NOT NULL,
        changed_by TEXT DEFAULT 'System',
        comments TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE
    )
    ''')

    # 11. Order History / Reorder Cache
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        user_id INTEGER,
        reorder_payload_json TEXT NOT NULL,
        archived_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    ''')

    # Create Indexes for fast lookup
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_number ON orders(order_number)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_templates_code ON templates(template_code)")

    conn.commit()
    conn.close()
    print("Database tables & indexes initialized successfully.")

def seed_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if already seeded
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] > 0:
        print("Database already contains data. Skipping re-seed.")
        conn.close()
        return

    print("Seeding initial ZamForward combat apparel data...")

    # Users
    users_data = [
        ('admin@zamforward.com', 'ZamForward', 'Staff', '+1', '8005550199', 'admin123', 1, 'admin'),
        ('athlete@zamforward.com', 'Marcus', 'Vance', '+1', '5552345678', 'athlete123', 1, 'customer'),
        ('elena@apexdojo.com', 'Elena', 'Rostova', '+44', '7911123456', 'elena123', 1, 'customer')
    ]
    cursor.executemany('''
    INSERT INTO users (email, first_name, last_name, country_code, phone, password_hash, email_verified, role)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', users_data)

    # Categories
    categories_data = [
        (1, 'All Sports Wear', 'sports-wear', None, 'High performance athletic and combat garments', 'Pro Combat Grade', 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600'),
        (2, 'Rashguards', 'rashguards', 1, 'Sublimated 450 GSM compression tops with reinforced flatlock stitching', 'IBJJF Compliant', 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600'),
        (3, 'Martial Arts', 'martial-arts', 1, 'MMA, BJJ, and Muay Thai combat tournament wear', 'Championship Standard', 'https://images.unsplash.com/photo-1509563428935-467f5664dbb7?w=600'),
        (4, 'MMA Gear', 'mma', 3, 'Flex-split cage fight shorts, 4oz gloves, and shin guards', 'Cage Certified', 'https://images.unsplash.com/photo-1517438322307-e67111335449?w=600'),
        (5, 'BJJ Gis & Belts', 'bjj', 3, 'Pearl weave and gold weave competition Gis with 5 belt ranks', 'IBJJF Legal', 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600'),
        (6, 'Muay Thai', 'muay-thai', 3, 'Retro satin flared fight shorts and hand wraps', 'Bangkok Cut', 'https://images.unsplash.com/photo-1549060279-7e168fcee0c2?w=600'),
        (7, 'Compression Wear', 'compression', 1, 'Grappling spats, muscle-mapping recovery tights and tops', '4-Way Stretch', 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600'),
    ]
    cursor.executemany('''
    INSERT INTO categories (id, name, slug, parent_id, description, badge, image_url)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', categories_data)

    # Products
    products_data = [
        (
            2,
            'Apex Sublimated Short-Sleeve Rashguard',
            'ZAM-RG-SS-01',
            'Engineered with 450 GSM Poly-Spandex, 6-needle flatlock contrast seams, and high-tenacity silicon anti-slip waistband. Moisture wicking and anti-microbial fabric.',
            54.00,
            '450 GSM',
            json.dumps(['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL']),
            json.dumps([
                {'name': 'Carbon Black', 'hex': '#111417'},
                {'name': 'Combat Cyan', 'hex': '#088395'},
                {'name': 'Bone Sandstone', 'hex': '#EDE8DE'},
                {'name': 'Ochre Gold', 'hex': '#C9A86A'}
            ]),
            'https://lh3.googleusercontent.com/aida-public/AB6AXuDiIivqWV2zkljxK2BElPuFhZ9MFhpuib8LjAz4MD4qEj-d-dmD4FuXZkJumaFnFdpywPDsC-UckvFober_UEW2gT5jUneKW1I2Jbl4HiOMzciMoJc9d5XJmmrHxXzVy08bSVgFPXgi09dVtglIy3tM59RPjGNiwRv5pjVua9Znr8CTzdWqhaq-iWb24FcY4k4kQiBt_ZJQfLaAfNrDeX8wLlXu7hvGFFf3RvMKu4inpLilrhyVvBg',
            1
        ),
        (
            2,
            'Apex Long-Sleeve Sublimation Rashguard',
            'ZAM-RG-LS-02',
            'Full forearm grip protection with dual-density muscle tension compression. Perfect for no-gi grappling and mat burn prevention.',
            62.00,
            '480 GSM',
            json.dumps(['S', 'M', 'L', 'XL', '2XL']),
            json.dumps([
                {'name': 'Stealth Onyx', 'hex': '#1c1c18'},
                {'name': 'Teal Strike', 'hex': '#006877'},
                {'name': 'Graphite', 'hex': '#44474a'}
            ]),
            'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600',
            1
        ),
        (
            4,
            'Apex Combat Flex-Split MMA Shorts',
            'ZAM-MMA-SH-01',
            'High-mobility side slits with 4-way stretch flex crotch panel. Internal drawstring with dual-lock Velcro flap and reinforced waistband.',
            48.00,
            '220 GSM Ripstop',
            json.dumps(['S', 'M', 'L', 'XL', '2XL']),
            json.dumps([
                {'name': 'Mat Charcoal', 'hex': '#22252a'},
                {'name': 'Combat Cyan', 'hex': '#088395'},
                {'name': 'Champion White', 'hex': '#ffffff'}
            ]),
            'https://lh3.googleusercontent.com/aida-public/AB6AXuAY1r2qM1B994s91o1676v2T4iYc3k_1o6h7m-89cf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ',
            1
        ),
        (
            5,
            'IBJJF Pro Gold Weave Kimono (Gi)',
            'ZAM-BJJ-GI-01',
            'Heavy-duty 550 GSM gold weave cotton jacket paired with 10oz ripstop pants with quadruple knee reinforcement. 5 belt ranks included for academy customization.',
            135.00,
            '550 GSM Gold Weave',
            json.dumps(['A0', 'A1', 'A2', 'A3', 'A4', 'A5']),
            json.dumps([
                {'name': 'White Belt Rank', 'hex': '#F4F1EA'},
                {'name': 'Blue Belt Rank', 'hex': '#1E3A8A'},
                {'name': 'Purple Belt Rank', 'hex': '#6B21A8'},
                {'name': 'Brown Belt Rank', 'hex': '#78350F'},
                {'name': 'Black Belt Rank', 'hex': '#111417'}
            ]),
            'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600',
            1
        ),
        (
            6,
            'Bangkok Cut Muay Thai Retro Shorts',
            'ZAM-MT-SH-01',
            'Traditional flared high leg slit with wide 8-stripe elastic waistband. Sublimated heavy satin side panels with custom gym crest embroidery ready.',
            45.00,
            'Heavy Satin',
            json.dumps(['S', 'M', 'L', 'XL', '2XL']),
            json.dumps([
                {'name': 'Midnight Navy', 'hex': '#0f172a'},
                {'name': 'Crimson Combat', 'hex': '#991b1b'},
                {'name': 'Gold Accent', 'hex': '#C9A86A'}
            ]),
            'https://images.unsplash.com/photo-1549060279-7e168fcee0c2?w=600',
            0
        ),
        (
            7,
            'Grappling Spats Compression Tights',
            'ZAM-CMP-LG-01',
            'Ergonomic muscle tracking cuts, flatlock stitching prevents chafing during takedowns and guard passes. UPF 50+ UV guard.',
            42.00,
            '320 GSM Lycra',
            json.dumps(['XS', 'S', 'M', 'L', 'XL', '2XL']),
            json.dumps([
                {'name': 'Deep Slate', 'hex': '#1c1c18'},
                {'name': 'Electric Cyan Line', 'hex': '#088395'}
            ]),
            'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600',
            1
        )
    ]
    cursor.executemany('''
    INSERT INTO products (category_id, name, sku, description, base_price, gsm_weight, sizes_json, colors_json, image_url, is_featured)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', products_data)

    # CorelDraw (CDR) Templates
    templates_data = [
        (
            2,
            'Rashguard Sublimation Master 2D CDR Template',
            'CDR-RG-01',
            '/uploads/templates/rashguard_master_v2.cdr',
            'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400',
            json.dumps({
                'zones': [
                    {'id': 'front_chest', 'name': 'Chest & Core Area', 'max_w_mm': 280, 'max_h_mm': 320},
                    {'id': 'back_spine', 'name': 'Upper Back & Spine', 'max_w_mm': 300, 'max_h_mm': 380},
                    {'id': 'left_sleeve', 'name': 'Left Sleeve Band', 'max_w_mm': 90, 'max_h_mm': 220},
                    {'id': 'right_sleeve', 'name': 'Right Sleeve Band', 'max_w_mm': 90, 'max_h_mm': 220}
                ]
            }),
            json.dumps({
                'cdr_version': 'CorelDraw X7/2024 (.cdr)',
                'bleed_margin_mm': 15,
                'color_space': 'CMYK / Sublimation High-Gamut',
                'resolution_dpi': 300,
                'cut_line_layer': 'DieCut_Layer_DoNotPrint',
                'art_layer': 'Artwork_Sublimation_CMYK'
            })
        ),
        (
            4,
            'MMA Fight Shorts Vector Pattern CDR Template',
            'CDR-MMA-02',
            '/uploads/templates/mma_shorts_pattern_v1.cdr',
            'https://images.unsplash.com/photo-1517438322307-e67111335449?w=400',
            json.dumps({
                'zones': [
                    {'id': 'left_leg_slit', 'name': 'Left Leg Outer Panel', 'max_w_mm': 180, 'max_h_mm': 240},
                    {'id': 'right_leg_slit', 'name': 'Right Leg Outer Panel', 'max_w_mm': 180, 'max_h_mm': 240},
                    {'id': 'waistband_center', 'name': 'Front Waistband Crest', 'max_w_mm': 80, 'max_h_mm': 45}
                ]
            }),
            json.dumps({
                'cdr_version': 'CorelDraw 2024',
                'bleed_margin_mm': 12,
                'color_space': 'CMYK',
                'resolution_dpi': 300
            })
        ),
        (
            5,
            'BJJ Gi Embroidery & Patch CDR Blueprint',
            'CDR-BJJ-03',
            '/uploads/templates/bjj_gi_blueprint_v1.cdr',
            'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=400',
            json.dumps({
                'zones': [
                    {'id': 'lapel_left', 'name': 'Left Lapel Patch', 'max_w_mm': 100, 'max_h_mm': 100},
                    {'id': 'back_skirt', 'name': 'Lower Back Skirt', 'max_w_mm': 300, 'max_h_mm': 120},
                    {'id': 'pant_side', 'name': 'Outer Thigh Seam Patch', 'max_w_mm': 100, 'max_h_mm': 250}
                ]
            }),
            json.dumps({
                'cdr_version': 'CorelDraw Vector (.cdr/.eps)',
                'stitch_mapping': 'Tajima DST / Barudan / Wilcom compatible'
            })
        )
    ]
    cursor.executemany('''
    INSERT INTO templates (category_id, name, template_code, file_path, preview_image, zones_json, cdr_metadata_json)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', templates_data)

    # Sample Initial Orders
    # Order 1: ZAM-401-26 (In Production - as specified in system design)
    cursor.execute('''
    INSERT INTO orders (order_number, user_id, customer_name, customer_email, customer_phone, status, total_amount, paid_amount, production_deadline, tracking_number, courier, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        'ZAM-401-26',
        2,
        'Marcus Vance',
        'athlete@zamforward.com',
        '+1 555-234-5678',
        'Production',
        850.00,
        425.00,
        '2026-11-15',
        'DHL-EXP-992144810',
        'DHL Express',
        'Apex Dojo team kit. 15 custom sublimated rashguards with gold foil embroidery crest.'
    ))
    order1_id = cursor.lastrowid

    # Order 1 items
    cursor.execute('''
    INSERT INTO order_items (order_id, product_id, product_name, quantity, size, color, unit_price, subtotal, design_config_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order1_id,
        1,
        'Apex Sublimated Short-Sleeve Rashguard',
        15,
        'L',
        'Combat Cyan / Carbon Black',
        54.00,
        810.00,
        json.dumps({
            'team_name': 'Apex Grappling Dojo',
            'logo_file': 'apex_crest.png',
            'sleeve_text': 'VANCE BJJ',
            'collar_style': 'Crew Rib',
            'template_ref': 'CDR-RG-01'
        })
    ))

    # Order 1 Invoice
    cursor.execute('''
    INSERT INTO invoices (order_id, invoice_number, subtotal, tax_rate, tax_amount, discount, total, deposit_required, status, line_items_json, due_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order1_id,
        'INV-ZAM-401-26',
        810.00,
        0.05,
        40.00,
        0.00,
        850.00,
        425.00,
        'Deposit Cleared',
        json.dumps([{'desc': '15x Apex Pro Rashguards (Custom Sublimation)', 'total': 810.00}, {'desc': 'Production Setup & Artwork Separation', 'total': 40.00}]),
        '2026-10-30'
    ))

    # Order 1 Payment slip
    cursor.execute('''
    INSERT INTO payment_slips (order_id, slip_file_path, relative_url, amount, bank_reference, status, verified_at, verified_by)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order1_id,
        'uploads/payment_slips/sample_slip_401.pdf',
        '/uploads/payment_slips/sample_slip_401.pdf',
        425.00,
        'WIRE-USAA-481920',
        'Verified & Cleared',
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Staff (ZamForward Ops)'
    ))

    # Order 1 Audit log
    cursor.execute('''
    INSERT INTO audit_status_logs (order_id, previous_status, new_status, changed_by, comments)
    VALUES (?, ?, ?, ?, ?)
    ''', (order1_id, 'In Progress', 'Production', 'ZamForward Ops', 'Fabric printing & sublimation laser cut completed. Sent to sewing floor.'))

    # Order 2: ZAM-402-26 (Invoice Sent - Awaiting 50% deposit)
    cursor.execute('''
    INSERT INTO orders (order_number, user_id, customer_name, customer_email, customer_phone, status, total_amount, paid_amount, production_deadline, tracking_number, courier, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        'ZAM-402-26',
        3,
        'Elena Rostova',
        'elena@apexdojo.com',
        '+44 7911-123456',
        'Invoice Sent',
        405.00,
        0.00,
        'TBD upon deposit',
        '',
        '',
        'Initial order of 3 IBJJF Gold Weave Gis with Blue belt embroidery.'
    ))
    order2_id = cursor.lastrowid

    cursor.execute('''
    INSERT INTO order_items (order_id, product_id, product_name, quantity, size, color, unit_price, subtotal, design_config_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order2_id,
        4,
        'IBJJF Pro Gold Weave Kimono (Gi)',
        3,
        'A2',
        'Blue Belt Rank',
        135.00,
        405.00,
        json.dumps({'team_name': 'Rostova Fight Club', 'template_ref': 'CDR-BJJ-03'})
    ))

    cursor.execute('''
    INSERT INTO invoices (order_id, invoice_number, subtotal, tax_rate, tax_amount, discount, total, deposit_required, status, line_items_json, due_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order2_id,
        'INV-ZAM-402-26',
        405.00,
        0.00,
        0.00,
        0.00,
        405.00,
        202.50,
        'Pending 50% Deposit',
        json.dumps([{'desc': '3x IBJJF Gold Weave Gis (Blue Belt Rank)', 'total': 405.00}]),
        '2026-11-05'
    ))

    # Order 3: ZAM-403-26 (Confirmed - Newly received by ZamForward)
    cursor.execute('''
    INSERT INTO orders (order_number, user_id, customer_name, customer_email, customer_phone, status, total_amount, paid_amount, production_deadline, tracking_number, courier, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        'ZAM-403-26',
        2,
        'Marcus Vance',
        'athlete@zamforward.com',
        '+1 555-234-5678',
        'Confirmed',
        240.00,
        0.00,
        'Pending Review',
        '',
        '',
        'Order submitted through Custom AI Studio. Artwork attached.'
    ))
    order3_id = cursor.lastrowid

    cursor.execute('''
    INSERT INTO order_items (order_id, product_id, product_name, quantity, size, color, unit_price, subtotal, design_config_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order3_id,
        3,
        'Apex Combat Flex-Split MMA Shorts',
        5,
        'M',
        'Mat Charcoal',
        48.00,
        240.00,
        json.dumps({'template_ref': 'CDR-MMA-02', 'custom_patch': 'Falcon Wing'})
    ))

    conn.commit()
    conn.close()
    print("Database seeded with sample combat products, categories, templates, and ZAM-401-26 orders successfully.")

if __name__ == '__main__':
    from file_manager import init_file_directories
    init_file_directories()
    init_db()
    seed_db()
