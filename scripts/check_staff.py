with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'.{0,50}(?:staffConsole|staff-console|Console|Staff).{0,50}', html, re.IGNORECASE)
for m in matches[:10]:
    print(m.strip())
