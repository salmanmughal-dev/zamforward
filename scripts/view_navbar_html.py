with open('scripts/navbar_component.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect all lines
lines = content.splitlines()
print(f"Total lines: {len(lines)}")
for i in range(0, len(lines), 30):
    print(f"--- Line {i+1} to {min(i+30, len(lines))} ---")
    for j in range(i, min(i+5, len(lines))):
        print(lines[j])
