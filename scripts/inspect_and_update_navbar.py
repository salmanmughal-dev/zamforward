import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find body start, header start/end
body_idx = html.find('<body')
body_close = html.find('>', body_idx) + 1
h_start = html.find('<header')
h_end = html.find('</header>') + len('</header>')

print(f"Body starts at {body_close}")
print(f"Header starts at {h_start}, ends at {h_end}")
print("Header snippet:")
print(html[h_start:h_start+300])

# What is before <header>? Any announcement rail?
print("Before header (up to body tag):")
print(html[body_close:h_start])
