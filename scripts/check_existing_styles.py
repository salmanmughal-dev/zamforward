with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
styles = re.findall(r'<style>(.*?)</style>', html, re.DOTALL)
print(f"Total <style> blocks in index.html: {len(styles)}")
for i, s in enumerate(styles):
    print(f"Style {i+1} length: {len(s)}")
    print(s[:100].strip())
