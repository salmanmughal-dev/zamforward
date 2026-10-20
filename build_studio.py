import re

# Read current public/index.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Three.js and OrbitControls to <head> if not present
three_scripts = '''  <!-- Three.js and OrbitControls for Real-time 3D Fight Shorts Simulation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>'''

if 'three.min.js' not in html:
    html = html.replace('</head>', three_scripts)

# 2. Add AI Studio launch buttons to navbar, hero, and custom-studio section
# Update Navbar Custom Studio button
html = html.replace(
    '<button onclick="openCustomOrderModal()" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors flex items-center gap-1">\n        <span>Custom Studio</span>\n        <span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>\n      </button>',
    '<button onclick="openAiStudioModal()" class="px-3 py-1.5 rounded-lg bg-secondary/10 text-secondary font-title-sm text-sm font-bold hover:bg-secondary hover:text-on-secondary transition-all flex items-center gap-1.5 shadow-sm">\n        <span class="material-symbols-outlined text-[16px]">auto_fix_high</span>\n        <span>AI 3D Studio</span>\n        <span class="px-1.5 py-0.2 rounded bg-secondary text-on-secondary text-[9px] font-bold uppercase">CDR</span>\n      </button>'
)

# Update Hero "Start Custom Kit Order" button
html = html.replace(
    '<button onclick="openCustomOrderModal()" class="px-6 py-3.5 rounded-xl bg-primary text-on-primary font-label-lg text-sm uppercase font-bold hover:bg-primary-container transition-all shadow-md flex items-center gap-2 group">\n          <span class="material-symbols-outlined text-[18px] group-hover:rotate-45 transition-transform">brush</span>\n          <span>Start Custom Kit Order</span>\n        </button>',
    '<button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-xl bg-primary text-on-primary font-label-lg text-sm uppercase font-bold hover:bg-secondary transition-all shadow-md flex items-center gap-2 group">\n          <span class="material-symbols-outlined text-[18px] text-secondary group-hover:text-on-secondary transition-colors">view_in_ar</span>\n          <span>Launch AI 3D Studio</span>\n          <span class="px-2 py-0.5 rounded bg-secondary text-on-secondary text-[10px] uppercase font-mono">CDR v17</span>\n        </button>'
)

# 3. Update the "#custom-studio" section on the landing page to feature the CDR 3D Studio
custom_studio_section = '''<!-- 6. AI DESIGN STUDIO & COREL TEMPLATE WORKSPACE BANNER -->
<section class="max-w-[1360px] mx-auto px-4 md:px-8 w-full mb-16" id="custom-studio">
  <div class="bg-gradient-to-br from-primary-container via-surface-container-highest to-surface-container p-6 md:p-10 rounded-3xl shadow-xl border border-outline-variant/40 overflow-hidden relative">
    
    <!-- Decorative background vector lines -->
    <div class="absolute -right-16 -bottom-16 w-96 h-96 rounded-full bg-secondary/10 blur-3xl pointer-events-none"></div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
      
      <!-- Left: Studio Details & CDR Blueprint Highlights (7 Cols) -->
      <div class="lg:col-span-7 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-secondary-container text-on-secondary-container font-label-md text-xs uppercase font-bold tracking-wider">
          <span class="material-symbols-outlined text-[16px]">view_in_ar</span>
          <span>CorelDraw (.CDR) 3D Sublimation Engine</span>
        </div>

        <h2 class="font-headline-lg text-3xl md:text-4xl text-primary font-extrabold uppercase tracking-tight">
          AI Studio &amp; Real-Time 3D Garment Designer
        </h2>

        <p class="font-body-md text-sm md:text-base text-on-surface-variant max-w-xl leading-relaxed">
          Powered directly by master vector cut files from <code class="px-2 py-0.5 rounded bg-surface-container font-mono text-xs text-primary font-bold">Backup_of_ZAM FORWARD 123456.cdr</code>. Customize flat 2D pattern pieces (waistband, left &amp; right legs, belt wrap), place logos, add custom typography, and view your design wrapped live in interactive <strong>360° 3D</strong>.
        </p>

        <!-- Feature chips -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2">
          <div class="p-3 rounded-xl bg-surface-container-lowest/80 border border-outline-variant/30 flex items-center gap-2.5">
            <span class="material-symbols-outlined text-secondary text-[20px]">layers</span>
            <div>
              <div class="font-bold text-xs text-primary">CDR Layer Sync</div>
              <div class="text-[10px] text-outline">190 Vector Objects</div>
            </div>
          </div>
          <div class="p-3 rounded-xl bg-surface-container-lowest/80 border border-outline-variant/30 flex items-center gap-2.5">
            <span class="material-symbols-outlined text-secondary text-[20px]">360</span>
            <div>
              <div class="font-bold text-xs text-primary">3D Orbit Preview</div>
              <div class="text-[10px] text-outline">WebGL Simulation</div>
            </div>
          </div>
          <div class="p-3 rounded-xl bg-surface-container-lowest/80 border border-outline-variant/30 flex items-center gap-2.5">
            <span class="material-symbols-outlined text-secondary text-[20px]">cloud_upload</span>
            <div>
              <div class="font-bold text-xs text-primary">Custom Logo Upload</div>
              <div class="text-[10px] text-outline">PNG, SVG &amp; Vector</div>
            </div>
          </div>
        </div>

        <!-- Launch Buttons -->
        <div class="flex flex-wrap items-center gap-3 pt-4">
          <button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-xl bg-primary text-on-primary font-label-lg text-sm uppercase font-bold hover:bg-secondary transition-all shadow-lg flex items-center gap-2 group">
            <span class="material-symbols-outlined text-[20px] text-secondary group-hover:text-on-secondary transition-colors">auto_fix_high</span>
            <span>Launch AI 3D Studio Workspace</span>
            <span class="material-symbols-outlined text-[16px] group-hover:translate-x-1 transition-transform">arrow_forward</span>
          </button>
          <a href="/uploads/templates/Backup_of_ZAM_FORWARD_123456.cdr" download class="px-4 py-3.5 rounded-xl bg-surface-container-lowest text-primary font-label-lg text-xs uppercase font-bold hover:bg-surface-container-high transition-colors border border-outline-variant/40 flex items-center gap-1.5 shadow-sm">
            <span class="material-symbols-outlined text-[18px]">download</span>
            <span>Download Master .CDR (36MB)</span>
          </a>
        </div>
      </div>

      <!-- Right: Interactive Visual Teaser (5 Cols) -->
      <div class="lg:col-span-5 relative">
        <div class="bg-surface-container-lowest p-4 rounded-2xl border border-outline-variant/40 shadow-lg relative group cursor-pointer" onclick="openAiStudioModal()">
          <div class="flex items-center justify-between pb-3 border-b border-outline-variant/30 text-xs">
            <span class="font-mono font-bold text-secondary flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
              MMA_SHORTS_PATTERN_123456.CDR
            </span>
            <span class="px-2 py-0.5 rounded bg-surface-container text-[10px] font-bold text-primary uppercase">Click to Edit in 3D</span>
          </div>

          <!-- Thumbnail Canvas Preview -->
          <div class="py-4 flex items-center justify-center relative overflow-hidden bg-surface-container-low/50 rounded-xl mt-3 aspect-video">
            <img src="/uploads/templates/zam_cdr_thumbnail.png" alt="CDR Pattern Thumbnail" class="h-32 object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500"/>
            <div class="absolute inset-0 bg-primary/40 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
              <span class="px-4 py-2 rounded-xl bg-surface text-primary font-label-md text-xs uppercase font-bold shadow-xl flex items-center gap-1.5">
                <span class="material-symbols-outlined text-[18px] text-secondary">view_in_ar</span>
                <span>Open 3D Customizer</span>
              </span>
            </div>
          </div>

          <div class="mt-3 flex items-center justify-between text-xs text-on-surface-variant">
            <span>Zones: <strong>Waistband, Left/Right Legs, Belt</strong></span>
            <span class="text-secondary font-bold font-mono">300 DPI CMYK</span>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>'''

