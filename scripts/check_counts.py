import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for term in ['Official BJJ', 'Batch 43 Production Active', '6-Needle Flatlock', 'Atelier Spotlight', 'AI 3D Studio & CorelDraw Pattern Engine', 'Combat Apparel Atelier']:
    count = html.count(term)
    print(f"'{term}': {count} occurrences")
