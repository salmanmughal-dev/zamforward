with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the last 1500 chars before </body>
body_end = html.rfind('</body>')
print(html[body_end-1500:body_end])
