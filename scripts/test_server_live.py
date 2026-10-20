import urllib.request

url = 'http://127.0.0.1:5000/'
try:
    with urllib.request.urlopen(url) as r:
        data = r.read().decode('utf-8')
        print('HTTP status:', r.status)
        print('Content length:', len(data))
        print('Announcement bar present:', 'class="ann"' in data)
        print('Atelier Spotlight present:', 'Atelier Spotlight' in data)
        print('AI 3D Pattern Engine section present:', 'AI 3D Studio &amp; CorelDraw Pattern Engine' in data)
        print('Batch 43 Production Active present:', 'Batch 43 Production Active' in data)
        print('Official BJJ present:', 'Official BJJ' in data)
except Exception as e:
    print("Error:", e)
