with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('const $')
print(html[idx:idx+200])
