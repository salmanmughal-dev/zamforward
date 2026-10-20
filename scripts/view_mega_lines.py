with open('scripts/navbar_component.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[200:349], start=201):
    print(f"{i}: {line.strip()}")
