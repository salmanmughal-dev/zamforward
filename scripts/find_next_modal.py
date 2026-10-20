with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

modal_start = text.find('id="aiStudioModal"')
tag_start = text.rfind('<div', 0, modal_start)

# Find next modal id="
idx = tag_start + 100
modals = []
while True:
    pos = text.find('id="', idx)
    if pos == -1 or pos > tag_start + 50000:
        break
    id_val = text[pos+4:text.find('"', pos+4)]
    if 'Modal' in id_val or 'Drawer' in id_val:
        modals.append((pos, id_val))
    idx = pos + 4

print("Modals found after aiStudioModal:")
for pos, m in modals:
    print(f"  Pos: {pos}, ID: {m}")
    # print preceding comment or snippet
    print("    Preceding:", text[pos-100:pos])
