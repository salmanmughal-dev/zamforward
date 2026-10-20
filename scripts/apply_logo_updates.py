import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .logo-badge
logo_badge_css = """
.logo-badge{height:46px;width:auto;border-radius:10px;object-fit:cover;background:#080b0e;border:1px solid rgba(255,255,255,.1);box-shadow:0 4px 12px -2px rgba(17,20,23,.22);transition:transform .2s ease,box-shadow .2s ease;display:block;flex-shrink:0}
.logo:hover .logo-badge{transform:translateY(-1px) scale(1.02);box-shadow:0 6px 16px -2px rgba(8,131,149,.3)}
.hdr.stuck .logo-badge{height:38px}
"""

if '.logo-badge{' not in html:
    html = html.replace('.logo{display:flex;', logo_badge_css + '\n.logo{display:flex;')

# 2. Main Navbar Header Logo
old_header_logo = """<a class="logo" href="#" aria-label="ZamForward home">
          <span class="logo-mark">ZF</span>
          <span class="logo-t"><b>ZAMFORWARD</b><small>Combat Apparel Atelier</small></span>
        </a>"""

new_header_logo = """<a class="logo" href="#" aria-label="ZamForward home">
          <img src="/images/logo.jpeg" alt="ZamForward Combat Apparel" class="logo-badge" />
          <span class="logo-t"><b>ZAMFORWARD</b><small>Combat Apparel Atelier</small></span>
        </a>"""

if old_header_logo in html:
    html = html.replace(old_header_logo, new_header_logo)
    print("Replaced main header logo!")
else:
    # Try more flexible whitespace match
    import re
    p = r'<a class="logo" href="#" aria-label="ZamForward home">\s*<span class="logo-mark">ZF</span>\s*<span class="logo-t"><b>ZAMFORWARD</b><small>Combat Apparel Atelier</small></span>\s*</a>'
    if re.search(p, html):
        html = re.sub(p, new_header_logo, html)
        print("Replaced main header logo with regex!")
    else:
        print("WARNING: Could not find main header logo!")

# 3. Mobile Nav Drawer Header Logo
old_drawer_logo = """<div class="d-head"><a class="logo" href="#"><span class="logo-mark" style="width:38px;height:38px;font-size:15px">ZF</span><span class="logo-t"><b style="font-size:18px">ZAMFORWARD</b></span></a>"""
new_drawer_logo = """<div class="d-head"><a class="logo" href="#"><img src="/images/logo.jpeg" alt="ZamForward" style="height:38px;width:auto;border-radius:8px;background:#080b0e;box-shadow:0 2px 6px rgba(0,0,0,0.2)" /><span class="logo-t"><b style="font-size:18px">ZAMFORWARD</b><small style="font-size:9.5px;color:var(--cyan-d);display:block;letter-spacing:.15em;text-transform:uppercase">Combat Apparel</small></span></a>"""

if old_drawer_logo in html:
    html = html.replace(old_drawer_logo, new_drawer_logo)
    print("Replaced mobile drawer logo!")
else:
    import re
    p = r'<div class="d-head"><a class="logo" href="#"><span class="logo-mark"[^>]*>ZF</span><span class="logo-t"><b style="font-size:18px">ZAMFORWARD</b></span></a>'
    if re.search(p, html):
        html = re.sub(p, new_drawer_logo, html)
        print("Replaced mobile drawer logo with regex!")
    else:
        print("WARNING: Could not find mobile drawer logo!")

# 4. Website Footer Logo
old_footer_logo = """<div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-bold text-sm">ZF</div>
            <span class="font-headline-sm text-lg font-bold tracking-tight text-[#111417] uppercase">ZamForward Combat</span>
          </div>"""

new_footer_logo = """<div class="flex items-center gap-3">
            <img src="/images/logo.jpeg" alt="ZamForward Combat" class="h-11 w-auto rounded-xl shadow-md border border-black/10 bg-[#080b0e]" />
            <div>
              <span class="font-headline-sm text-lg font-bold tracking-tight text-[#111417] uppercase block">ZamForward Combat</span>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#088395] font-bold">Combat Apparel Atelier</span>
            </div>
          </div>"""

if old_footer_logo in html:
    html = html.replace(old_footer_logo, new_footer_logo)
    print("Replaced footer logo!")
else:
    import re
    p = r'<div class="flex items-center gap-3">\s*<div class="w-8 h-8 rounded-lg bg-\[#111417\][^>]*>ZF</div>\s*<span class="font-headline-sm text-lg font-bold tracking-tight text-\[#111417\] uppercase">ZamForward Combat</span>\s*</div>'
    if re.search(p, html):
        html = re.sub(p, new_footer_logo, html)
        print("Replaced footer logo with regex!")
    else:
        print("WARNING: Could not find footer logo!")

