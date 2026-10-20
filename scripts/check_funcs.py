with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

funcs = ['openAiStudioModal', 'openCdrTemplateVault', 'openAuthModal', 'toggleStaffConsole', 'openCustomOrderModal']
for fn in funcs:
    print(f"{fn} in index.html: {fn in html}")
