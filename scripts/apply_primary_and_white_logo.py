import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def apply_updates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    initial_len = len(html)
    print(f"\nProcessing {filepath} (len: {initial_len})")

    # 1. Update logo container CSS and inline styles to white background
    # CSS .logo-badge
    html = re.sub(
        r'\.logo-badge\{[^}]*\}',
        '.logo-badge{height:52px;width:auto;border-radius:12px;object-fit:contain;background:#ffffff;border:1.5px solid #DFD9CC;box-shadow:0 2px 10px rgba(17,20,23,.06);padding:3px 8px;transition:transform .2s ease,box-shadow .2s ease;display:block;flex-shrink:0}',
        html
    )

    # In mobile drawer, footer, AI studio, staff console: change background:#080b0e / bg-[#080b0e] to #ffffff / bg-white
    html = html.replace('background:#080b0e;box-shadow:0 3px 10px rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.1)',
                        'background:#ffffff;box-shadow:0 2px 8px rgba(17,20,23,0.08);border:1.5px solid #DFD9CC;padding:2px 6px;')
    html = html.replace('bg-[#080b0e]', 'bg-white border border-[#DFD9CC]')
    html = html.replace('background:#080b0e', 'background:#ffffff')

    # Bump cache-buster on logo image
    import time
    cb = str(int(time.time()))
    html = re.sub(r'/images/logo\.jpeg(?:\?v=\d+)?', f'/images/logo.jpeg?v={cb}', html)

    # 2. Update Launch AI 3D Studio button in Hero to Primary Color (Combat Cyan #088395)
    # Old hero button:
    # <button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-lg bg-[#111417] text-[#F4F1EA] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#088395] transition-all shadow-md flex items-center gap-2 group">
    hero_btn_old = r'<button onclick="openAiStudioModal\(\)" class="px-6 py-3\.5 rounded-lg bg-\[#111417\] text-\[#F4F1EA\] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-\[#088395\] transition-all shadow-md flex items-center gap-2 group">'
    hero_btn_new = '<button onclick="openAiStudioModal()" class="px-7 py-3.5 rounded-xl bg-[#088395] text-white font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#066c7b] transition-all shadow-lg shadow-[#088395]/25 hover:shadow-xl flex items-center gap-2.5 group transform hover:-translate-y-0.5">'
    
    m_hbtn = re.search(hero_btn_old, html)
    if m_hbtn:
        html = html[:m_hbtn.start()] + hero_btn_new + html[m_hbtn.end():]
        print("Updated Hero 'Launch AI 3D Studio' button to primary cyan!")
    else:
        # Direct replacement if regex didn't hit
        target = 'px-6 py-3.5 rounded-lg bg-[#111417] text-[#F4F1EA] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#088395]'
        rep = 'px-7 py-3.5 rounded-xl bg-[#088395] text-white font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#066c7b] shadow-lg shadow-[#088395]/25'
        if target in html:
            html = html.replace(target, rep)
            print("Updated Hero button via string replace!")
        else:
            print("Warning: Could not match hero button target!")

    # 3. Remove "Where's my order?" section from landing page
    sec_where = r'<section class="zt" id="tracking" aria-labelledby="zt-title">.*?</section>'
    m_where = re.search(sec_where, html, re.DOTALL)
    if m_where:
        html = html[:m_where.start()] + html[m_where.end():]
        print("Removed 'Where\'s my order?' section!")
    else:
        # Fallback index search
        idx_w = html.find('Where\'s my order?')
        if idx_w != -1:
            s_start = html.rfind('<section', 0, idx_w)
            s_end = html.find('</section>', idx_w) + len('</section>')
            html = html[:s_start] + html[s_end:]
            print("Removed 'Where\'s my order?' section via index locator!")
        else:
            print("Warning: Could not find 'Where\'s my order?' section!")

    # 4. Make other key product / CTA action buttons use primary cyan color
    # E.g., Catalog "All Combat" active filter button
    html = html.replace('class="px-4 py-1.5 rounded-full bg-[#111417] text-[#F4F1EA] text-xs font-headline-sm uppercase font-bold">All Combat<',
                        'class="px-4 py-1.5 rounded-full bg-[#088395] text-white text-xs font-headline-sm uppercase font-bold shadow-sm">All Combat<')

    # Product quick order buttons in catalog: bg-[#111417] text-[#F4F1EA] -> bg-[#088395] text-white hover:bg-[#066c7b]
    html = html.replace('class="px-3.5 py-1.5 rounded-lg bg-[#111417] text-[#F4F1EA] text-xs font-bold uppercase hover:bg-[#088395]',
                        'class="px-3.5 py-1.5 rounded-lg bg-[#088395] text-white text-xs font-bold uppercase hover:bg-[#066c7b] shadow-sm')

    # Write out updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Saved {filepath} (new len: {len(html)})")

apply_updates('code.html')
apply_updates('public/index.html')
print("\nBoth code.html and public/index.html successfully updated!")
