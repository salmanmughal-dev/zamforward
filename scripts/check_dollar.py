with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("jQuery in index.html:", "jquery" in html.lower())
print("const $ =" in html)
print("let $ =" in html)
print("var $ =" in html)
