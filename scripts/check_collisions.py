import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for cls in ['btn', 'badge', 'tag', 'wrap', 'line', 'row', 'menu', 'sub', 'active', 'price']:
    pattern = r'class=["\'][^"\']*\b' + cls + r'\b[^"\']*["\']'
    matches = len(re.findall(pattern, html))
    print(f'{cls}: {matches} occurrences in current index.html')
