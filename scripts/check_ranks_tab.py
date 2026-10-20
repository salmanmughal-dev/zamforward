import json

with open(r'public/graphics/graphics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('{')
end = text.rfind('}') + 1
data = json.loads(text[start:end])

first = data['items'][0]
print("Keys of item:", list(first.keys()))
print("First item:", {k: first[k] for k in first if k != 'body'})

ranks = [it for it in data['items'] if it.get('cat') == 'ranks']
print(f"\nRanks items ({len(ranks)}):")
for r in ranks:
    print(f"  id='{r['id']}', name='{r['name']}', aspect={r.get('aspect')}")
