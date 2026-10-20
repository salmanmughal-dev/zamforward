import re

with open('user_prompt_10.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract parts:
style_m = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
css_content = style_m.group(1).strip() if style_m else ""

# Extract SVG sprite and components
# In the user prompt, after <body>:
body_m = re.search(r'<body>(.*?)<script>(.*?)</script>', text, re.DOTALL)
body_html = body_m.group(1).strip() if body_m else ""
js_content = body_m.group(2).strip() if body_m else ""

print("CSS length:", len(css_content))
print("Body HTML length:", len(body_html))
print("JS length:", len(js_content))

# Look at main sections in body_html
# It has:
# 1. <!-- SVG icon sprite -->
# 2. <!-- Announcement bar -->
# 3. <!-- Header -->
# 4. <!-- Scrim -->
# 5. <!-- Cart Drawer -->
# 6. <!-- Mobile Nav Drawer -->
# 7. <!-- Demo page content --> (We exclude this demo main because public/index.html has the full real app!)

sections = re.split(r'<!--\s*(.*?)\s*-->', body_html)
print("Sections count:", len(sections))
for i in range(1, len(sections), 2):
    print(f"Section header: {sections[i]} (len={len(sections[i+1])})")

