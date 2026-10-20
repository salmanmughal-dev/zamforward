import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'invoiceModal', html)]
print("invoiceModal matches:", len(matches))
for p in matches[:2]:
    print(html[p:p+600])
    print("---")