# 5. AI 3D Studio Modal Header Logo
old_ai_logo = """<a href="#" class="flex items-center gap-2.5 flex-shrink-0 group">
      <div class="w-9 h-9 rounded-xl bg-sky-600 text-white flex items-center justify-center font-extrabold text-base shadow-sm group-hover:bg-slate-900 transition-colors">
        ZF
      </div>
      <div class="flex flex-col">
        <span class="text-lg font-bold tracking-tight text-slate-900 leading-tight">ZamForward</span>
        <span class="text-[11px] font-medium text-sky-600 -mt-0.5">Custom Fight Gear</span>
      </div>
    </a>"""

new_ai_logo = """<a href="#" class="flex items-center gap-2.5 flex-shrink-0 group">
      <img src="/images/logo.jpeg" alt="ZamForward" class="h-10 w-auto rounded-xl shadow-md border border-slate-700/20 bg-[#080b0e]" />
      <div class="flex flex-col">
        <span class="text-lg font-bold tracking-tight text-slate-900 leading-tight">ZamForward</span>
        <span class="text-[11px] font-medium text-sky-600 -mt-0.5">Custom Fight Gear Atelier</span>
      </div>
    </a>"""

if old_ai_logo in html:
    html = html.replace(old_ai_logo, new_ai_logo)
    print("Replaced AI Studio modal logo!")
else:
    import re
    p = r'<a href="#" class="flex items-center gap-2\.5 flex-shrink-0 group">\s*<div class="w-9 h-9 rounded-xl bg-sky-600[^>]*>\s*ZF\s*</div>\s*<div class="flex flex-col">\s*<span class="text-lg font-bold[^"]*">ZamForward</span>\s*<span class="text-\[11px\][^"]*">Custom Fight Gear</span>\s*</div>\s*</a>'
    if re.search(p, html):
        html = re.sub(p, new_ai_logo, html)
        print("Replaced AI Studio modal logo with regex!")
    else:
        print("WARNING: Could not find AI Studio modal logo!")

# 6. Staff Console Drawer Header Logo
old_staff_header = """<div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-secondary animate-pulse"></span>
      <h3 class="font-headline-sm text-headline-sm text-primary uppercase">ZamForward Staff Atelier Console</h3>
    </div>"""

new_staff_header = """<div class="flex items-center gap-3">
      <img src="/images/logo.jpeg" alt="ZamForward" class="h-8 w-auto rounded-md shadow-sm border border-slate-700/20 bg-[#080b0e]" />
      <span class="w-2.5 h-2.5 rounded-full bg-secondary animate-pulse"></span>
      <h3 class="font-headline-sm text-headline-sm text-primary uppercase">ZamForward Staff Atelier Console</h3>
    </div>"""

if old_staff_header in html:
    html = html.replace(old_staff_header, new_staff_header)
    print("Replaced Staff Console drawer logo!")

# 7. AI 3D Studio: Add Official ZamForward 3D Logo to presets and graphics renderer
old_presets_def = """  const presets = [
    { name: 'Wings Crest', preset: 'wings', icon: '★' },"""

new_presets_def = """  const presets = [
    { name: 'ZamForward 3D Crest', preset: 'zamforward_official', icon: 'ZF' },
    { name: 'Wings Crest', preset: 'wings', icon: '★' },"""

if old_presets_def in html:
    html = html.replace(old_presets_def, new_presets_def)
    print("Added ZamForward 3D Crest to AI Studio presets!")

# Support 'zamforward_official' in renderVectorGraphic
old_wings_block = """  if (el.preset === 'wings') {"""
new_wings_block = """  if (el.preset === 'zamforward_official') {
    if (!window._zfLogoImg) {
      window._zfLogoImg = new Image();
      window._zfLogoImg.src = '/images/logo.jpeg';
      window._zfLogoImg.onload = () => { if (typeof update3DTexture === 'function') update3DTexture(); };
    }
    if (window._zfLogoImg.complete && window._zfLogoImg.naturalWidth > 0) {
      try {
        ctx.drawImage(window._zfLogoImg, -45, -25, 90, 50);
      } catch(e) {}
    } else {
      ctx.font = 'bold 16px Impact';
      ctx.textAlign = 'center';
      ctx.fillText('ZAMFORWARD', 0, 0);
    }
  } else if (el.preset === 'wings') {"""

if old_wings_block in html and "el.preset === 'zamforward_official'" not in html:
    html = html.replace(old_wings_block, new_wings_block)
    print("Added zamforward_official handler to renderVectorGraphic!")

# Write updated files
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved changes to public/index.html and code.html!")
