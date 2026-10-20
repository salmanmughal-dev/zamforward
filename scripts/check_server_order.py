with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('def create_order():')
print(text[idx:idx+1200])
