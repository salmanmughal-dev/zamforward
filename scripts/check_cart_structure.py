import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="cart"')
print(text[idx:idx+1200])
