with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

modal_start = text.find('id="aiStudioModal"')
modal_end = text.find('<!-- ================= MODALS', modal_start)
modal_html = text[modal_start:modal_end]

tabs = re.findall(r'tabPanel_[a-zA-Z0-9_]+|switchStudioTab\([^)]*\)', modal_html)
print('Studio tabs:', set(tabs))

# Check for Ranks or workflow tabs/sections
for kw in ['workflow', 'Ranks', 'ranks', 'Workflow']:
    matches = [m.start() for m in re.finditer(re.escape(kw), text)]
    print(f"Keyword '{kw}': {len(matches)} occurrences")
    for p in matches[:4]:
        print("  Snippet:", text[max(0, p-60):min(len(text), p+120)].replace('\n', ' '))
