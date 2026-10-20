with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [(m.start(), m.group(0)) for m in re.finditer(r'<[^>]*class=["\'][^"\']*\blogo\b[^"\']*["\'][^>]*>', html)]
print(f"Found {len(matches)} tags with class 'logo':")
for pos, tag in matches:
    print(pos, tag)
    print("Context:", html[pos:pos+350].strip())
    print("---")
