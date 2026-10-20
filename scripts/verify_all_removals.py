import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("1. 'class=\"ann\"' in html:", 'class="ann"' in html)
print("   'Batch 43 is in production' in html:", 'Batch 43 is in production' in html)
print("   'topAnn' in html:", 'topAnn' in html)

print("\n2. Main logo HTML:")
idx = html.find('class="logo"')
print(html[idx-10:idx+250])

print("\n3. 'Official BJJ & MMA' in html:", 'Official BJJ & MMA' in html)
print("   'Batch 43 Production Active' in html:", 'Batch 43 Production Active' in html)
print("   '6-Needle Flatlock' in html:", '6-Needle Flatlock' in html)

print("\n4. 'Atelier Spotlight' in html:", 'Atelier Spotlight' in html)
print("   'Apex Pro Sublimation Kit' in html:", 'Apex Pro Sublimation Kit' in html)
print("   '450 GSM Poly-Spandex • Anti-slip silicone waist' in html:", '450 GSM Poly-Spandex • Anti-slip silicone waist' in html)
print("   'Configure in 3D' in html:", 'Configure in 3D' in html)

print("\n5. 'Pattern Engine' in html:", 'Pattern Engine' in html)
print("   'AI 3D Studio & CorelDraw Pattern Engine' in html:", 'AI 3D Studio & CorelDraw Pattern Engine' in html)
