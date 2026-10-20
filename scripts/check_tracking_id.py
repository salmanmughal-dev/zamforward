with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<section[^>]*id=["\'][^"\']*track[^"\']*["\'][^>]*>', html, re.IGNORECASE)
print("Tracking section matches:", matches)
if not matches:
    # check where class="zt" is
    idx = html.find('class="zt"')
    print("Found zt at:", idx)
    print(html[idx-150:idx+150])
