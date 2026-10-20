import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def integrate_graphics(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"\n--- Integrating Graphics into {filepath} (len: {len(html)}) ---")

    # 1. Add graphics.css and wordmark fonts to <head>
    head_marker = '</head>'
    head_addition = """  <!-- ZamForward Graphics Library (163 Vector Symbols, Belts & Ranks) -->
  <link rel="stylesheet" href="/graphics/graphics.css">
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Black+Ops+One&family=Oswald:wght@700&family=Permanent+Marker&family=Russo+One&display=swap" rel="stylesheet">
"""
    if '/graphics/graphics.css' not in html:
        idx_head = html.find(head_marker)
        html = html[:idx_head] + head_addition + html[idx_head:]
        print("1. Injected graphics.css and fonts into <head>")
    else:
        print("1. graphics.css already in <head>")

    # 2. Add graphics-data.js and graphics.js scripts
    script_marker = '<!-- ZamForward Graphics Scripts -->'
    if '/graphics/graphics-data.js' not in html:
        # Find where studio script starts
        s_pos = html.find('ZAMFORWARD AI 3D RASHGUARD & FIGHTWEAR STUDIO ENGINE (v2.0)')
        if s_pos != -1:
            s_tag = html.rfind('<script>', 0, s_pos)
            script_tags = """<!-- ZamForward Graphics Data & Library -->
<script src="/graphics/graphics-data.js"></script>
<script src="/graphics/graphics.js"></script>
"""
            html = html[:s_tag] + script_tags + html[s_tag:]
            print("2. Injected graphics-data.js and graphics.js before studio script")
        else:
            print("Warning: Could not find studio script marker for script injection!")

    # 3. Update #tabPanel_cliparts in #aiStudioModal
    old_panel_cliparts = r'<div id="tabPanel_cliparts" class="space-y-3 hidden">.*?</div>\s*</div>\s*<!-- Right Dock Footer'
    new_panel_cliparts = """<div id="tabPanel_cliparts" class="hidden flex-1 flex flex-col h-full overflow-hidden p-0">
          <div class="px-3 py-2 bg-slate-100 border-b border-slate-200 flex items-center justify-between">
            <span class="font-headline-sm text-xs uppercase font-bold text-[#111417] flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px] text-[#088395]">military_tech</span>
              <span>163 Combat &amp; Belt Rank Graphics</span>
            </span>
            <span class="text-[10px] font-mono text-[#088395] font-bold">1-Tap Inject</span>
          </div>
          <div id="zgStudioLibrary" class="w-full flex-1" style="height: 510px; max-height: 58vh;"></div>
        </div>

      </div>

      <!-- Right Dock Footer"""

    m_clip = re.search(old_panel_cliparts, html, re.DOTALL)
    if m_clip:
        html = html[:m_clip.start()] + new_panel_cliparts + html[m_clip.end():]
        print("3. Updated #tabPanel_cliparts to host #zgStudioLibrary")
    else:
        # Check if already updated
        if 'zgStudioLibrary' in html:
            print("3. #zgStudioLibrary already present in tabPanel_cliparts")
        else:
            print("Warning: Could not match #tabPanel_cliparts pattern!")

    # 4. Update Workflow Section with Interactive Ranks & Graphics Showcase
    workflow_marker = '</section>\n\n    <!-- 5. FOOTER'
    if 'id="workflowGraphicsPreview"' not in html:
        # Find closing of workflow section
        wf_pos = html.find('id="workflow"')
        if wf_pos != -1:
            wf_end = html.find('</section>', wf_pos)
            # Find the inner container closing inside workflow section
            last_inner_div = html.rfind('</div>', wf_pos, wf_end)
            
            workflow_showcase = """
        <!-- Ranks & Vector Graphics Library Showcase (Workflow Design Step) -->
        <div class="mt-10 pt-8 border-t border-[#DFD9CC]">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
            <div>
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white text-[#088395] font-mono text-[11px] uppercase font-bold tracking-wider border border-[#DFD9CC] mb-2 shadow-sm">
                <span class="w-2 h-2 rounded-full bg-[#088395] animate-pulse"></span>
                <span>163 Combat &amp; Rank Vectors (Included Free)</span>
              </div>
              <h3 class="font-headline-sm text-xl sm:text-2xl text-[#111417] font-bold uppercase">Official BJJ Belt Ranks &amp; Combat Symbols</h3>
              <p class="font-body-sm text-xs sm:text-sm text-[#6B675E] max-w-2xl mt-1">
                IBJJF tournament rank bars, degree stripes (1–4), warrior mascots, striking emblems, and national flags. Click any symbol to launch and inject it directly into your 3D design.
              </p>
            </div>
            <div class="flex items-center gap-2.5">
              <button onclick="openAiStudioWithTab('cliparts')" class="px-5 py-2.5 rounded-xl bg-[#088395] text-white font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#066c7b] transition-all shadow-md flex items-center gap-2 whitespace-nowrap">
                <span class="material-symbols-outlined text-[18px]">military_tech</span>
                <span>Browse All 163 in 3D</span>
              </button>
            </div>
          </div>

          <!-- Featured Rank & Combat Graphics Showcase Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-3" id="workflowGraphicsPreview">
            <!-- 1. White Belt -->
            <button onclick="openAiStudioWithGraphic('ranks-white-belt')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="w-full h-3 bg-white border border-slate-400 rounded-sm shadow-inner relative flex items-center justify-end pr-1"><div class="w-3 h-full bg-black"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">White Belt</span>
            </button>

            <!-- 2. Blue Belt -->
            <button onclick="openAiStudioWithGraphic('ranks-blue-belt')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="w-full h-3 bg-blue-600 rounded-sm shadow-inner relative flex items-center justify-end pr-1"><div class="w-3 h-full bg-black"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Blue Belt</span>
            </button>

            <!-- 3. Purple Belt -->
            <button onclick="openAiStudioWithGraphic('ranks-purple-belt')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="w-full h-3 bg-purple-700 rounded-sm shadow-inner relative flex items-center justify-end pr-1"><div class="w-3 h-full bg-black"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Purple Belt</span>
            </button>

            <!-- 4. Brown Belt -->
            <button onclick="openAiStudioWithGraphic('ranks-brown-belt')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="w-full h-3 bg-amber-900 rounded-sm shadow-inner relative flex items-center justify-end pr-1"><div class="w-3 h-full bg-black"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Brown Belt</span>
            </button>

            <!-- 5. Black Belt -->
            <button onclick="openAiStudioWithGraphic('ranks-black-belt-rank')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="w-full h-3 bg-black rounded-sm shadow-inner relative flex items-center justify-end pr-1"><div class="w-3.5 h-full bg-red-600"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Black Belt</span>
            </button>

            <!-- 6. Degree Stripes 4 -->
            <button onclick="openAiStudioWithGraphic('ranks-4-degree-stripes')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1">
                <div class="flex gap-1 items-center justify-center bg-black px-2 py-1.5 rounded"><div class="w-1.5 h-4 bg-white"></div><div class="w-1.5 h-4 bg-white"></div><div class="w-1.5 h-4 bg-white"></div><div class="w-1.5 h-4 bg-white"></div></div>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">4 Degrees</span>
            </button>

            <!-- 7. Spartan Warrior -->
            <button onclick="openAiStudioWithGraphic('warrior-spartan')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1 text-[#088395]">
                <span class="material-symbols-outlined text-[32px]">shield</span>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Spartan Helmet</span>
            </button>

            <!-- 8. Boxing Gloves -->
            <button onclick="openAiStudioWithGraphic('combat-boxing-glove')" class="p-3 bg-white hover:bg-slate-50 border border-[#DFD9CC] hover:border-[#088395] rounded-xl flex flex-col items-center justify-between gap-2 shadow-sm hover:shadow transition-all group text-left">
              <div class="w-full h-12 flex items-center justify-center p-1 text-[#C9A86A]">
                <span class="material-symbols-outlined text-[32px]">sports_mma</span>
              </div>
              <span class="text-[11px] font-bold text-[#111417] text-center w-full truncate">Combat Gloves</span>
            </button>
          </div>
        </div>
"""
            html = html[:last_inner_div] + workflow_showcase + '\n      ' + html[last_inner_div:]
            print("4. Added Ranks & Graphics showcase to #workflow section")
    else:
        print("4. Workflow graphics showcase already present")

    # 5. Add Studio Engine helpers for ZamGraphics: addZamGraphicElement, openAiStudioWithTab, openAiStudioWithGraphic
    helper_code = """
/* ---------------- ZamGraphics Library Integration ---------------- */
window._zgStudioMounted = null;

function mountStudioGraphicsLibrary() {
  const mountEl = document.getElementById('zgStudioLibrary');
  if (!mountEl || !window.ZamGraphics) return;
  if (window._zgStudioMounted) return;

  try {
    window._zgStudioMounted = window.ZamGraphics.mount(mountEl, {
      color: studioState.fabricColor || '#C9A86A',
      onAdd(g) {
        addZamGraphicElement(g);
      },
      onUndo() {
        undoStudio();
      }
    });
  } catch(err) {
    console.warn('ZamGraphics mount error:', err);
  }
}

async function addZamGraphicElement(g) {
  saveStudioHistory();
  const isShorts = studioState.garmentType === 'shorts';
  const targetX = isShorts ? 425 : 205;
  const targetY = isShorts ? 260 : 240;

  if (g.type === 'text') {
    const newEl = {
      id: 'zg_' + Date.now(),
      type: 'text',
      name: g.name,
      text: g.text || g.name,
      font: g.font || 'Impact',
      x: targetX,
      y: targetY,
      scale: 1.0,
      rotation: 0,
      color: g.color || '#C9A86A',
      size: 32
    };
    studioState.elements.push(newEl);
    studioState.selectedElementId = newEl.id;
    refreshAllStudioViews();
    return;
  }

  // Vector icon or rank graphic
  try {
    const wide = g.aspect && g.aspect > 1.6;
    const tall = g.aspect && g.aspect < 0.6;
    const svgDataUrl = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(g.svg);
    const img = new Image();
    img.onload = () => {
      const newEl = {
        id: 'zg_' + Date.now(),
        type: 'logo',
        name: g.name,
        preset: g.id,
        zgId: g.id,
        imageObj: img,
        svg: g.svg,
        x: targetX,
        y: targetY,
        scale: wide ? 1.4 : (tall ? 1.2 : 1.0),
        aspect: g.aspect || 1,
        rotation: 0,
        color: g.color || '#C9A86A'
      };
      studioState.elements.push(newEl);
      studioState.selectedElementId = newEl.id;
      refreshAllStudioViews();
    };
    img.src = svgDataUrl;
  } catch(e) {
    console.error('Error creating graphic element:', e);
  }
}

function openAiStudioWithTab(tab) {
  openAiStudioModal();
  setTimeout(() => {
    setStudioTab(tab);
  }, 220);
}

function openAiStudioWithGraphic(graphicId) {
  openAiStudioModal();
  setTimeout(() => {
    setStudioTab('cliparts');
    if (window.ZamGraphics) {
      const item = window.ZamGraphics.get(graphicId);
      if (item) {
        const svgStr = window.ZamGraphics.svg(graphicId, { color: '#C9A86A', size: 512 });
        addZamGraphicElement({
          id: item.id,
          name: item.name,
          category: item.cat,
          type: item.cat === 'words' ? 'text' : 'icon',
          svg: svgStr,
          color: '#C9A86A',
          aspect: item.aspect || 1
        });
      }
    }
  }, 250);
}
"""

    if 'addZamGraphicElement' not in html:
        # Inject right after function setStudioTab
        tab_fn_pos = html.find('function setStudioTab(tabName) {')
        if tab_fn_pos != -1:
            # Modify setStudioTab to call mountStudioGraphicsLibrary
            old_set_tab = """function setStudioTab(tabName) {
  ['colors', 'layers', 'text', 'uploads', 'cliparts'].forEach(t => {
    const btn = document.getElementById(`tabBtn_${t}`);
    const panel = document.getElementById(`tabPanel_${t}`);
    if (btn && panel) {
      if (t === tabName) {
        btn.className = 'py-3 text-center border-b-2 border-[#088395] text-[#111417] bg-white flex flex-col items-center justify-center gap-0.5 transition-all';
        panel.classList.remove('hidden');
      } else {
        btn.className = 'py-3 text-center border-b-2 border-transparent text-[#6B675E] hover:text-[#111417] flex flex-col items-center justify-center gap-0.5 transition-all';
        panel.classList.add('hidden');
      }
    }
  });
}"""
            new_set_tab = """function setStudioTab(tabName) {
  ['colors', 'layers', 'text', 'uploads', 'cliparts'].forEach(t => {
    const btn = document.getElementById(`tabBtn_${t}`);
    const panel = document.getElementById(`tabPanel_${t}`);
    if (btn && panel) {
      if (t === tabName) {
        btn.className = 'py-3 text-center border-b-2 border-[#088395] text-[#111417] bg-white flex flex-col items-center justify-center gap-0.5 transition-all';
        panel.classList.remove('hidden');
      } else {
        btn.className = 'py-3 text-center border-b-2 border-transparent text-[#6B675E] hover:text-[#111417] flex flex-col items-center justify-center gap-0.5 transition-all';
        panel.classList.add('hidden');
      }
    }
  });
  if (tabName === 'cliparts') {
    mountStudioGraphicsLibrary();
  }
}"""
            html = html.replace(old_set_tab, new_set_tab + '\n' + helper_code)
            print("5. Hooked mountStudioGraphicsLibrary into setStudioTab and injected helpers")

    # 6. Update renderVectorGraphic to handle aspect ratios gracefully
    old_rvg = """  if (el.imageObj) {
    try { ctx.drawImage(el.imageObj, -38, -38, 76, 76); } catch (e) {}
    return;
  }"""

    new_rvg = """  if (el.imageObj) {
    try {
      const asp = el.aspect || 1;
      let w = 76, h = 76;
      if (asp > 1.2) {
        w = Math.min(76 * asp, 150);
        h = w / asp;
      } else if (asp < 0.8) {
        h = Math.min(76 / asp, 150);
        w = h * asp;
      }
      ctx.drawImage(el.imageObj, -w / 2, -h / 2, w, h);
    } catch (e) {}
    return;
  }"""

    if old_rvg in html:
        html = html.replace(old_rvg, new_rvg)
        print("6. Enhanced renderVectorGraphic with aspect-ratio scaling")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Finished {filepath} (new len: {len(html)})\n")

integrate_graphics('code.html')
integrate_graphics('public/index.html')
print("All files updated successfully!")
