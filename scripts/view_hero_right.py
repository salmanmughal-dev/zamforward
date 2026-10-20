import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_idx = html.find('<!-- Right Atelier Spotlight Card')
if hero_idx == -1:
    hero_idx = html.find('Atelier Spotlight')
print(html[hero_idx-100:hero_idx+2000])
