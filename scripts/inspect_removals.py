import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check announcement bar
print("=== 1. Announcement bar ===")
idx_ann = html.find('class="ann"')
if idx_ann != -1:
    print("Found .ann at", idx_ann)
    print(html[idx_ann-20:idx_ann+250])

# 2. Check logo-t in .logo
print("\n=== 2. logo-t ===")
for m in re.finditer(r'<a class="logo".*?</a>', html, re.DOTALL):
    print(m.group(0))

# 3. Check 'Batch 43 Production Active', '6-Needle Flatlock', 'Official BJJ & MMA Combat Apparel Atelier'
print("\n=== 3. Hero tags and subtitle ===")
for phrase in ['Batch 43 Production Active', '6-Needle Flatlock', 'Official BJJ & MMA Combat Apparel Atelier']:
    pos = html.find(phrase)
    print(f"'{phrase}': pos={pos}")
    if pos != -1:
        print(html[pos-100:pos+200])
        print("---")

# 4. Check 'Atelier Spotlight'
print("\n=== 4. Atelier Spotlight ===")
pos_spot = html.find('Atelier Spotlight')
print(f"'Atelier Spotlight': pos={pos_spot}")
if pos_spot != -1:
    print(html[pos_spot-100:pos_spot+400])

# 5. Check 'AI 3D Studio & CorelDraw Pattern Engine'
print("\n=== 5. AI 3D Studio & CorelDraw Pattern Engine ===")
pos_engine = html.find('AI 3D Studio & CorelDraw Pattern Engine')
print(f"'AI 3D Studio & CorelDraw Pattern Engine': pos={pos_engine}")
if pos_engine != -1:
    print(html[pos_engine-150:pos_engine+300])
