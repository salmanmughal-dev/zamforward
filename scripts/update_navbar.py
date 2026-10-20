import re

# Read original index.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Read navbar CSS
with open('scripts/navbar_component.css', 'r', encoding='utf-8') as f:
    nav_css = f.read().strip()

# Clean out .demo styles from nav_css as they are demo filler
nav_css = re.sub(r'/\*\s*Demo page filler\s*\*/.*$', '', nav_css, flags=re.DOTALL).strip()

# 2. Read navbar HTML
with open('scripts/navbar_component.html', 'r', encoding='utf-8') as f:
    nav_html = f.read().strip()

# 3. Read navbar JS
with open('scripts/navbar_component.js', 'r', encoding='utf-8') as f:
    nav_js = f.read().strip()

print("Original HTML length:", len(html))
print("Navbar CSS length:", len(nav_css))
print("Navbar HTML length:", len(nav_html))
print("Navbar JS length:", len(nav_js))
