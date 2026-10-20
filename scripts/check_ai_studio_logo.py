import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'logo', html, re.IGNORECASE)]
print(f"Total 'logo' mentions: {len(matches)}")

# Check AI studio script for logo
idx = html.find('openAiStudioModal')
if idx != -1:
    studio_sub = html[idx:idx+8000]
    logo_sub_matches = [m.start() for m in re.finditer(r'logo', studio_sub, re.IGNORECASE)]
    print(f"Logo mentions in AI studio area: {len(logo_sub_matches)}")
    for p in logo_sub_matches[:5]:
        print(studio_sub[p-40:p+100])
        print("---")
