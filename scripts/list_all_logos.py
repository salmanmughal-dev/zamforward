import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [(m.start(), html[max(0, m.start()-30):min(len(html), m.end()+50)].replace('\n', ' ')) 
           for m in re.finditer(r'logo', html, re.IGNORECASE)]

print(f"Total: {len(matches)}")
for idx, (pos, snippet) in enumerate(matches):
    print(f"{idx+1}. Pos {pos}: {snippet}")
