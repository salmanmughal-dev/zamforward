import re

with open('user_prompt_10.txt', 'r', encoding='utf-8') as f:
    text = f.read()

body_m = re.search(r'<body>(.*?)<!-- Demo page content -->', text, re.DOTALL)
if body_m:
    print("Navbar HTML before demo content found, length:", len(body_m.group(1).strip()))
    with open('scripts/navbar_component.html', 'w', encoding='utf-8') as out:
        out.write(body_m.group(1).strip())

js_m = re.search(r'<script>(.*?)</script>', text, re.DOTALL)
if js_m:
    print("JS found, length:", len(js_m.group(1).strip()))
    with open('scripts/navbar_component.js', 'w', encoding='utf-8') as out:
        out.write(js_m.group(1).strip())

style_m = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
if style_m:
    print("CSS found, length:", len(style_m.group(1).strip()))
    with open('scripts/navbar_component.css', 'w', encoding='utf-8') as out:
        out.write(style_m.group(1).strip())
