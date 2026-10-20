import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('renderVectorGraphics')
print("Found at:", idx)
if idx != -1:
    print(html[idx-50:idx+600])
