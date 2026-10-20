# Let's inspect the exact CSS rules in scripts/navbar_component.css
with open('scripts/navbar_component.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("CSS Total characters:", len(css))
print("First 400 chars:")
print(css[:400])
print("...")
print("Last 400 chars:")
print(css[-400:])
