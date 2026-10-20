with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("catalog id:", "id=\"catalog\"" in html or "id='catalog'" in html)
print("workflow id:", "id=\"workflow\"" in html or "id='workflow'" in html)
if not ("id=\"catalog\"" in html):
    # find where catalog is
    m = re.findall(r'<section[^>]*id=["\'][^"\']*["\'][^>]*>', html)
    print("All section ids:", m)
