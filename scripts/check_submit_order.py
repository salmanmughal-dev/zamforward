with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('async function submitStudioOrder')
if idx == -1:
    idx = text.find('submitStudioOrder')
print(text[idx:idx+1500])
