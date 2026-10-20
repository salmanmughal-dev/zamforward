import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

terms = [
    'Official BJJ',
    'Combat Apparel Atelier',
    'Pattern Engine',
    'CorelDraw',
    'Engine',
    'Spotlight',
    'Configure in 3D',
    'arrow_forward'
]

for t in terms:
    matches = [m.start() for m in re.finditer(re.escape(t), html, re.IGNORECASE)]
    print(f"Term '{t}': {len(matches)} occurrences")
    for p in matches[:3]:
        print("  ", html[max(0, p-60):min(len(html), p+120)].replace('\n', ' '))
