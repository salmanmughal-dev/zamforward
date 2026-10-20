with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'footer', html, re.IGNORECASE)]
print("Footer occurrences:", len(matches))
for p in matches[:5]:
    print(html[p-50:p+300])
    print("===")
