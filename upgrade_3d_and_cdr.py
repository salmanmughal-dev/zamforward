import re

# Read current public/index.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Floating 3D Preview Window HTML in the AI Studio Modal
# Make it larger (w-80 sm:w-96, h-80 sm:h-96), clean light/studio backdrop, angle buttons, and Dual Render Mode
old_3d_card = re.search(r'<div id="studio3DFloatingCard".*?<!-- 2D FLAT PATTERN CANVAS AREA -->', html, re.DOTALL)

new_3d_card = '''<div id="studio3DFloatingCard" class="absolute top-4 left-4 z-20 w-80 sm:w-96 bg-white/95 backdrop-blur-md rounded-2xl shadow-2xl border border-slate-300 overflow-hidden flex flex-col transition-all duration-300">
        <!-- 3D Header -->
        <div class="px-4 py-2.5 bg-slate-900 text-white flex items-center justify-between text-xs cursor-move" id="studio3DHeader">
          <div class="flex items-center gap-2 font-bold uppercase tracking-wider text-[11px]">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>3D Fight Shorts Simulation</span>
          </div>
          <div class="flex items-center gap-1.5">
            <!-- Render Mode Toggle -->
            <button onclick="toggle3DRenderMode()" id="btnRenderMode" class="px-2 py-0.5 rounded bg-sky-600 text-white text-[10px] font-bold uppercase hover:bg-sky-500 transition-colors" title="Switch between 3D Orbit and Photo Render">
              3D Orbit
            </button>
            <button onclick="toggle3DAutoRotate()" id="btnAutoRotate" class="p-1 rounded text-slate-400 hover:text-white" title="Auto-spin 360°">
              <span class="material-symbols-outlined text-[16px]">rotate_right</span>
            </button>
            <button onclick="reset3DCamera()" class="p-1 rounded text-slate-400 hover:text-white" title="Reset Camera">
              <span class="material-symbols-outlined text-[16px]">sync</span>
            </button>
            <button onclick="toggle3DMinimize()" class="p-1 rounded text-slate-400 hover:text-white" title="Minimize / Expand">
              <span id="btn3DMinIcon" class="material-symbols-outlined text-[16px]">unfold_less</span>
            </button>
          </div>
        </div>

        <!-- 3D Viewport (Height 340px for generous viewing) -->
        <div id="studio3DCanvasContainer" class="relative w-full h-80 sm:h-96 bg-gradient-to-b from-slate-100 via-slate-50 to-slate-200 flex items-center justify-center overflow-hidden">
          <!-- Three.js Canvas -->
          <canvas id="threeCanvas" class="w-full h-full cursor-grab active:cursor-grabbing"></canvas>
          
          <!-- Photorealistic 2D Render Overlay (Alternate Mode) -->
          <div id="photoRenderOverlay" class="absolute inset-0 hidden flex items-center justify-center bg-gradient-to-b from-slate-50 to-slate-200 p-4">
            <canvas id="photoCanvas" width="500" height="500" class="max-w-full max-h-full object-contain drop-shadow-2xl"></canvas>
          </div>

          <!-- Bottom Floating Controls: 3D Rotation Badge & Quick Angles -->
          <div class="absolute bottom-3 inset-x-3 flex items-center justify-between pointer-events-none">
            <!-- 3D Badge (Matches reference screenshot) -->
            <div class="pointer-events-auto px-3 py-1 rounded-full bg-sky-600 text-white text-[11px] font-bold uppercase tracking-wider flex items-center gap-1.5 shadow-lg">
              <span class="material-symbols-outlined text-[16px] animate-spin" style="animation-duration: 8s;">360</span>
              <span id="lbl3DMode">3D Orbit</span>
            </div>

            <!-- Quick Angle Pills -->
            <div class="pointer-events-auto flex items-center gap-1 bg-white/90 backdrop-blur-sm p-1 rounded-xl shadow-md border border-slate-200 text-[10px] font-bold text-slate-700">
              <button onclick="set3DAngle('front')" class="px-2 py-0.5 rounded hover:bg-slate-200">Front</button>
              <button onclick="set3DAngle('left')" class="px-2 py-0.5 rounded hover:bg-slate-200">Left</button>
              <button onclick="set3DAngle('right')" class="px-2 py-0.5 rounded hover:bg-slate-200">Right</button>
              <button onclick="set3DAngle('back')" class="px-2 py-0.5 rounded hover:bg-slate-200">Back</button>
            </div>
          </div>

          <!-- Helpful drag hint -->
          <div class="absolute top-2 left-2 pointer-events-none text-[10px] font-medium text-slate-600 bg-white/80 backdrop-blur-sm px-2 py-0.5 rounded shadow-sm border border-slate-200">
            🖱️ Drag to rotate 360° • Scroll to zoom
          </div>
        </div>
      </div>

      <!-- 2D FLAT PATTERN CANVAS AREA -->'''

if old_3d_card:
    html = html.replace(old_3d_card.group(0), new_3d_card)

# 2. Update the 2D Pattern Canvas wrapper & header for high-definition CDR pattern
old_canvas_header = re.search(r'<!-- Top Waistband Logo Placement -->.*?<canvas id="patternCanvas"', html, re.DOTALL)
new_canvas_header = '''<!-- Top CDR Blueprint Specification Header -->
          <div class="flex items-center justify-between pb-3 mb-2 border-b border-slate-200 text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-sky-100 text-sky-800 font-bold font-mono text-[11px] uppercase">
                CorelDraw CDR Master Pattern
              </span>
              <span class="font-bold text-slate-800">Backup_of_ZAM FORWARD 123456.cdr</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-slate-500 font-medium hidden sm:inline">Scale: 1:1 Sublimation DieCut</span>
              <a href="/uploads/templates/Backup_of_ZAM_FORWARD_123456.cdr" download class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 text-[11px] font-bold hover:bg-slate-200 transition-colors flex items-center gap-1">
                <span class="material-symbols-outlined text-[14px]">download</span>
                <span>Download .CDR</span>
              </a>
            </div>
          </div>

          <!-- Helpful Guidance Pill -->
          <div class="mb-3 px-3 py-1.5 rounded-xl bg-sky-50 border border-sky-200/60 text-sky-900 text-xs flex items-center justify-between gap-2">
            <div class="flex items-center gap-1.5">
              <span class="material-symbols-outlined text-sky-600 text-[18px]">touch_app</span>
              <span><strong>Interactive Design:</strong> Click and drag any text or logo to position it. Watch the 3D preview on the left update in real time!</span>
            </div>
            <button onclick="addPresetLogo('wings', 'Waistband Wings')" class="text-[11px] font-bold text-sky-700 hover:underline uppercase whitespace-nowrap">+ Add Wings Crest</button>
          </div>

          <!-- HTML5 2D Pattern Canvas -->
          <canvas id="patternCanvas"'''

if old_canvas_header:
    html = html.replace(old_canvas_header.group(0), new_canvas_header)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("AI Studio UI elements and 3D preview layout updated.")
