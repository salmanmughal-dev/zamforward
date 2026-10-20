import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'>ZF<', html)]
print("Total '>ZF<' found:", len(matches))
for p in matches:
    print(html[p-100:p+80].replace('\n', ' '))
    print('---')
