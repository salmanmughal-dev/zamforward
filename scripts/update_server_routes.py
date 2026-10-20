with open('server.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add /api/orders/next-id and /order-file
if '/api/orders/next-id' not in code:
    marker = "@app.route('/api/orders', methods=['POST'])"
    addition = """@app.route('/api/orders/next-id', methods=['GET'])
def get_next_order_id():
    conn = get_db_connection()
    last_row = conn.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1").fetchone()
    next_seq = 400 + (last_row['id'] + 1 if last_row else 1)
    current_year_suffix = datetime.now().strftime('%y')
    conn.close()
    return jsonify({
        'next_order_id': f"ZAM-{next_seq}-{current_year_suffix}",
        'next_sequence': next_seq
    })

"""
    code = code.replace(marker, addition + marker)
    print("Added /api/orders/next-id to server.py")

if "@app.route('/order-file')" not in code:
    marker = "@app.route('/')"
    addition = """@app.route('/order-file')
def order_file():
    return send_from_directory('public', 'order-file.html')

"""
    code = code.replace(marker, addition + marker)
    print("Added /order-file route to server.py")

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated server.py")
