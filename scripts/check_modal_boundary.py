with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<!-- ================= FULL-SCREEN INTERACTIVE MODALS')
print("Snippet before FULL-SCREEN INTERACTIVE MODALS:")
print(text[pos-200:pos+100])
