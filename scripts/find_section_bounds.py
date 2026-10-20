import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Pattern Engine')
# Find enclosing <section
sec_start = html.rfind('<section', 0, idx)
sec_end = html.find('</section>', idx) + len('</section>')

print(f"Section starts at {sec_start}, ends at {sec_end}")
print("--- Section Start ---")
print(html[sec_start:sec_start+250])
print("--- Section End ---")
print(html[sec_end-250:sec_end])
