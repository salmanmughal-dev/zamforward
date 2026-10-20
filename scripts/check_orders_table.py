with open('database.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('CREATE TABLE IF NOT EXISTS orders')
print(text[idx:idx+1200])
