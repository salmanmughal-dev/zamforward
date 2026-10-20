with open('server.py', 'r', encoding='utf-8') as f:
    code = f.read()

alias_code = '''
@app.route('/api/track/<order_number>', methods=['GET'])
def track_order_alias(order_number):
    return get_order_detail(order_number)
'''

if '/api/track/<order_number>' not in code:
    code = code.replace("@app.route('/api/orders/<order_number>', methods=['GET'])", alias_code + "\n@app.route('/api/orders/<order_number>', methods=['GET'])")
    with open('server.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Added /api/track/<order_number> alias to server.py")
else:
    print("Alias already in server.py")
