with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for studio variables and functions
pos_start = text.find('// =========================================================================')
if pos_start == -1:
    pos_start = text.find('function openAiStudioModal')

print("Studio script search:", pos_start)
# Let's see what is before openAiStudioModal
print(text[pos_start-200:pos_start+200])

# Where does the studio script end?
# Let's look for functions after openAiStudioModal:
# Does it end before closeModal or lookupOrder or something?
for marker in ['function closeModal', 'function openModal', 'function lookupOrder', 'function openSlipModal', 'function openInvoiceModal']:
    p = text.find(marker, pos_start)
    print(f"Marker '{marker}': {p}")
