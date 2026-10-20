with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = 139365
pos_end = text.find('</script>', pos_start) + len('</script>')
print(f"Studio script ends at: {pos_end}")
print("Snippet at end of studio script:")
print(text[pos_end-300:pos_end+300])
