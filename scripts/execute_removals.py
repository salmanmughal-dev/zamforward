import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

initial_len = len(html)
print(f"Initial file length: {initial_len}")

# 1. Remove Announcement bar (top black strip)
ann_pattern = r'<!-- Announcement -->\s*<div class="ann"[^>]*>.*?</div>\s*</div>\s*</div>'
m_ann = re.search(ann_pattern, html, re.DOTALL)
if m_ann:
    html = html[:m_ann.start()] + html[m_ann.end():]
    print("1. Successfully removed Announcement bar (black strip)!")
else:
    # Alternative direct substring find
    idx1 = html.find('<!-- Announcement -->')
    idx2 = html.find('<!-- Header -->')
    if idx1 != -1 and idx2 != -1 and idx1 < idx2:
        html = html[:idx1] + html[idx2:]
        print("1. Successfully removed Announcement bar via index locator!")
    else:
        print("WARNING: Could not locate Announcement bar!")

# 2. Adjust Logo & remove text in Navbar Header & Mobile Drawer
# Update CSS for .logo-badge to be 52px (42px stuck)
old_logo_css = r'\.logo-badge\{height:46px;[^}]*\}'
new_logo_css = '.logo-badge{height:52px;width:auto;border-radius:12px;object-fit:cover;background:#080b0e;border:1px solid rgba(255,255,255,.12);box-shadow:0 4px 14px -2px rgba(17,20,23,.25);transition:transform .2s ease,box-shadow .2s ease;display:block;flex-shrink:0}'
html = re.sub(old_logo_css, new_logo_css, html)
html = html.replace('.hdr.stuck .logo-badge{height:38px}', '.hdr.stuck .logo-badge{height:42px}')

# Header logo text removal
old_hdr_logo_pattern = r'<a class="logo" href="#" aria-label="ZamForward home">\s*<img src="/images/logo\.jpeg"[^>]*>\s*<span class="logo-t">.*?</span>\s*</a>'
new_hdr_logo = '<a class="logo" href="#" aria-label="ZamForward home">\n          <img src="/images/logo.jpeg" alt="ZamForward Combat Apparel" class="logo-badge" />\n        </a>'
m_logo = re.search(old_hdr_logo_pattern, html, re.DOTALL)
if m_logo:
    html = html[:m_logo.start()] + new_hdr_logo + html[m_logo.end():]
    print("2a. Successfully removed text from main navbar logo and adjusted logo!")
else:
    print("WARNING: Could not find main navbar logo text pattern!")

# Mobile drawer logo text removal
old_drawer_logo_pattern = r'<div class="d-head"><a class="logo" href="#">.*?</a>'
new_drawer_logo = '<div class="d-head"><a class="logo" href="#" aria-label="ZamForward home"><img src="/images/logo.jpeg" alt="ZamForward Combat Apparel" style="height:44px;width:auto;border-radius:10px;background:#080b0e;box-shadow:0 3px 10px rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.1)" /></a>'
m_dlogo = re.search(old_drawer_logo_pattern, html, re.DOTALL)
if m_dlogo:
    html = html[:m_dlogo.start()] + new_drawer_logo + html[m_dlogo.end():]
    print("2b. Successfully removed text from mobile drawer logo!")
else:
    print("WARNING: Could not find mobile drawer logo pattern!")

# 3. Remove "Official BJJ & MMA Combat Apparel Atelier" chip
hero_chip_pattern = r'<!-- Technical Chip / IBJJF Atelier Tag -->\s*<div class="inline-flex items-center gap-2[^>]*>.*?<span>Official BJJ &amp; MMA Combat Apparel Atelier</span>\s*</div>'
m_chip = re.search(hero_chip_pattern, html, re.DOTALL)
if m_chip:
    html = html[:m_chip.start()] + html[m_chip.end():]
    print("3. Successfully removed 'Official BJJ & MMA Combat Apparel Atelier' chip!")
else:
    # Alternative direct removal of div containing Official BJJ
    p2 = r'<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full[^>]*>.*?<span>Official BJJ &amp; MMA Combat Apparel Atelier</span>\s*</div>'
    m_chip2 = re.search(p2, html, re.DOTALL)
    if m_chip2:
        html = html[:m_chip2.start()] + html[m_chip2.end():]
        print("3. Successfully removed Official BJJ chip via fallback!")
    else:
        print("WARNING: Could not find Official BJJ chip!")

# 4. Remove floating badges (Batch 43, 6-Needle Flatlock) and bottom metadata bar (Atelier Spotlight...)
col5_pattern = r'<!-- Right Atelier Showcase / Product Showcase \(5 Columns\) -->.*?<!-- 2\. CATEGORY NAVIGATION RIBBON'
new_col5 = """<!-- Right Product Showcase (5 Columns) -->
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-2xl overflow-hidden shadow-xl bg-[#EDE8DE] border border-[#DFD9CC] group">
            <div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="/images/home-page.jpg"/>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 2. CATEGORY NAVIGATION RIBBON"""

m_col5 = re.search(col5_pattern, html, re.DOTALL)
if m_col5:
    html = html[:m_col5.start()] + new_col5 + html[m_col5.end():]
    print("4. Successfully removed Batch 43 beep, 6-Needle Flatlock tag, and Atelier Spotlight bottom bar!")
else:
    print("WARNING: Could not find Right Column 5 pattern!")

# 5. Remove "AI 3D Studio & CorelDraw Pattern Engine" section
sec_pattern = r'<section class="max-w-\[1360px\] mx-auto px-4 sm:px-8 w-full mb-20" id="custom-studio">.*?</section>'
m_sec = re.search(sec_pattern, html, re.DOTALL)
if m_sec:
    html = html[:m_sec.start()] + html[m_sec.end():]
    print("5. Successfully removed 'AI 3D Studio & CorelDraw Pattern Engine' section!")
else:
    idx_p = html.find('Pattern Engine')
    if idx_p != -1:
        s_start = html.rfind('<section', 0, idx_p)
        s_end = html.find('</section>', idx_p) + len('</section>')
        html = html[:s_start] + html[s_end:]
        print("5. Successfully removed 'AI 3D Studio & CorelDraw Pattern Engine' section via index fallback!")
    else:
        print("WARNING: Could not find 'AI 3D Studio & CorelDraw Pattern Engine' section!")

# Save to public/index.html and code.html
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Final file length: {len(html)}")
print("Saved clean updates to public/index.html and code.html!")
