with open('scripts/navbar_component.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines):
    if any(k in line for k in ['<header', '<nav', 'id=', 'class="logo"', 'class="cta"', 'Start Designing', 'AI 3D', 'Vault', 'Track', 'class="drawer"']):
        print(f"Line {i+1}: {line.strip()[:100]}")
