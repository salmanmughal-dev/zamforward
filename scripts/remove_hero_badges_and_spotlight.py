import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find the exact block around aspect-[4/5]
target_block = """            <div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="/images/home-page.jpg"/>
              
              <!-- Floating Top Tag -->
              <div class="absolute top-4 left-4 z-10">
                <span class="px-3 py-1 rounded-full bg-[#111417]/85 backdrop-blur-md text-[#F4F1EA] font-mono text-[11px] uppercase font-bold tracking-wider flex items-center gap-2 shadow-sm">
                  <span class="w-2 h-2 rounded-full bg-[#088395] animate-ping"></span>
                  <span>Batch 43 Production Active</span>
                </span>
              </div>

              <!-- Top-Right Spec Badge -->
              <div class="absolute top-4 right-4 z-10">
                <span class="px-2.5 py-1 rounded bg-[#FFFFFF]/90 backdrop-blur-md text-[#111417] font-mono text-[11px] font-bold uppercase shadow-sm border border-[#DFD9CC]">
                  6-Needle Flatlock
                </span>
              </div>
            </div>

            <!-- Inset Metadata Bar (No text over image) -->
            <div class="p-5 bg-[#FFFFFF] border-t border-[#DFD9CC] flex items-center justify-between gap-4">
              <div>
                <span class="font-mono text-[10px] uppercase tracking-wider font-bold text-[#088395]">Atelier Spotlight</span>
                <h4 class="font-headline-sm text-base text-[#111417] font-bold uppercase">Apex Pro Sublimation Kit</h4>
                <p class="font-body-sm text-xs text-[#6B675E]">450 GSM Poly-Spandex • Anti-slip silicone waist</p>
              </div>
              <button onclick="openAiStudioModal()" class="px-4 py-2 rounded-lg bg-[#111417] text-[#F4F1EA] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#088395] transition-colors whitespace-nowrap flex items-center gap-1">
                <span>Configure in 3D</span>
                <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
              </button>
            </div>"""

replacement_block = """            <div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="/images/home-page.jpg"/>
            </div>"""

if target_block in html:
    html = html.replace(target_block, replacement_block)
    print("Exact target block found and replaced successfully!")
else:
    # Use index find
    start_tag = '<!-- Floating Top Tag -->'
    end_tag = '</button>\n            </div>'
    p1 = html.find(start_tag)
    p2 = html.find(end_tag, p1)
    if p1 != -1 and p2 != -1:
        p2 += len(end_tag)
        # remove from p1 to p2, but keep closing of aspect-[4/5]
        # let's inspect
        print("Found via indices:", p1, p2)
        before = html[:p1].rstrip() + '\n            </div>'
        after = html[p2:]
        html = before + after
        print("Replaced via index locator!")
    else:
        print("Failed to locate target block!")

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved public/index.html and code.html!")
