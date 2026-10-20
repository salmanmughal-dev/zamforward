import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_ann = html.find('<!-- Announcement -->')
if idx_ann == -1:
    idx_ann = html.find('class="ann"')
print(html[idx_ann-50:idx_ann+1200])