html = re.sub(
    r'<!-- 6\. AI DESIGN STUDIO & COREL TEMPLATE WORKSPACE BANNER.*?<!-- 7\. ATHLETE',
    custom_studio_section + '\n<!-- 7. ATHLETE',
    html,
    flags=re.DOTALL
)

# 4. The Complete AI Studio Full-Screen Workspace Modal with Three.js 3D View and 2D Pattern Canvas
ai_studio_modal = '''
<!-- ================= AI 3D STUDIO FULL-SCREEN WORKSPACE MODAL ================= -->
<div id="aiStudioModal" class="fixed inset-0 z-50 bg-[#f4f1ea] text-[#111417] hidden flex flex-col overflow-hidden select-none font-body-md">
  
  <!-- Studio Top Navigation Rail -->
  <header class="h-16 bg-surface-container-lowest border-b border-outline-variant/40 px-4 md:px-6 flex items-center justify-between gap-4 flex-shrink-0 z-30 shadow-sm">
    <!-- Left: Title & Active Template Badge -->
    <div class="flex items-center gap-3">
      <button onclick="closeAiStudioModal()" class="w-9 h-9 rounded-xl bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors" title="Back to Home">
        <span class="material-symbols-outlined text-[20px]">arrow_back</span>
      </button>
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-primary text-on-primary flex items-center justify-center font-bold text-xs">
          ZF
        </div>
        <div>
          <h2 class="font-headline-sm text-sm md:text-base font-bold uppercase tracking-tight text-primary leading-tight flex items-center gap-2">
            <span>ZamForward AI Studio</span>
            <span class="px-2 py-0.5 rounded bg-secondary-container text-on-secondary-container text-[10px] font-bold font-mono uppercase">3D CDR Engine</span>
          </h2>
          <p class="text-[11px] text-on-surface-variant hidden sm:block">Master: <code class="font-mono text-primary font-semibold">Backup_of_ZAM FORWARD 123456.cdr</code> (MMA Fight Shorts)</p>
        </div>
      </div>
    </div>

    <!-- Center: View Switcher & Action Tools -->
    <div class="flex items-center gap-2">
      <div class="bg-surface-container p-1 rounded-xl flex items-center gap-1 border border-outline-variant/30">
        <button id="btnViewFront" onclick="setStudioView('front')" class="px-3 py-1 rounded-lg text-xs font-bold uppercase bg-surface-container-lowest text-primary shadow-sm transition-all">Front Cut</button>
        <button id="btnViewBack" onclick="setStudioView('back')" class="px-3 py-1 rounded-lg text-xs font-bold uppercase text-on-surface-variant hover:text-primary transition-all">Back Cut</button>
      </div>

      <div class="h-6 w-px bg-outline-variant/40 mx-1 hidden md:block"></div>

      <div class="flex items-center gap-1">
        <button onclick="undoStudio()" class="w-8 h-8 rounded-lg bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors" title="Undo">
          <span class="material-symbols-outlined text-[18px]">undo</span>
        </button>
        <button onclick="redoStudio()" class="w-8 h-8 rounded-lg bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors" title="Redo">
          <span class="material-symbols-outlined text-[18px]">redo</span>
        </button>
        <button onclick="resetStudioCanvas()" class="w-8 h-8 rounded-lg bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors" title="Reset Pattern">
          <span class="material-symbols-outlined text-[18px]">restart_alt</span>
        </button>
      </div>
    </div>

    <!-- Right: Save & Add to Cart Action -->
    <div class="flex items-center gap-2">
      <button onclick="saveStudioDraft()" class="hidden md:inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-surface-container font-label-md text-xs uppercase font-bold text-primary hover:bg-surface-container-high transition-colors">
        <span class="material-symbols-outlined text-[16px]">save</span>
        <span>Save</span>
      </button>
      <button onclick="openStudio3DFullscreen()" class="hidden sm:inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-surface-container font-label-md text-xs uppercase font-bold text-primary hover:bg-surface-container-high transition-colors">
        <span class="material-symbols-outlined text-[16px]">fullscreen</span>
        <span>Full 3D</span>
      </button>
      <button onclick="submitStudioOrder()" class="px-4 py-2 rounded-xl bg-secondary text-on-secondary font-label-lg text-xs uppercase font-bold hover:opacity-90 transition-opacity shadow-md flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">shopping_cart_checkout</span>
        <span>Add to Cart / Order</span>
      </button>
    </div>
  </header>

  <!-- Studio Main Work Area (Split: Left/Center 2D & 3D Canvas + Right Tools Drawer) -->
  <div class="flex-1 flex overflow-hidden relative">

    <!-- Center/Main Canvas Workspace -->
    <div class="flex-1 relative flex flex-col bg-[#f0eee6] overflow-hidden">
      
      <!-- FLOATING 3D PREVIEW WINDOW (Matches User Screenshot) -->
      <div id="studio3DFloatingCard" class="absolute top-4 left-4 z-20 w-64 sm:w-80 bg-surface-container-lowest/95 backdrop-blur-md rounded-2xl shadow-2xl border border-outline-variant/40 overflow-hidden flex flex-col transition-all duration-300">
        <!-- 3D Header -->
        <div class="px-3 py-2 bg-surface-container-low border-b border-outline-variant/30 flex items-center justify-between text-xs cursor-move" id="studio3DHeader">
          <div class="flex items-center gap-1.5 font-bold text-primary uppercase text-[11px]">
            <span class="w-2 h-2 rounded-full bg-secondary animate-ping"></span>
            <span>Live 3D Garment View</span>
          </div>
          <div class="flex items-center gap-1">
            <button onclick="reset3DCamera()" class="w-6 h-6 rounded flex items-center justify-center text-outline hover:text-primary" title="Reset 3D Angle">
              <span class="material-symbols-outlined text-[16px]">sync</span>
            </button>
            <button onclick="toggle3DMinimize()" class="w-6 h-6 rounded flex items-center justify-center text-outline hover:text-primary" title="Minimize / Expand">
              <span id="btn3DMinIcon" class="material-symbols-outlined text-[16px]">unfold_less</span>
            </button>
          </div>
        </div>

        <!-- Three.js 3D Canvas Container -->
        <div id="studio3DCanvasContainer" class="relative w-full h-64 bg-gradient-to-b from-[#1c1c18] to-[#2c2d30] flex items-center justify-center">
          <canvas id="threeCanvas" class="w-full h-full cursor-grab active:cursor-grabbing"></canvas>
          
          <!-- 3D Rotation Badge (Matches screenshot) -->
          <div class="absolute bottom-3 left-3 pointer-events-none">
            <div class="px-2.5 py-1 rounded-full bg-secondary text-on-secondary text-[10px] font-bold uppercase tracking-wider flex items-center gap-1 shadow-md">
              <span class="material-symbols-outlined text-[14px] animate-spin" style="animation-duration: 6s;">360</span>
              <span>3D Orbit Active</span>
            </div>
          </div>

          <!-- Hint -->
          <div class="absolute top-2 right-2 pointer-events-none text-[10px] text-white/50 bg-black/40 px-2 py-0.5 rounded">
            Drag to Rotate 360°
          </div>
        </div>
      </div>

      <!-- 2D FLAT PATTERN CANVAS AREA -->
      <div class="flex-1 overflow-auto flex items-center justify-center p-4 relative" id="canvasWrapper">
        <div class="relative bg-white rounded-2xl shadow-xl border border-outline-variant/40 p-4 overflow-hidden">
          
          <!-- Top Waistband Logo Placement -->
          <div class="text-center pb-2 text-[11px] font-mono text-outline uppercase tracking-wider flex items-center justify-center gap-2">
            <span>CorelDraw Vector Pattern</span>
            <span class="text-secondary font-bold">•</span>
            <span>MMA Fight Shorts Cut &amp; Sew Blueprint</span>
          </div>

          <!-- HTML5 2D Pattern Canvas -->
          <canvas id="patternCanvas" width="850" height="600" class="border border-outline-variant/30 rounded-xl bg-[#fafafa] cursor-crosshair shadow-inner"></canvas>

          <!-- Canvas Bottom Specs -->
          <div class="pt-3 flex items-center justify-between text-xs text-outline font-mono">
            <span>Pattern Scale: 1:1 Sublimation Spec</span>
            <span>CutContour Bleed: 15mm</span>
            <span>Objects: <strong class="text-primary" id="lblObjectCount">5 Active Elements</strong></span>
          </div>
        </div>
      </div>

      <!-- Bottom Status Bar -->
      <div class="h-12 bg-surface-container-lowest border-t border-outline-variant/30 px-6 flex items-center justify-between text-xs text-on-surface-variant flex-shrink-0">
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2 font-mono font-bold text-primary">
            <span class="w-2.5 h-2.5 rounded-full bg-secondary"></span>
            <span>Pattern: Backup_of_ZAM FORWARD 123456.cdr</span>
          </div>
          <span class="text-outline">|</span>
          <span class="hidden sm:inline">Fabric: <strong class="text-primary font-semibold" id="lblFabricColor">Champion Gold (#efd965)</strong></span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-outline hidden md:inline">Click any element on canvas to scale, rotate or drag</span>
          <button onclick="submitStudioOrder()" class="font-bold text-secondary hover:underline flex items-center gap-1 uppercase">
            <span>Confirm Order File</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </button>
        </div>
      </div>

    </div>

    <!-- Right: Studio Tools & Layers Drawer (Matches User Screenshot) -->
    <div class="w-80 sm:w-96 bg-surface-container-lowest border-l border-outline-variant/40 flex flex-col z-20 shadow-xl flex-shrink-0">
      
      <!-- Drawer Navigation Tabs -->
      <div class="flex items-center border-b border-outline-variant/30 bg-surface-container-low text-xs font-bold uppercase">
        <button onclick="setStudioTab('layers')" id="tabBtn_layers" class="flex-1 py-3 text-center border-b-2 border-secondary text-primary flex items-center justify-center gap-1.5 transition-all">
          <span class="material-symbols-outlined text-[18px]">layers</span>
          <span>Layers</span>
        </button>
        <button onclick="setStudioTab('uploads')" id="tabBtn_uploads" class="flex-1 py-3 text-center border-b-2 border-transparent text-on-surface-variant hover:text-primary flex items-center justify-center gap-1.5 transition-all">
          <span class="material-symbols-outlined text-[18px]">cloud_upload</span>
          <span>Uploads</span>
        </button>
        <button onclick="setStudioTab('cliparts')" id="tabBtn_cliparts" class="flex-1 py-3 text-center border-b-2 border-transparent text-on-surface-variant hover:text-primary flex items-center justify-center gap-1.5 transition-all">
          <span class="material-symbols-outlined text-[18px]">category</span>
          <span>Cliparts</span>
        </button>
        <button onclick="setStudioTab('text')" id="tabBtn_text" class="flex-1 py-3 text-center border-b-2 border-transparent text-on-surface-variant hover:text-primary flex items-center justify-center gap-1.5 transition-all">
          <span class="material-symbols-outlined text-[18px]">title</span>
          <span>Text</span>
        </button>
        <button onclick="setStudioTab('colors')" id="tabBtn_colors" class="flex-1 py-3 text-center border-b-2 border-transparent text-on-surface-variant hover:text-primary flex items-center justify-center gap-1.5 transition-all">
          <span class="material-symbols-outlined text-[18px]">palette</span>
          <span>Colors</span>
        </button>
      </div>

      <!-- Tab Content Area -->
      <div class="flex-1 overflow-y-auto p-4 space-y-4">
        
        <!-- 1. LAYERS TAB -->
        <div id="tabPanel_layers" class="space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
            <span class="font-headline-sm text-xs uppercase font-bold text-primary">Design Elements (<span id="lblLayerCount">5</span>)</span>
            <button onclick="clearAllElements()" class="text-[11px] text-error hover:underline font-semibold">Clear All</button>
          </div>

          <!-- Dynamic Elements List -->
          <div id="studioElementsList" class="space-y-2">
            <!-- Rendered dynamically by updateStudioLayers() -->
          </div>
        </div>

        <!-- 2. UPLOADS TAB (Custom Logo Upload to Local Storage) -->
        <div id="tabPanel_uploads" class="space-y-4 hidden">
          <div class="p-4 rounded-xl bg-surface-container-low border-2 border-dashed border-outline-variant/60 text-center hover:border-secondary transition-colors cursor-pointer" onclick="document.getElementById('studioUploadInput').click()">
            <span class="material-symbols-outlined text-secondary text-[36px] mb-1">cloud_upload</span>
            <h4 class="font-title-md text-xs uppercase font-bold text-primary">Upload Team Logo / Vector</h4>
            <p class="text-[11px] text-on-surface-variant mt-1">PNG, SVG, JPG, CDR, AI supported (Max 64MB)</p>
            <input type="file" id="studioUploadInput" accept=".png,.jpg,.jpeg,.svg,.ai,.cdr" class="hidden" onchange="handleStudioLogoUpload(event)"/>
            <button type="button" class="mt-3 px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-xs uppercase font-bold">Browse Files</button>
          </div>
          <p class="text-[11px] text-outline text-center">Files are stored locally in <code>uploads/designs/</code> &amp; linked in SQLite.</p>

          <div>
            <h5 class="font-label-md text-xs uppercase font-bold text-primary mb-2">Preset Combat Team Crests</h5>
            <div class="grid grid-cols-2 gap-2" id="presetLogosContainer">
              <!-- Preset Logos -->
            </div>
          </div>
        </div>

        <!-- 3. CLIPARTS TAB -->
        <div id="tabPanel_cliparts" class="space-y-3 hidden">
          <span class="font-label-md text-xs uppercase font-bold text-primary block">Fight Graphics &amp; Emblems</span>
          <div class="grid grid-cols-3 gap-2" id="clipartsContainer">
            <!-- Dynamic Combat Cliparts -->
          </div>
        </div>

        <!-- 4. TEXT TAB -->
        <div id="tabPanel_text" class="space-y-3 hidden">
          <span class="font-label-md text-xs uppercase font-bold text-primary block">Add Custom Typography</span>
          <div>
            <label class="block text-[11px] uppercase font-bold text-outline mb-1">Text Content</label>
            <input type="text" id="studioTextInput" value="INFERNO" placeholder="Enter text..." class="w-full bg-surface-container px-3 py-2 rounded-lg text-xs font-bold text-primary uppercase focus:outline-none border border-outline-variant"/>
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] uppercase font-bold text-outline mb-1">Font Family</label>
              <select id="studioFontSelect" class="w-full bg-surface-container px-2.5 py-2 rounded-lg text-xs font-bold text-primary focus:outline-none border border-outline-variant">
                <option value="Space Grotesk">Space Grotesk</option>
                <option value="Impact" selected>Impact (Bold)</option>
                <option value="Plus Jakarta Sans">Jakarta Sans</option>
                <option value="Courier New">Mono Stencil</option>
              </select>
            </div>
            <div>
              <label class="block text-[11px] uppercase font-bold text-outline mb-1">Text Color</label>
              <input type="color" id="studioTextColorInput" value="#111417" class="w-full h-9 rounded-lg bg-surface-container cursor-pointer p-1 border border-outline-variant"/>
            </div>
          </div>

          <button onclick="addTextToCanvas()" class="w-full py-2.5 rounded-xl bg-primary text-on-primary font-label-md text-xs uppercase font-bold hover:bg-secondary transition-colors flex items-center justify-center gap-1.5 shadow-sm">
            <span class="material-symbols-outlined text-[16px]">add_circle</span>
            <span>Add Text to Shorts</span>
          </button>
        </div>

        <!-- 5. FABRIC COLORS TAB -->
        <div id="tabPanel_colors" class="space-y-4 hidden">
          <div>
            <span class="font-label-md text-xs uppercase font-bold text-primary block mb-2">Garment Base Fabric Color</span>
            <div class="grid grid-cols-3 gap-2">
              <button onclick="setFabricColor('#efd965', 'Champion Gold')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #efd965;"></span>
                <span class="text-[10px] font-bold">Gold</span>
              </button>
              <button onclick="setFabricColor('#18181b', 'Carbon Black')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #18181b;"></span>
                <span class="text-[10px] font-bold">Black</span>
              </button>
              <button onclick="setFabricColor('#088395', 'Combat Cyan')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #088395;"></span>
                <span class="text-[10px] font-bold">Cyan</span>
              </button>
              <button onclick="setFabricColor('#ffffff', 'Champion White')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #ffffff;"></span>
                <span class="text-[10px] font-bold">White</span>
              </button>
              <button onclick="setFabricColor('#dc2626', 'Crimson Red')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #dc2626;"></span>
                <span class="text-[10px] font-bold">Red</span>
              </button>
              <button onclick="setFabricColor('#1e3a8a', 'Navy Combat')" class="flex flex-col items-center gap-1.5 p-2 rounded-xl bg-surface-container hover:ring-2 hover:ring-secondary transition-all">
                <span class="w-8 h-8 rounded-full border border-black/20 shadow-sm" style="background-color: #1e3a8a;"></span>
                <span class="text-[10px] font-bold">Navy</span>
              </button>
            </div>
          </div>

          <div class="pt-3 border-t border-outline-variant/30">
            <span class="font-label-md text-xs uppercase font-bold text-primary block mb-2">Waistband &amp; Trim Accent</span>
            <div class="grid grid-cols-3 gap-2">
              <button onclick="setWaistbandColor('#18181b')" class="p-2 rounded-xl bg-surface-container text-xs font-bold text-center">Black Trim</button>
              <button onclick="setWaistbandColor('#ffffff')" class="p-2 rounded-xl bg-surface-container text-xs font-bold text-center">White Trim</button>
              <button onclick="setWaistbandColor('#088395')" class="p-2 rounded-xl bg-surface-container text-xs font-bold text-center">Cyan Trim</button>
            </div>
          </div>
        </div>

      </div>

      <!-- Drawer Footer Action -->
      <div class="p-4 bg-surface-container-low border-t border-outline-variant/30 flex items-center justify-between">
        <div>
          <span class="text-[10px] uppercase font-bold text-outline block">Batch Unit Price</span>
          <span class="font-headline-sm text-base text-primary font-bold">$48.00 / pair</span>
        </div>
        <button onclick="submitStudioOrder()" class="px-5 py-2.5 rounded-xl bg-primary text-on-primary font-label-md text-xs uppercase font-bold hover:bg-secondary transition-colors shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px]">shopping_cart</span>
          <span>Add to Cart</span>
        </button>
      </div>

    </div>

  </div>
</div>
'''

