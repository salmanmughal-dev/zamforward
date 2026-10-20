with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 94367
print(text[pos-250:pos+50])
