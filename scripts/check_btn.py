import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for m in re.finditer(r'<[^>]*class=["\'][^"\']*\bbtn\b[^"\']*["\'][^>]*>', html):
    print(m.group(0)[:120])
