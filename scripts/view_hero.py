import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find the hero section
hero_idx = html.find('<!-- 1. HERO SECTION')
if hero_idx == -1:
    hero_idx = html.find('Official BJJ')
print(html[hero_idx-100:hero_idx+2500])