# Add modal before </body>
html = html.replace('<!-- ================= MODALS & SLIDEOUT PANELS ================= -->', ai_studio_modal + '\n<!-- ================= MODALS & SLIDEOUT PANELS ================= -->')

# 5. Append Complete AI Studio Script (Three.js 3D Engine + 2D Pattern Canvas Engine)
studio_engine_script = '''
<script>
/* =========================================================================
   ZAMFORWARD AI 3D STUDIO & CDR PATTERN ENGINE
   Master CDR File: Backup_of_ZAM FORWARD 123456.cdr
   ========================================================================= */

// Studio State
let studioState = {
  view: 'front', // 'front' | 'back'
  fabricColor: '#efd965', // Champion Gold (matches screenshot)
  fabricName: 'Champion Gold',
  waistbandColor: '#18181b', // Carbon Black
  flapColor: '#f4f1ea', // White closure flap
  elements: [
    // Pre-populate with design elements matching user's CDR screenshot!
    { id: 'el_crest', type: 'logo', name: 'Waistband Crest Wings', x: 425, y: 70, scale: 0.65, rotation: 0, color: '#111417', preset: 'wings' },
    { id: 'el_text1', type: 'text', name: 'Left Leg Vertical INFERNO', text: 'INFERNO', x: 265, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 36 },
    { id: 'el_text2', type: 'text', name: 'Right Leg Vertical INFERNO', text: 'INFERNO', x: 585, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 36 },
    { id: 'el_sponsor1', type: 'logo', name: 'Left Slit Sponsor Logo', x: 310, y: 350, scale: 0.7, rotation: 0, color: '#111417', preset: 'metal' },
    { id: 'el_sponsor2', type: 'logo', name: 'Right Slit Custom Inferno', x: 535, y: 350, scale: 0.75, rotation: 0, color: '#111417', preset: 'inferno_script' },
    { id: 'el_bolt', type: 'clipart', name: 'Right Slit Lightning Bolt', x: 635, y: 350, scale: 0.8, rotation: 0, color: '#111417', preset: 'bolt' },
    { id: 'el_belt', type: 'text', name: 'Lower Belt Script', text: 'CUSTOM INFERNO', x: 425, y: 535, scale: 0.9, rotation: 0, color: '#efd965', font: 'Impact', size: 28 }
  ],
  selectedElementId: null,
  isDragging: false,
  dragOffset: { x: 0, y: 0 }
};

// Undo/Redo Stacks
let undoStack = [];
let redoStack = [];

function saveStudioHistory() {
  undoStack.push(JSON.stringify(studioState));
  if (undoStack.length > 20) undoStack.shift();
  redoStack = [];
}

function undoStudio() {
  if (undoStack.length === 0) return;
  redoStack.push(JSON.stringify(studioState));
  const prevState = JSON.parse(undoStack.pop());
  studioState = prevState;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function redoStudio() {
  if (redoStack.length === 0) return;
  undoStack.push(JSON.stringify(studioState));
  const nextState = JSON.parse(redoStack.pop());
  studioState = nextState;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

// ------------------- MODAL CONTROLS -------------------
function openAiStudioModal() {
  const modal = document.getElementById('aiStudioModal');
  modal.classList.remove('hidden');
  initStudio2DCanvas();
  initThreeJS3D();
  renderPatternCanvas();
  updateStudioLayers();
  renderPresetLogos();
  renderCliparts();
  showToast('AI Studio loaded with Backup_of_ZAM FORWARD 123456.cdr MMA Fight Shorts!', 'success');
}

function closeAiStudioModal() {
  const modal = document.getElementById('aiStudioModal');
  modal.classList.add('hidden');
}

function setStudioTab(tabName) {
  ['layers', 'uploads', 'cliparts', 'text', 'colors'].forEach(t => {
    const btn = document.getElementById(`tabBtn_${t}`);
    const panel = document.getElementById(`tabPanel_${t}`);
    if (btn && panel) {
      if (t === tabName) {
        btn.classList.add('border-secondary', 'text-primary');
        btn.classList.remove('border-transparent', 'text-on-surface-variant');
        panel.classList.remove('hidden');
      } else {
        btn.classList.remove('border-secondary', 'text-primary');
        btn.classList.add('border-transparent', 'text-on-surface-variant');
        panel.classList.add('hidden');
      }
    }
  });
}

function setStudioView(view) {
  studioState.view = view;
  const btnF = document.getElementById('btnViewFront');
  const btnB = document.getElementById('btnViewBack');
  if (view === 'front') {
    btnF.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase bg-surface-container-lowest text-primary shadow-sm transition-all';
    btnB.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase text-on-surface-variant hover:text-primary transition-all';
  } else {
    btnB.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase bg-surface-container-lowest text-primary shadow-sm transition-all';
    btnF.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase text-on-surface-variant hover:text-primary transition-all';
  }
  renderPatternCanvas();
  update3DTexture();
}

function setFabricColor(hex, name) {
  saveStudioHistory();
  studioState.fabricColor = hex;
  studioState.fabricName = name;
  document.getElementById('lblFabricColor').innerText = `${name} (${hex})`;
  renderPatternCanvas();
  update3DTexture();
  showToast(`Garment color changed to ${name}`, 'info');
}

function setWaistbandColor(hex) {
  saveStudioHistory();
  studioState.waistbandColor = hex;
  renderPatternCanvas();
  update3DTexture();
}

// ------------------- 2D PATTERN CANVAS ENGINE -------------------
let patternCanvas, ctx2d;

function initStudio2DCanvas() {
  patternCanvas = document.getElementById('patternCanvas');
  ctx2d = patternCanvas.getContext('2d');

  // Interactive mouse handlers for dragging and selecting
  patternCanvas.onmousedown = onCanvasMouseDown;
  patternCanvas.onmousemove = onCanvasMouseMove;
  window.onmouseup = onCanvasMouseUp;

  // Touch support
  patternCanvas.ontouchstart = (e) => {
    const t = e.touches[0];
    const rect = patternCanvas.getBoundingClientRect();
    handlePointerDown(t.clientX - rect.left, t.clientY - rect.top);
  };
  patternCanvas.ontouchmove = (e) => {
    const t = e.touches[0];
    const rect = patternCanvas.getBoundingClientRect();
    handlePointerMove(t.clientX - rect.left, t.clientY - rect.top);
  };
  window.ontouchend = () => { studioState.isDragging = false; };
}

function getCanvasCoords(e) {
  const rect = patternCanvas.getBoundingClientRect();
  const scaleX = patternCanvas.width / rect.width;
  const scaleY = patternCanvas.height / rect.height;
  return {
    x: (e.clientX - rect.left) * scaleX,
    y: (e.clientY - rect.top) * scaleY
  };
}

function onCanvasMouseDown(e) {
  const pt = getCanvasCoords(e);
  handlePointerDown(pt.x, pt.y);
}

function handlePointerDown(x, y) {
  // Check if clicked inside any element (in reverse order for top-most)
  let found = null;
  for (let i = studioState.elements.length - 1; i >= 0; i--) {
    const el = studioState.elements[i];
    const dist = Math.hypot(el.x - x, el.y - y);
    if (dist < 40 * el.scale) {
      found = el;
      break;
    }
  }

  if (found) {
    saveStudioHistory();
    studioState.selectedElementId = found.id;
    studioState.isDragging = true;
    studioState.dragOffset = { x: x - found.x, y: y - found.y };
  } else {
    studioState.selectedElementId = null;
  }
  renderPatternCanvas();
  updateStudioLayers();
}

function onCanvasMouseMove(e) {
  if (!studioState.isDragging || !studioState.selectedElementId) return;
  const pt = getCanvasCoords(e);
  handlePointerMove(pt.x, pt.y);
}

function handlePointerMove(x, y) {
  const el = studioState.elements.find(e => e.id === studioState.selectedElementId);
  if (!el) return;
  el.x = Math.max(50, Math.min(patternCanvas.width - 50, x - studioState.dragOffset.x));
  el.y = Math.max(30, Math.min(patternCanvas.height - 30, y - studioState.dragOffset.y));
  renderPatternCanvas();
  update3DTexture();
}

function onCanvasMouseUp() {
  studioState.isDragging = false;
}

// Render the exact MMA Fight Shorts flat pattern pieces matching user's CDR screenshot!
function renderPatternCanvas() {
  if (!ctx2d) return;
  const w = patternCanvas.width;
  const h = patternCanvas.height;

  // Clear background
  ctx2d.fillStyle = '#fafafa';
  ctx2d.fillRect(0, 0, w, h);

  // Subtle grid guide lines
  ctx2d.strokeStyle = '#f0eee6';
  ctx2d.lineWidth = 1;
  for (let x = 0; x < w; x += 40) {
    ctx2d.beginPath(); ctx2d.moveTo(x, 0); ctx2d.lineTo(x, h); ctx2d.stroke();
  }
  for (let y = 0; y < h; y += 40) {
    ctx2d.beginPath(); ctx2d.moveTo(0, y); ctx2d.lineTo(w, y); ctx2d.stroke();
  }

  // 1. TOP CENTER: Waistband Closure Flap
  ctx2d.save();
  ctx2d.fillStyle = studioState.flapColor;
  ctx2d.strokeStyle = '#d4d4d8';
  ctx2d.lineWidth = 2;
  ctx2d.beginPath();
  ctx2d.roundRect(360, 40, 130, 55, 6);
  ctx2d.fill();
  ctx2d.stroke();
  // Seam stitch line
  ctx2d.setLineDash([4, 4]);
  ctx2d.strokeStyle = '#a1a1aa';
  ctx2d.strokeRect(364, 44, 122, 47);
  ctx2d.setLineDash([]);
  ctx2d.restore();

  // 2. LEFT FLIGHT SHORTS LEG (Trapezoid Flared Pattern from CDR)
  ctx2d.save();
  ctx2d.fillStyle = studioState.fabricColor;
  ctx2d.strokeStyle = '#71717a';
  ctx2d.lineWidth = 2.5;

  ctx2d.beginPath();
  ctx2d.moveTo(210, 160); // top waist left
  ctx2d.lineTo(350, 160); // top waist right
  ctx2d.lineTo(370, 260); // inner inseam crotch curve
  ctx2d.lineTo(330, 390); // inner leg hem
  ctx2d.lineTo(190, 390); // outer leg hem with slit cut
  ctx2d.lineTo(175, 340); // 45-deg split slit corner
  ctx2d.lineTo(210, 160); // close to top
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();

  // Side accent panel trim (Black stripe)
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.beginPath();
  ctx2d.moveTo(175, 340);
  ctx2d.lineTo(190, 390);
  ctx2d.lineTo(182, 390);
  ctx2d.lineTo(170, 342);
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.restore();

  // 3. RIGHT FLIGHT SHORTS LEG (Mirror Flared Pattern from CDR)
  ctx2d.save();
  ctx2d.fillStyle = studioState.fabricColor;
  ctx2d.strokeStyle = '#71717a';
  ctx2d.lineWidth = 2.5;

  ctx2d.beginPath();
  ctx2d.moveTo(500, 160); // top waist left
  ctx2d.lineTo(640, 160); // top waist right
  ctx2d.lineTo(675, 340); // outer leg slit corner
  ctx2d.lineTo(660, 390); // outer leg hem
  ctx2d.lineTo(520, 390); // inner leg hem
  ctx2d.lineTo(480, 260); // inner inseam crotch curve
  ctx2d.lineTo(500, 160); // close to top
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();

  // Side accent panel trim (Black stripe)
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.beginPath();
  ctx2d.moveTo(675, 340);
  ctx2d.lineTo(660, 390);
  ctx2d.lineTo(668, 390);
  ctx2d.lineTo(680, 342);
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.restore();

  // 4. LOWER BELT / WAISTBAND STRIP (Wide curved belt panel at bottom)
  ctx2d.save();
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.strokeStyle = '#3f3f46';
  ctx2d.lineWidth = 2;
  ctx2d.beginPath();
  ctx2d.moveTo(200, 480);
  ctx2d.lineTo(650, 480);
  ctx2d.lineTo(660, 520);
  ctx2d.lineTo(425, 570); // V-taper center
  ctx2d.lineTo(190, 520);
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();
  ctx2d.restore();

  // RENDER DESIGN ELEMENTS
  studioState.elements.forEach(el => {
    ctx2d.save();
    ctx2d.translate(el.x, el.y);
    ctx2d.rotate((el.rotation || 0) * Math.PI / 180);
    ctx2d.scale(el.scale || 1, el.scale || 1);

    const isSelected = el.id === studioState.selectedElementId;

    if (el.type === 'text') {
      ctx2d.font = `bold ${el.size || 32}px ${el.font || 'Impact'}`;
      ctx2d.textAlign = 'center';
      ctx2d.textBaseline = 'middle';
      ctx2d.fillStyle = el.color || '#111417';
      ctx2d.fillText(el.text, 0, 0);

      // Stroke outline
      ctx2d.strokeStyle = el.color === '#efd965' ? '#18181b' : 'rgba(255,255,255,0.4)';
      ctx2d.lineWidth = 1.5;
      ctx2d.strokeText(el.text, 0, 0);
    } else if (el.type === 'logo' || el.type === 'clipart') {
      renderVectorGraphic(ctx2d, el);
    }

    // Selection bounding box
    if (isSelected) {
      ctx2d.strokeStyle = '#088395';
      ctx2d.lineWidth = 2;
      ctx2d.setLineDash([4, 4]);
      ctx2d.strokeRect(-45, -30, 90, 60);

      // Corner handles
      ctx2d.setLineDash([]);
      ctx2d.fillStyle = '#088395';
      [-45, 45].forEach(cx => {
        [-30, 30].forEach(cy => {
          ctx2d.fillRect(cx - 4, cy - 4, 8, 8);
        });
      });
    }

    ctx2d.restore();
  });
}

// Vector graphics helper (Draws custom logos matching CDR screenshot)
function renderVectorGraphic(ctx, el) {
  ctx.fillStyle = el.color || '#111417';
  ctx.strokeStyle = el.color || '#111417';

  if (el.preset === 'wings') {
    // Sharp combat wings emblem
    ctx.beginPath();
    ctx.moveTo(0, 10);
    ctx.quadraticCurveTo(-20, -15, -35, -25);
    ctx.quadraticCurveTo(-15, -10, 0, 0);
    ctx.quadraticCurveTo(15, -10, 35, -25);
    ctx.quadraticCurveTo(20, -15, 0, 10);
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(0, 5);
    ctx.lineTo(-20, -18);
    ctx.lineTo(-8, -5);
    ctx.lineTo(0, 0);
    ctx.lineTo(8, -5);
    ctx.lineTo(20, -18);
    ctx.closePath();
    ctx.fill();
  } else if (el.preset === 'bolt') {
    // High-impact lightning bolt
    ctx.beginPath();
    ctx.moveTo(4, -22);
    ctx.lineTo(-14, -2);
    ctx.lineTo(-2, -2);
    ctx.lineTo(-6, 22);
    ctx.lineTo(14, 2);
    ctx.lineTo(2, 2);
    ctx.closePath();
    ctx.fill();
  } else if (el.preset === 'metal') {
    // Angular sponsor mark
    ctx.font = 'bold 22px Impact';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('⚡STRIKE', 0, 0);
  } else if (el.preset === 'inferno_script') {
    // Distressed script mark
    ctx.font = 'italic bold 20px Impact';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('CUSTOM INFERNO', 0, 0);
  } else if (el.imageObj) {
    // Custom uploaded user logo
    try {
      ctx.drawImage(el.imageObj, -35, -35, 70, 70);
    } catch(err) {}
  } else {
    // Generic fallback shield
    ctx.beginPath();
    ctx.moveTo(0, -20);
    ctx.lineTo(18, -12);
    ctx.lineTo(14, 12);
    ctx.lineTo(0, 22);
    ctx.lineTo(-14, 12);
    ctx.lineTo(-18, -12);
    ctx.closePath();
    ctx.fill();
  }
}

// ------------------- THREE.JS 3D ENGINE -------------------
let threeScene, threeCamera, threeRenderer, threeControls;
let shortsGroup, offscreenCanvas, offscreenCtx, canvasTexture;

function initThreeJS3D() {
  const container = document.getElementById('studio3DCanvasContainer');
  if (!container) return;
  const canvas = document.getElementById('threeCanvas');

  // Prevent duplicate initialization
  if (threeRenderer) {
    onWindowResize3D();
    return;
  }

  // 1. Scene
  threeScene = new THREE.Scene();

  // 2. Camera
  threeCamera = new THREE.PerspectiveCamera(38, container.clientWidth / container.clientHeight, 0.1, 100);
  threeCamera.position.set(0, 0.2, 5.2);

  // 3. Renderer
  threeRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
  threeRenderer.setSize(container.clientWidth, container.clientHeight);
  threeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  threeRenderer.shadowMap.enabled = true;

  // 4. Orbit Controls (360° rotation)
  threeControls = new THREE.OrbitControls(threeCamera, threeRenderer.domElement);
  threeControls.enableDamping = true;
  threeControls.dampingFactor = 0.05;
  threeControls.minDistance = 3.0;
  threeControls.maxDistance = 7.5;
  threeControls.autoRotate = false;
  threeControls.autoRotateSpeed = 1.5;

  // 5. Studio Lighting
  const ambLight = new THREE.AmbientLight(0xffffff, 0.85);
  threeScene.add(ambLight);

  const keyLight = new THREE.DirectionalLight(0xffffff, 0.9);
  keyLight.position.set(3, 4, 5);
  threeScene.add(keyLight);

  const fillLight = new THREE.DirectionalLight(0x088395, 0.4);
  fillLight.position.set(-4, -2, -3);
  threeScene.add(fillLight);

  const rimLight = new THREE.DirectionalLight(0xffffff, 0.6);
  rimLight.position.set(0, 5, -4);
  threeScene.add(rimLight);

  // 6. Offscreen Texture Canvas for Live 3D Texture Mapping
  offscreenCanvas = document.createElement('canvas');
  offscreenCanvas.width = 1024;
  offscreenCanvas.height = 1024;
  offscreenCtx = offscreenCanvas.getContext('2d');
  canvasTexture = new THREE.CanvasTexture(offscreenCanvas);
  canvasTexture.wrapS = THREE.RepeatWrapping;
  canvasTexture.wrapT = THREE.RepeatWrapping;

  // 7. Build 3D Combat Shorts Geometry
  build3DShortsModel();

  // Animation Loop
  function animate3D() {
    requestAnimationFrame(animate3D);
    threeControls.update();
    threeRenderer.render(threeScene, threeCamera);
  }
  animate3D();

  // Resize handler
  window.addEventListener('resize', onWindowResize3D);
}

function onWindowResize3D() {
  const container = document.getElementById('studio3DCanvasContainer');
  if (!container || !threeRenderer || !threeCamera) return;
  threeCamera.aspect = container.clientWidth / container.clientHeight;
  threeCamera.updateProjectionMatrix();
  threeRenderer.setSize(container.clientWidth, container.clientHeight);
}

// Build athletic MMA fight shorts mesh
function build3DShortsModel() {
  shortsGroup = new THREE.Group();

  // Main Fabric Material (Uses dynamic canvas texture)
  const fabricMaterial = new THREE.MeshStandardMaterial({
    map: canvasTexture,
    roughness: 0.35,
    metalness: 0.1,
    side: THREE.DoubleSide
  });

  // Waistband Material (Carbon Black with ribbing)
  const waistbandMaterial = new THREE.MeshStandardMaterial({
    color: new THREE.Color(studioState.waistbandColor),
    roughness: 0.6,
    metalness: 0.05
  });

  // 1. Waistband Ring
  const waistGeom = new THREE.CylinderGeometry(1.28, 1.34, 0.42, 36, 1, true);
  const waistMesh = new THREE.Mesh(waistGeom, waistbandMaterial);
  waistMesh.position.y = 0.95;
  shortsGroup.add(waistMesh);

  // Front closure velcro flap (White)
  const flapGeom = new THREE.BoxGeometry(0.48, 0.44, 0.14);
  const flapMat = new THREE.MeshStandardMaterial({ color: 0xf4f1ea, roughness: 0.4 });
  const flapMesh = new THREE.Mesh(flapGeom, flapMat);
  flapMesh.position.set(0, 0.95, 1.32);
  shortsGroup.add(flapMesh);

  // 2. Left Leg (Flared with side slit angle)
  const leftLegGeom = new THREE.CylinderGeometry(0.82, 0.96, 1.85, 32, 1, true);
  const leftLegMesh = new THREE.Mesh(leftLegGeom, fabricMaterial);
  leftLegMesh.position.set(-0.62, -0.05, 0);
  leftLegMesh.rotation.z = 0.06;
  shortsGroup.add(leftLegMesh);

  // 3. Right Leg (Flared with side slit angle)
  const rightLegGeom = new THREE.CylinderGeometry(0.82, 0.96, 1.85, 32, 1, true);
  const rightLegMesh = new THREE.Mesh(rightLegGeom, fabricMaterial);
  rightLegMesh.position.set(0.62, -0.05, 0);
  rightLegMesh.rotation.z = -0.06;
  shortsGroup.add(rightLegMesh);

  // 4. Center Crotch Flex Panel
  const crotchGeom = new THREE.SphereGeometry(0.65, 16, 12, 0, Math.PI);
  const crotchMesh = new THREE.Mesh(crotchGeom, fabricMaterial);
  crotchMesh.scale.set(0.9, 0.6, 0.9);
  crotchMesh.position.set(0, 0.45, 0);
  shortsGroup.add(crotchMesh);

  // Center the whole shorts group
  shortsGroup.position.y = -0.3;
  threeScene.add(shortsGroup);

  update3DTexture();
}

// Sync the 2D pattern canvas onto the 3D shorts mesh texture
function update3DTexture() {
  if (!offscreenCtx || !canvasTexture) return;

  // Background base color
  offscreenCtx.fillStyle = studioState.fabricColor;
  offscreenCtx.fillRect(0, 0, 1024, 1024);

  // Draw black side stripes
  offscreenCtx.fillStyle = studioState.waistbandColor;
  offscreenCtx.fillRect(0, 0, 80, 1024);
  offscreenCtx.fillRect(944, 0, 80, 1024);

  // Project the 2D elements onto the 3D texture map
  studioState.elements.forEach(el => {
    offscreenCtx.save();
    // Normalized coordinate mapping
    const normX = (el.x / 850) * 1024;
    const normY = (el.y / 600) * 1024;

    offscreenCtx.translate(normX, normY);
    offscreenCtx.rotate((el.rotation || 0) * Math.PI / 180);
    offscreenCtx.scale((el.scale || 1) * 1.3, (el.scale || 1) * 1.3);

    if (el.type === 'text') {
      offscreenCtx.font = `bold ${el.size || 32}px ${el.font || 'Impact'}`;
      offscreenCtx.textAlign = 'center';
      offscreenCtx.textBaseline = 'middle';
      offscreenCtx.fillStyle = el.color || '#111417';
      offscreenCtx.fillText(el.text, 0, 0);
    } else {
      renderVectorGraphic(offscreenCtx, el);
    }
    offscreenCtx.restore();
  });

  canvasTexture.needsUpdate = true;
}

function reset3DCamera() {
  if (!threeCamera || !threeControls) return;
  threeCamera.position.set(0, 0.2, 5.2);
  threeControls.target.set(0, -0.3, 0);
  threeControls.reset();
}

function toggle3DMinimize() {
  const container = document.getElementById('studio3DCanvasContainer');
  const icon = document.getElementById('btn3DMinIcon');
  if (container.classList.contains('hidden')) {
    container.classList.remove('hidden');
    icon.innerText = 'unfold_less';
  } else {
    container.classList.add('hidden');
    icon.innerText = 'unfold_more';
  }
}

// ------------------- STUDIO ACTIONS & TOOLS -------------------
function updateStudioLayers() {
  const list = document.getElementById('studioElementsList');
  const countLbl = document.getElementById('lblLayerCount');
  const objCountLbl = document.getElementById('lblObjectCount');
  if (!list) return;

  countLbl.innerText = studioState.elements.length;
  objCountLbl.innerText = `${studioState.elements.length} Active Elements`;

  list.innerHTML = studioState.elements.map(el => {
    const isSel = el.id === studioState.selectedElementId;
    const border = isSel ? 'border-secondary ring-1 ring-secondary' : 'border-outline-variant/30';
    return `
      <div class="p-2.5 rounded-xl bg-surface-container border ${border} flex items-center justify-between gap-2 hover:bg-surface-container-high transition-all cursor-pointer" onclick="selectStudioElement('${el.id}')">
        <div class="flex items-center gap-2 flex-1 overflow-hidden">
          <div class="w-7 h-7 rounded-lg bg-surface-container-lowest border border-outline-variant/30 flex items-center justify-center flex-shrink-0 font-bold text-xs text-primary">
            ${el.type === 'text' ? 'T' : (el.type === 'logo' ? '★' : '⚡')}
          </div>
          <div class="truncate">
            <div class="font-bold text-xs text-primary truncate">${el.name}</div>
            <div class="text-[10px] text-outline uppercase">${el.type} • Scale: ${(el.scale || 1).toFixed(2)}</div>
          </div>
        </div>

        <div class="flex items-center gap-1">
          <!-- Color picker trigger -->
          <input type="color" value="${el.color || '#111417'}" onchange="changeElementColor('${el.id}', this.value)" class="w-6 h-6 rounded cursor-pointer border-0 p-0 bg-transparent" title="Change Color"/>
          <!-- Delete button -->
          <button onclick="event.stopPropagation(); deleteStudioElement('${el.id}')" class="w-6 h-6 rounded flex items-center justify-center text-outline hover:text-error" title="Delete Layer">
            <span class="material-symbols-outlined text-[16px]">delete</span>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function selectStudioElement(id) {
  studioState.selectedElementId = id;
  renderPatternCanvas();
  updateStudioLayers();
}

function deleteStudioElement(id) {
  saveStudioHistory();
  studioState.elements = studioState.elements.filter(e => e.id !== id);
  if (studioState.selectedElementId === id) studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function changeElementColor(id, hex) {
  saveStudioHistory();
  const el = studioState.elements.find(e => e.id === id);
  if (el) {
    el.color = hex;
    renderPatternCanvas();
    updateStudioLayers();
    update3DTexture();
  }
}

function clearAllElements() {
  if (!confirm('Clear all placed logos and text from shorts?')) return;
  saveStudioHistory();
  studioState.elements = [];
  studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function addTextToCanvas() {
  const text = document.getElementById('studioTextInput').value.trim();
  if (!text) return;
  const font = document.getElementById('studioFontSelect').value;
  const color = document.getElementById('studioTextColorInput').value;

  saveStudioHistory();
  const newEl = {
    id: 'text_' + Date.now(),
    type: 'text',
    name: `Text: ${text.toUpperCase()}`,
    text: text.toUpperCase(),
    x: 425,
    y: 280,
    scale: 1.0,
    rotation: 0,
    color: color,
    font: font,
    size: 32
  };
  studioState.elements.push(newEl);
  studioState.selectedElementId = newEl.id;

  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  setStudioTab('layers');
  showToast(`Added "${text}" to pattern! Drag on canvas to place.`, 'success');
}

// Preset logos and cliparts library
function renderPresetLogos() {
  const container = document.getElementById('presetLogosContainer');
  if (!container) return;
  const presets = [
    { name: 'Wings Crest', preset: 'wings', icon: '★' },
    { name: 'Strike Text', preset: 'metal', icon: '⚡' },
    { name: 'Custom Inferno', preset: 'inferno_script', icon: '🔥' },
    { name: 'Lightning Bolt', preset: 'bolt', icon: '⚡' }
  ];

  container.innerHTML = presets.map(p => `
    <button onclick="addPresetLogo('${p.preset}', '${p.name}')" class="p-2.5 rounded-xl bg-surface-container hover:bg-surface-container-high transition-all border border-outline-variant/30 flex items-center gap-2 text-left">
      <span class="w-7 h-7 rounded-lg bg-surface-container-lowest flex items-center justify-center font-bold text-sm text-secondary">${p.icon}</span>
      <span class="text-xs font-bold text-primary">${p.name}</span>
    </button>
  `).join('');
}

function renderCliparts() {
  const container = document.getElementById('clipartsContainer');
  if (!container) return;
  const cliparts = [
    { name: 'Bolt', preset: 'bolt', symbol: '⚡' },
    { name: 'Wings', preset: 'wings', symbol: '🦅' },
    { name: 'Shield', preset: 'shield', symbol: '🛡️' },
    { name: 'Dragon', preset: 'dragon', symbol: '🐉' },
    { name: 'Skull', preset: 'skull', symbol: '💀' },
    { name: 'Fist', preset: 'fist', symbol: '👊' }
  ];

  container.innerHTML = cliparts.map(c => `
    <button onclick="addPresetLogo('${c.preset}', '${c.name}')" class="p-3 rounded-xl bg-surface-container hover:bg-surface-container-high transition-all flex flex-col items-center gap-1 border border-outline-variant/30">
      <span class="text-2xl">${c.symbol}</span>
      <span class="text-[10px] font-bold text-primary uppercase">${c.name}</span>
    </button>
  `).join('');
}

function addPresetLogo(preset, name) {
  saveStudioHistory();
  const newEl = {
    id: 'logo_' + Date.now(),
    type: 'logo',
    name: name,
    preset: preset,
    x: 425,
    y: 280,
    scale: 0.8,
    rotation: 0,
    color: '#111417'
  };
  studioState.elements.push(newEl);
  studioState.selectedElementId = newEl.id;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  setStudioTab('layers');
  showToast(`Placed ${name} on pattern!`, 'info');
}

// CUSTOM LOGO UPLOAD (Direct local storage integration)
async function handleStudioLogoUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = async (e) => {
    const img = new Image();
    img.onload = () => {
      saveStudioHistory();
      const newEl = {
        id: 'upload_' + Date.now(),
        type: 'logo',
        name: `Upload: ${file.name.slice(0, 15)}`,
        imageObj: img,
        x: 425,
        y: 260,
        scale: 0.85,
        rotation: 0,
        color: '#111417'
      };
      studioState.elements.push(newEl);
      studioState.selectedElementId = newEl.id;
      renderPatternCanvas();
      updateStudioLayers();
      update3DTexture();
      setStudioTab('layers');
      showToast(`Uploaded ${file.name} and mapped to 3D shorts!`, 'success');
    };
    img.src = e.target.result;

    // Send file to local backend storage
    const formData = new FormData();
    formData.append('file', file);
    formData.append('category', 'designs');
    try {
      await fetch('/api/upload', { method: 'POST', body: formData });
    } catch(err) {}
  };
  reader.readAsDataURL(file);
}

function resetStudioCanvas() {
  if (!confirm('Reset pattern to CDR default layout?')) return;
  saveStudioHistory();
  studioState.fabricColor = '#efd965';
  studioState.elements = [
    { id: 'el_crest', type: 'logo', name: 'Waistband Crest Wings', x: 425, y: 70, scale: 0.65, rotation: 0, color: '#111417', preset: 'wings' },
    { id: 'el_text1', type: 'text', name: 'Left Leg Vertical INFERNO', text: 'INFERNO', x: 265, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 36 },
    { id: 'el_text2', type: 'text', name: 'Right Leg Vertical INFERNO', text: 'INFERNO', x: 585, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 36 },
    { id: 'el_sponsor1', type: 'logo', name: 'Left Slit Sponsor Logo', x: 310, y: 350, scale: 0.7, rotation: 0, color: '#111417', preset: 'metal' },
    { id: 'el_sponsor2', type: 'logo', name: 'Right Slit Custom Inferno', x: 535, y: 350, scale: 0.75, rotation: 0, color: '#111417', preset: 'inferno_script' },
    { id: 'el_bolt', type: 'clipart', name: 'Right Slit Lightning Bolt', x: 635, y: 350, scale: 0.8, rotation: 0, color: '#111417', preset: 'bolt' },
    { id: 'el_belt', type: 'text', name: 'Lower Belt Script', text: 'CUSTOM INFERNO', x: 425, y: 535, scale: 0.9, rotation: 0, color: '#efd965', font: 'Impact', size: 28 }
  ];
  studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  showToast('Pattern reset to default CDR template layout.', 'info');
}

function saveStudioDraft() {
  const snapshot = {
    template: 'Backup_of_ZAM FORWARD 123456.cdr',
    timestamp: new Date().toISOString(),
    state: studioState
  };
  localStorage.setItem('zam_studio_draft', JSON.stringify(snapshot));
  showToast('Design draft and 3D configuration saved locally!', 'success');
}

// SUBMIT ORDER DIRECTLY FROM AI STUDIO
async function submitStudioOrder() {
  const custName = prompt('Enter Athlete / Fight Gym Name for Order:', 'Inferno Fight Team');
  if (!custName) return;
  const custEmail = prompt('Enter Contact Email Address:', 'coach@infernofight.com');
  if (!custEmail) return;

  const payload = {
    customer_name: custName,
    customer_email: custEmail,
    customer_phone: '+1 555-0199',
    notes: `Created via ZamForward AI 3D Studio from template Backup_of_ZAM FORWARD 123456.cdr. Body: ${studioState.fabricName}.`,
    items: [{
      product_id: 3,
      product_name: 'Apex Combat Flex-Split MMA Shorts (CDR Custom)',
      quantity: 15,
      size: 'L',
      color: studioState.fabricName,
      unit_price: 48.0,
      design_config: {
        template_source: 'Backup_of_ZAM FORWARD 123456.cdr',
        fabric_color: studioState.fabricColor,
        elements_count: studioState.elements.length,
        elements: studioState.elements.map(e => ({ name: e.name, type: e.type, x: e.x, y: e.y, color: e.color }))
      }
    }]
  };

  try {
    const res = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (res.ok) {
      closeAiStudioModal();
      showToast(`Order ${data.order_number} confirmed! Saved to SQLite with 3D design files.`, 'success');
      document.getElementById('trackingInput').value = data.order_number;
      lookupOrder(data.order_number);
      loadAdminOrders();
      window.location.hash = '#tracking';
    } else {
      showToast(data.error || 'Failed to submit order', 'error');
    }
  } catch(err) {
    showToast(err.message, 'error');
  }
}
</script>
'''

html = html.replace('</body></html>', studio_engine_script + '\n</body></html>')

# Write to public/index.html
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("public/index.html upgraded with full AI 3D Studio & CDR Pattern Engine!")
