import re

# Read DESIGN.md tokens and design specifications
# We will create public/index.html with 100% adherence to DESIGN.md

with open('public/index.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

# 1. Update <head> with Space Grotesk & Plus Jakarta Sans, Tailwind theme with DESIGN.md color palette
head_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>ZamForward Combat Apparel — Apex Combat Editorial Atelier</title>
  
  <!-- Fonts: Space Grotesk & Plus Jakarta Sans as per DESIGN.md -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>

  <!-- Three.js for 3D Simulation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>

  <!-- Tailwind CSS with DESIGN.md Theme Configuration -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "surface": "#F4F1EA",             // Neutral Base Canvas (Warm Sandstone)
            "surface-dim": "#DCDAD3",
            "surface-bright": "#FCF9F2",
            "surface-container-lowest": "#FFFFFF",
            "surface-container-low": "#F6F3EC",
            "surface-container": "#EDE8DE",    // Subtle Recessed Neutral Card Tint
            "surface-container-high": "#E5E2DB",
            "surface-container-highest": "#DFD9CC",
            "on-surface": "#111417",           // Text Primary (Deep Onyx)
            "on-surface-variant": "#6B675E",   // Text Secondary (Warm Mineral Gray)
            "primary": "#111417",              // Deep Onyx Slate
            "primary-container": "#191C1F",
            "on-primary": "#F4F1EA",
            "secondary": "#088395",            // Combat Cyan / Deep Teal
            "secondary-container": "#E0F7FA",
            "on-secondary-container": "#004E5A",
            "tertiary": "#C9A86A",             // Champion Gold / Ochre
            "tertiary-container": "#261900",
            "outline": "#75777B",
            "outline-variant": "#DFD9CC",      // Fine Sandstone Border Rule
            "error": "#C53030",
            "success": "#107C41"
          },
          fontFamily: {
            "display-hero": ["Space Grotesk", "sans-serif"],
            "headline-lg": ["Space Grotesk", "sans-serif"],
            "headline-md": ["Space Grotesk", "sans-serif"],
            "headline-sm": ["Space Grotesk", "sans-serif"],
            "category-caps": ["Space Grotesk", "sans-serif"],
            "title-md": ["Plus Jakarta Sans", "sans-serif"],
            "title-sm": ["Plus Jakarta Sans", "sans-serif"],
            "body-lg": ["Plus Jakarta Sans", "sans-serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"],
            "body-sm": ["Plus Jakarta Sans", "sans-serif"],
            "label-lg": ["Plus Jakarta Sans", "sans-serif"],
            "label-md": ["Plus Jakarta Sans", "sans-serif"]
          },
          borderRadius: {
            DEFAULT: "0.25rem",
            sm: "0.25rem",
            md: "0.5rem",
            lg: "0.75rem",
            xl: "1rem",
            "2xl": "1.5rem",
            full: "9999px"
          },
          spacing: {
            "gutter": "1.5rem",
            "margin": "3.5rem",
            "margin-tablet": "2rem",
            "margin-mobile": "1.25rem"
          }
        }
      }
    };
  </script>
  <style>
    body {
      background-color: #F4F1EA;
      color: #111417;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    h1, h2, h3, .font-heading {
      font-family: 'Space Grotesk', sans-serif;
    }
    ::-webkit-scrollbar { display: none; }
  </style>
</head>
<body class="bg-[#F4F1EA] text-[#111417] antialiased selection:bg-[#088395] selection:text-white">'''

# 2. Build the Complete, Clean, Editorial Landing Page according to DESIGN.md
# Extract the modal definitions and scripts from current_html so we retain all functionality
modals_idx = current_html.find('<!-- ================= AI 3D STUDIO FULL-SCREEN WORKSPACE MODAL ================= -->')
if modals_idx == -1:
    modals_idx = current_html.find('<!-- ================= MODALS & SLIDEOUT PANELS ================= -->')
modals_and_js = current_html[modals_idx:]

editorial_body = '''
  <!-- TOP UTILITY RAIL (36px Marquee Announcement as per DESIGN.md Sectional Rhythm) -->
  <div class="w-full bg-[#111417] text-[#F4F1EA] h-9 px-4 text-center font-mono text-xs tracking-wider uppercase flex items-center justify-center gap-3 z-50 relative">
    <span>Free Team Swatch Kits &amp; Global Shipping on Orders over $250</span>
    <span class="opacity-40">•</span>
    <span class="text-[#088395] font-bold">Use Code ZAMCOMBAT</span>
    <span class="opacity-40 hidden md:inline">•</span>
    <span class="text-[#EDE8DE] hidden md:inline font-mono">Batch 43 Atelier Production Active</span>
  </div>

  <!-- EDITORIAL HEADER (Fixed 72px, Warm Sandstone Translucent with Fine 1px Sandstone Border) -->
  <header class="sticky top-0 w-full z-40 bg-[#F4F1EA]/95 backdrop-blur-md border-b border-[#DFD9CC]">
    <div class="h-18 max-w-[1360px] mx-auto px-4 sm:px-8 flex items-center justify-between gap-6">
      
      <!-- Brand Logo -->
      <a href="#" class="flex items-center gap-3 flex-shrink-0 group">
        <div class="w-10 h-10 rounded-lg bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-display-hero font-bold text-lg group-hover:bg-[#088395] transition-colors">
          ZF
        </div>
        <div class="flex flex-col">
          <span class="font-headline-sm text-xl font-bold tracking-tight text-[#111417] uppercase leading-none">ZamForward</span>
          <span class="font-mono text-[10px] tracking-widest text-[#088395] uppercase font-bold mt-1">Combat Apparel Atelier</span>
        </div>
      </a>

      <!-- Center Editorial Navigation (Single line, Space Grotesk Category Caps & Plus Jakarta Sans) -->
      <nav class="hidden lg:flex items-center gap-1 xl:gap-2">
        <a href="#" class="px-3 py-1.5 rounded text-sm font-semibold text-[#111417] bg-[#EDE8DE] transition-colors">Home</a>
        <a href="#catalog" class="px-3 py-1.5 rounded text-sm font-semibold text-[#6B675E] hover:text-[#111417] hover:bg-[#EDE8DE] transition-colors">Catalog</a>
        <button onclick="openAiStudioModal()" class="px-3 py-1.5 rounded text-sm font-bold text-[#088395] hover:bg-[#088395]/10 transition-colors flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
          <span>AI 3D Studio</span>
          <span class="px-1.5 py-0.2 rounded bg-[#088395] text-white text-[9px] font-mono font-bold uppercase">CDR</span>
        </button>
        <a href="#workflow" class="px-3 py-1.5 rounded text-sm font-semibold text-[#6B675E] hover:text-[#111417] hover:bg-[#EDE8DE] transition-colors">Workflow</a>
        <button onclick="openCdrTemplateVault()" class="px-3 py-1.5 rounded text-sm font-semibold text-[#6B675E] hover:text-[#111417] hover:bg-[#EDE8DE] transition-colors">CDR Vault</button>
        <a href="#tracking" class="px-3 py-1.5 rounded text-sm font-semibold text-[#6B675E] hover:text-[#111417] hover:bg-[#EDE8DE] transition-colors">Track ZAM-ID</a>
      </nav>

      <!-- Right Utility Actions -->
      <div class="flex items-center gap-3">
        <!-- Search Pill -->
        <div class="hidden md:flex items-center bg-[#EDE8DE] px-3.5 py-2 rounded-lg border border-[#DFD9CC] focus-within:border-[#088395] transition-all">
          <span class="material-symbols-outlined text-[#75777B] text-[18px] mr-2">search</span>
          <input class="bg-transparent text-[#111417] placeholder:text-[#75777B] text-xs font-medium focus:outline-none w-28 xl:w-44" placeholder="Search rashguards, Gis..." type="text"/>
        </div>

        <!-- Custom Mockup CTA -->
        <button onclick="openAiStudioModal()" class="px-4 py-2 rounded-lg bg-[#111417] text-[#F4F1EA] text-xs font-bold uppercase tracking-wider hover:bg-[#088395] transition-all shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[16px] text-[#088395]">draw</span>
          <span>Start 3D Design</span>
        </button>

        <!-- Account Pill -->
        <button onclick="openAuthModal()" class="flex items-center gap-2 pl-1 hover:opacity-90 transition-opacity">
          <div class="w-8 h-8 rounded-full bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-bold text-xs ring-2 ring-[#088395]/40">
            <span class="material-symbols-outlined text-[18px]">person</span>
          </div>
          <span id="headerUserLabel" class="hidden xl:inline text-xs font-semibold text-[#111417]">Sign In</span>
        </button>
      </div>

    </div>
  </header>

  <main class="w-full">
    
    <!-- 1. HERO SECTION (Apex Combat Editorial Architecture as per DESIGN.md) -->
    <section class="max-w-[1360px] mx-auto px-4 sm:px-8 pt-8 pb-16">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
        
        <!-- Left Editorial Column (7 Columns) -->
        <div class="lg:col-span-7 space-y-6">
          
          <!-- Technical Chip / IBJJF Atelier Tag -->
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#EDE8DE] text-[#088395] font-mono text-xs uppercase font-bold tracking-wider border border-[#DFD9CC]">
            <span class="w-2 h-2 rounded-full bg-[#088395] animate-pulse"></span>
            <span>Official BJJ &amp; MMA Combat Apparel Atelier</span>
          </div>

          <!-- Master Space Grotesk Headline (DESIGN.md display-hero) -->
          <div class="space-y-1">
            <h1 class="font-display-hero text-4xl sm:text-5xl lg:text-[56px] text-[#111417] font-bold uppercase tracking-tight leading-[1.05]">
              Engineered for Combat.
            </h1>
            <h1 class="font-display-hero text-4xl sm:text-5xl lg:text-[56px] text-[#088395] font-bold uppercase tracking-tight leading-[1.05] flex items-center gap-3">
              Built for Champions
              <span class="material-symbols-outlined text-[36px] sm:text-[48px] text-[#088395]">verified</span>
            </h1>
          </div>

          <!-- Editorial Narrative in Plus Jakarta Sans -->
          <p class="font-body-lg text-base sm:text-lg text-[#6B675E] max-w-2xl leading-relaxed">
            High-performance custom sublimated rashguards, IBJJF-compliant Gis, and competition fightwear engineered for championship academies worldwide. Zero MOQ on team kits, 50% milestone deposits, and rapid worldwide dispatch.
          </p>

          <!-- Primary Action CTAs -->
          <div class="flex flex-wrap items-center gap-4 pt-2">
            <button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-lg bg-[#111417] text-[#F4F1EA] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#088395] transition-all shadow-md flex items-center gap-2 group">
              <span class="material-symbols-outlined text-[18px] text-[#088395] group-hover:text-white transition-colors">view_in_ar</span>
              <span>Launch AI 3D Studio</span>
              <span class="px-2 py-0.5 rounded bg-[#088395] text-white text-[10px] font-mono uppercase font-bold">CDR v17</span>
            </button>
            
            <a href="#tracking" class="px-5 py-3.5 rounded-lg bg-[#EDE8DE] text-[#111417] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#E5E2DB] transition-colors border border-[#DFD9CC] flex items-center gap-2">
              <span class="material-symbols-outlined text-[18px] text-[#088395]">track_changes</span>
              <span>Track Order (ZAM-ID)</span>
            </a>

            <button onclick="openCdrTemplateVault()" class="px-4 py-3.5 rounded-lg bg-transparent text-[#6B675E] hover:text-[#111417] text-xs uppercase font-bold font-mono transition-colors flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[18px]">draft</span>
              <span>Master CDR Vector Vault</span>
            </button>
          </div>

          <!-- Trust & Standards Strip (DESIGN.md Level 1 Elevation & Champion Gold #C9A86A) -->
          <div class="pt-6 border-t border-[#DFD9CC] grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div>
              <div class="font-headline-sm text-2xl font-bold text-[#111417]">50,000+</div>
              <div class="font-body-sm text-xs text-[#6B675E]">Athletes Geared</div>
            </div>
            <div>
              <div class="font-headline-sm text-2xl font-bold text-[#088395]">450 GSM</div>
              <div class="font-body-sm text-xs text-[#6B675E]">Sublimated Spandex</div>
            </div>
            <div>
              <div class="font-headline-sm text-2xl font-bold text-[#111417]">IBJJF Legal</div>
              <div class="font-body-sm text-xs text-[#6B675E]">5 Belt Ranks Standard</div>
            </div>
            <div>
              <div class="flex text-[#C9A86A] items-center">
                <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">star</span>
              </div>
              <div class="font-body-sm text-xs text-[#6B675E]">500+ Fight Academies</div>
            </div>
          </div>

        </div>

        <!-- Right Focal Column: Clean High-Res Product Showcase (5 Columns) -->
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-2xl overflow-hidden shadow-xl bg-[#EDE8DE] border border-[#DFD9CC] group">
            
            <div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="https://lh3.googleusercontent.com/aida-public/AB6AXuB0bh0920oDUW-DNllDkVgJHiLrVgCYZ1U9cpr5N63qaBsUAtRT3sFYzf9BVo3te9auHuUQN7s4M4SvKVBOjYOP6Qj6lb4U1-Tzh9OAsOZOuRxyOIVWldqggpafh8WCojkZKWozMX2EuTcS5LLeG804jVS_l-8ysyiLJmRx41ByWm7fks1csoTcV0MK1jokTkVCpcpPxJeYvTpTqqej6O26WVpjeSWahMf_SCPs8MjdrTD2rDDzkaw"/>
              
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
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- 2. CATEGORY NAVIGATION RIBBON & VALUE PROPOSITION MODULES (DESIGN.md Sectional Rhythm) -->
    <section class="w-full bg-[#EDE8DE]/60 py-6 mb-16 border-y border-[#DFD9CC]">
      <div class="max-w-[1360px] mx-auto px-4 sm:px-8">
        
        <!-- Horizontal Category Strip with Category Caps -->
        <div class="flex items-center justify-between gap-3 overflow-x-auto pb-2 no-scrollbar">
          <a class="flex items-center gap-2.5 px-4 py-2.5 bg-[#FFFFFF] rounded-lg whitespace-nowrap hover:bg-[#111417] hover:text-[#F4F1EA] transition-all shadow-sm border border-[#DFD9CC] font-category-caps text-xs uppercase font-bold tracking-wider" href="#catalog">
            <span class="material-symbols-outlined text-[18px] text-[#088395]">fitness_center</span>
            <span>Rashguards ↗</span>
          </a>
          <a class="flex items-center gap-2.5 px-4 py-2.5 bg-[#FFFFFF] rounded-lg whitespace-nowrap hover:bg-[#111417] hover:text-[#F4F1EA] transition-all shadow-sm border border-[#DFD9CC] font-category-caps text-xs uppercase font-bold tracking-wider" href="#catalog">
            <span class="material-symbols-outlined text-[18px] text-[#088395]">sports_mma</span>
            <span>MMA Fight Shorts ↗</span>
          </a>
          <a class="flex items-center gap-2.5 px-4 py-2.5 bg-[#FFFFFF] rounded-lg whitespace-nowrap hover:bg-[#111417] hover:text-[#F4F1EA] transition-all shadow-sm border border-[#DFD9CC] font-category-caps text-xs uppercase font-bold tracking-wider" href="#catalog">
            <span class="material-symbols-outlined text-[18px] text-[#088395]">military_tech</span>
            <span>BJJ Gis &amp; Belts ↗</span>
          </a>
          <a class="flex items-center gap-2.5 px-4 py-2.5 bg-[#FFFFFF] rounded-lg whitespace-nowrap hover:bg-[#111417] hover:text-[#F4F1EA] transition-all shadow-sm border border-[#DFD9CC] font-category-caps text-xs uppercase font-bold tracking-wider" href="#catalog">
            <span class="material-symbols-outlined text-[18px] text-[#088395]">sports_kabaddi</span>
            <span>Muay Thai Retro ↗</span>
          </a>
          <a class="flex items-center gap-2.5 px-4 py-2.5 bg-[#FFFFFF] rounded-lg whitespace-nowrap hover:bg-[#111417] hover:text-[#F4F1EA] transition-all shadow-sm border border-[#DFD9CC] font-category-caps text-xs uppercase font-bold tracking-wider" href="#catalog">
            <span class="material-symbols-outlined text-[18px] text-[#088395]">accessibility_new</span>
            <span>Compression Spats ↗</span>
          </a>
          <button onclick="openAiStudioModal()" class="flex items-center gap-2.5 px-4 py-2.5 bg-[#088395] text-white rounded-lg whitespace-nowrap hover:opacity-90 transition-all shadow-sm font-category-caps text-xs uppercase font-bold tracking-wider">
            <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
            <span>Custom Kits (3D) ↗</span>
          </button>
        </div>

        <!-- 4-Column Value Proposition Grid (DESIGN.md Level 1 Surface Elevation) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          <div class="bg-[#FFFFFF] p-4 rounded-xl flex items-center gap-3.5 shadow-sm border border-[#DFD9CC]">
            <div class="w-11 h-11 rounded-lg bg-[#EDE8DE] flex items-center justify-center text-[#088395] flex-shrink-0">
              <span class="material-symbols-outlined text-[22px]">timer</span>
            </div>
            <div>
              <h5 class="font-headline-sm text-xs text-[#111417] uppercase font-bold">Guaranteed Lead-Time</h5>
              <p class="font-body-sm text-[11px] text-[#6B675E]">60-day complete run &amp; delivery</p>
            </div>
          </div>

          <div class="bg-[#FFFFFF] p-4 rounded-xl flex items-center gap-3.5 shadow-sm border border-[#DFD9CC]">
            <div class="w-11 h-11 rounded-lg bg-[#EDE8DE] flex items-center justify-center text-[#088395] flex-shrink-0">
              <span class="material-symbols-outlined text-[22px]">payments</span>
            </div>
            <div>
              <h5 class="font-headline-sm text-xs text-[#111417] uppercase font-bold">50% Milestone Invoicing</h5>
              <p class="font-body-sm text-[11px] text-[#6B675E]">Clear deposit upon slip upload</p>
            </div>
          </div>

          <div class="bg-[#FFFFFF] p-4 rounded-xl flex items-center gap-3.5 shadow-sm border border-[#DFD9CC]">
            <div class="w-11 h-11 rounded-lg bg-[#EDE8DE] flex items-center justify-center text-[#088395] flex-shrink-0">
              <span class="material-symbols-outlined text-[22px]">architecture</span>
            </div>
            <div>
              <h5 class="font-headline-sm text-xs text-[#111417] uppercase font-bold">Corel (.CDR) Vector Suite</h5>
              <p class="font-body-sm text-[11px] text-[#6B675E]">Direct vector cut &amp; zone markup</p>
            </div>
          </div>

          <div class="bg-[#FFFFFF] p-4 rounded-xl flex items-center gap-3.5 shadow-sm border border-[#DFD9CC]">
            <div class="w-11 h-11 rounded-lg bg-[#EDE8DE] flex items-center justify-center text-[#088395] flex-shrink-0">
              <span class="material-symbols-outlined text-[22px]">local_shipping</span>
            </div>
            <div>
              <h5 class="font-headline-sm text-xs text-[#111417] uppercase font-bold">Real-Time ZAM-ID</h5>
              <p class="font-body-sm text-[11px] text-[#6B675E]">Milestone tracking &amp; DHL dispatch</p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 3. BEST SELLERS & PRODUCT CATALOG (DESIGN.md Editorial Card Grid) -->
    <section class="max-w-[1360px] mx-auto px-4 sm:px-8 w-full mb-20" id="catalog">
      <div class="text-center max-w-xl mx-auto mb-10">
        <span class="font-mono text-xs uppercase tracking-widest text-[#088395] font-bold">Tournaments &amp; Mat Proven</span>
        <h2 class="font-headline-lg text-3xl md:text-4xl text-[#111417] font-bold uppercase mt-1">Best Selling Combat Apparel</h2>
        <div class="flex items-center justify-center gap-2 mt-4 flex-wrap">
          <button class="px-4 py-1.5 rounded-full bg-[#111417] text-[#F4F1EA] text-xs font-headline-sm uppercase font-bold">All Combat</button>
          <button class="px-4 py-1.5 rounded-full bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] text-xs font-headline-sm uppercase font-bold transition-colors">Rashguards</button>
          <button class="px-4 py-1.5 rounded-full bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] text-xs font-headline-sm uppercase font-bold transition-colors">Fight Shorts</button>
          <button class="px-4 py-1.5 rounded-full bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] text-xs font-headline-sm uppercase font-bold transition-colors">BJJ Gis</button>
          <button class="px-4 py-1.5 rounded-full bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] text-xs font-headline-sm uppercase font-bold transition-colors">Muay Thai</button>
        </div>
      </div>

      <!-- 3x2 Product Grid (DESIGN.md Specifications) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Card 1 -->
        <div class="bg-[#FFFFFF] rounded-2xl overflow-hidden border border-[#DFD9CC] shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
          <div class="relative aspect-[4/5] bg-[#EDE8DE] overflow-hidden">
            <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600" alt="Apex Pro Rashguard"/>
            <div class="absolute top-3 left-3 bg-[#111417] text-[#F4F1EA] font-mono text-[10px] uppercase font-bold px-2 py-0.5 rounded">
              IBJJF Compliant
            </div>
            <div class="absolute top-3 right-3 bg-[#FFFFFF]/90 backdrop-blur-sm text-[#111417] font-mono text-[10px] font-bold px-2 py-0.5 rounded border border-[#DFD9CC]">
              450 GSM
            </div>
          </div>
          <div class="p-5 flex flex-col justify-between flex-1">
            <div>
              <div class="flex items-center justify-between mb-1">
                <span class="font-mono text-[11px] text-[#088395] font-bold uppercase">Sublimation Rashguard</span>
                <span class="font-headline-sm text-lg font-bold text-[#111417]">$54.00</span>
              </div>
              <h3 class="font-headline-sm text-base font-bold text-[#111417] uppercase">Apex Sublimated Short-Sleeve Rashguard</h3>
              <p class="font-body-sm text-xs text-[#6B675E] mt-1">450 GSM Poly-Spandex with 6-needle flatlock contrast seams and silicone waist grip.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] flex items-center justify-between">
              <span class="text-[11px] text-[#6B675E] font-medium">XS • S • M • L • XL • 2XL</span>
              <button onclick="openCustomOrderModal(1)" class="px-3.5 py-1.5 rounded-lg bg-[#111417] text-[#F4F1EA] text-xs font-bold uppercase hover:bg-[#088395] transition-colors">
                Order Custom
              </button>
            </div>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="bg-[#FFFFFF] rounded-2xl overflow-hidden border border-[#DFD9CC] shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
          <div class="relative aspect-[4/5] bg-[#EDE8DE] overflow-hidden">
            <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAY1r2qM1B994s91o1676v2T4iYc3k_1o6h7m-89cf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ" alt="Apex Combat MMA Shorts"/>
            <div class="absolute top-3 left-3 bg-[#088395] text-white font-mono text-[10px] uppercase font-bold px-2 py-0.5 rounded">
              CDR Template Ready
            </div>
            <div class="absolute top-3 right-3 bg-[#FFFFFF]/90 backdrop-blur-sm text-[#111417] font-mono text-[10px] font-bold px-2 py-0.5 rounded border border-[#DFD9CC]">
              220 GSM Ripstop
            </div>
          </div>
          <div class="p-5 flex flex-col justify-between flex-1">
            <div>
              <div class="flex items-center justify-between mb-1">
                <span class="font-mono text-[11px] text-[#088395] font-bold uppercase">Fight Shorts</span>
                <span class="font-headline-sm text-lg font-bold text-[#111417]">$48.00</span>
              </div>
              <h3 class="font-headline-sm text-base font-bold text-[#111417] uppercase">Apex Combat Flex-Split MMA Shorts</h3>
              <p class="font-body-sm text-xs text-[#6B675E] mt-1">4-way stretch crotch panel, reinforced side split slits, and internal drawstring lock.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] flex items-center justify-between">
              <span class="text-[11px] text-[#6B675E] font-medium">S • M • L • XL • 2XL</span>
              <button onclick="openAiStudioModal()" class="px-3.5 py-1.5 rounded-lg bg-[#088395] text-white text-xs font-bold uppercase hover:opacity-90 transition-opacity">
                Design in 3D
              </button>
            </div>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="bg-[#FFFFFF] rounded-2xl overflow-hidden border border-[#DFD9CC] shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
          <div class="relative aspect-[4/5] bg-[#EDE8DE] overflow-hidden">
            <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600" alt="BJJ Competition Gi"/>
            <div class="absolute top-3 left-3 bg-[#111417] text-[#F4F1EA] font-mono text-[10px] uppercase font-bold px-2 py-0.5 rounded">
              5 Belt Ranks
            </div>
            <div class="absolute top-3 right-3 bg-[#FFFFFF]/90 backdrop-blur-sm text-[#111417] font-mono text-[10px] font-bold px-2 py-0.5 rounded border border-[#DFD9CC]">
              550 GSM Gold
            </div>
          </div>
          <div class="p-5 flex flex-col justify-between flex-1">
            <div>
              <div class="flex items-center justify-between mb-1">
                <span class="font-mono text-[11px] text-[#088395] font-bold uppercase">Kimono / Gi</span>
                <span class="font-headline-sm text-lg font-bold text-[#111417]">$135.00</span>
              </div>
              <h3 class="font-headline-sm text-base font-bold text-[#111417] uppercase">IBJJF Pro Gold Weave Kimono (Gi)</h3>
              <p class="font-body-sm text-xs text-[#6B675E] mt-1">Heavy-duty 550 GSM gold weave jacket with 10oz ripstop pants. Custom embroidery ready.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] flex items-center justify-between">
              <span class="text-[11px] text-[#6B675E] font-medium">A0 • A1 • A2 • A3 • A4 • A5</span>
              <button onclick="openCustomOrderModal(4)" class="px-3.5 py-1.5 rounded-lg bg-[#111417] text-[#F4F1EA] text-xs font-bold uppercase hover:bg-[#088395] transition-colors">
                Order Custom
              </button>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 4. CUSTOM WORKFLOW ENGINE (DESIGN.md 4-Step Order Visualizer) -->
    <section class="max-w-[1360px] mx-auto px-4 sm:px-8 w-full mb-20" id="workflow">
      <div class="bg-[#EDE8DE] p-8 md:p-12 rounded-3xl border border-[#DFD9CC] shadow-sm">
        
        <div class="text-center max-w-xl mx-auto mb-10">
          <span class="font-mono text-xs uppercase tracking-widest text-[#088395] font-bold">Factory Direct Pipeline</span>
          <h2 class="font-headline-lg text-2xl md:text-3xl text-[#111417] font-bold uppercase mt-1">The ZamForward Manufacturing Engine</h2>
          <p class="font-body-sm text-sm text-[#6B675E] mt-1">From vector upload to laser sublimation and doorstep delivery.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-[#FFFFFF] p-6 rounded-2xl border border-[#DFD9CC] shadow-sm flex flex-col justify-between">
            <div>
              <span class="w-8 h-8 rounded-lg bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-bold text-xs mb-4">01</span>
              <h4 class="font-headline-sm text-base text-[#111417] uppercase font-bold">1. Design &amp; Mockup</h4>
              <p class="font-body-sm text-xs text-[#6B675E] mt-2">Upload your gym vector or use our 3D builder with CorelDraw master templates.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] text-[11px] font-mono text-[#088395] font-bold">Specs Locked (ZAM-ID)</div>
          </div>

          <div class="bg-[#FFFFFF] p-6 rounded-2xl border border-[#DFD9CC] shadow-sm flex flex-col justify-between">
            <div>
              <span class="w-8 h-8 rounded-lg bg-[#088395] text-white flex items-center justify-center font-bold text-xs mb-4">02</span>
              <h4 class="font-headline-sm text-base text-[#111417] uppercase font-bold">2. 50% Milestone Invoicing</h4>
              <p class="font-body-sm text-xs text-[#6B675E] mt-2">Auto-calculated invoice sent to your dashboard. Upload wire slip to clear production.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] text-[11px] font-mono text-[#088395] font-bold">Slip Verified</div>
          </div>

          <div class="bg-[#FFFFFF] p-6 rounded-2xl border border-[#DFD9CC] shadow-sm flex flex-col justify-between">
            <div>
              <span class="w-8 h-8 rounded-lg bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-bold text-xs mb-4">03</span>
              <h4 class="font-headline-sm text-base text-[#111417] uppercase font-bold">3. Sublimation &amp; Sewing</h4>
              <p class="font-body-sm text-xs text-[#6B675E] mt-2">450 GSM poly-spandex printing, automated laser cutting, and 6-needle flatlock assembly.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] text-[11px] font-mono text-[#088395] font-bold">Deadline Assigned</div>
          </div>

          <div class="bg-[#FFFFFF] p-6 rounded-2xl border border-[#DFD9CC] shadow-sm flex flex-col justify-between">
            <div>
              <span class="w-8 h-8 rounded-lg bg-[#088395] text-white flex items-center justify-center font-bold text-xs mb-4">04</span>
              <h4 class="font-headline-sm text-base text-[#111417] uppercase font-bold">4. QC &amp; Door Delivery</h4>
              <p class="font-body-sm text-xs text-[#6B675E] mt-2">Full seam stress testing, barcode verification, and DHL express courier tracking.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-[#DFD9CC] text-[11px] font-mono text-[#088395] font-bold">DHL Global Express</div>
          </div>
        </div>

      </div>
    </section>

    <!-- 5. AI DESIGN STUDIO BANNER (Connected to Backup_of_ZAM FORWARD 123456.cdr) -->
    <section class="max-w-[1360px] mx-auto px-4 sm:px-8 w-full mb-20" id="custom-studio">
      <div class="bg-[#111417] text-[#F4F1EA] p-8 md:p-12 rounded-3xl shadow-xl relative overflow-hidden">
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
          <div class="lg:col-span-7 space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#088395]/20 text-[#088395] font-mono text-xs uppercase font-bold border border-[#088395]/40">
              <span class="material-symbols-outlined text-[16px]">view_in_ar</span>
              <span>CorelDraw (.CDR) 3D Sublimation Engine</span>
            </div>

            <h2 class="font-headline-lg text-3xl md:text-4xl text-[#F4F1EA] font-bold uppercase tracking-tight">
              AI 3D Studio &amp; CorelDraw Pattern Engine
            </h2>

            <p class="font-body-md text-sm md:text-base text-[#EDE8DE]/80 max-w-xl leading-relaxed">
              Powered directly by the master vector cut file <code class="px-2 py-0.5 rounded bg-[#191C1F] text-[#088395] font-mono font-bold text-xs">Backup_of_ZAM FORWARD 123456.cdr</code>. Customize flat 2D pattern pieces, place logos, type your team name, and view your design wrapped live in interactive <strong>360° 3D</strong>.
            </p>

            <div class="flex flex-wrap items-center gap-4 pt-2">
              <button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-lg bg-[#088395] text-white font-headline-sm text-xs uppercase font-bold tracking-wider hover:opacity-90 transition-opacity shadow-md flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
                <span>Open 3D Design Studio</span>
              </button>
              <a href="/uploads/templates/Backup_of_ZAM_FORWARD_123456.cdr" download class="px-5 py-3.5 rounded-lg bg-[#191C1F] text-[#F4F1EA] font-headline-sm text-xs uppercase font-bold tracking-wider hover:bg-[#22282E] transition-colors border border-[#75777B]/40 flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">download</span>
                <span>Download Master .CDR (36MB)</span>
              </a>
            </div>
          </div>

          <div class="lg:col-span-5 relative cursor-pointer" onclick="openAiStudioModal()">
            <div class="bg-[#191C1F] p-4 rounded-2xl border border-[#75777B]/30 shadow-2xl group hover:border-[#088395] transition-all">
              <div class="flex items-center justify-between pb-3 border-b border-[#75777B]/30 text-xs">
                <span class="font-mono text-[#088395] font-bold flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-[#088395] animate-pulse"></span>
                  MMA_FIGHT_SHORTS_123456.CDR
                </span>
                <span class="text-[10px] font-mono text-[#EDE8DE] uppercase">360° 3D Active</span>
              </div>
              <div class="py-6 flex items-center justify-center relative">
                <img src="/uploads/templates/zam_cdr_thumbnail.png" alt="CDR Thumbnail" class="h-44 object-contain group-hover:scale-105 transition-transform duration-500 drop-shadow-2xl"/>
              </div>
              <div class="pt-3 border-t border-[#75777B]/30 flex items-center justify-between text-xs text-[#EDE8DE]/70 font-mono">
                <span>Zones: Waistband, Left/Right Legs, Belt</span>
                <span class="text-[#088395] font-bold">Click to Launch →</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 6. LIVE ORDER TRACKER WIDGET (DESIGN.md ZAM-ID Verification) -->
    <section class="max-w-[1360px] mx-auto px-4 sm:px-8 w-full mb-20" id="tracking">
      <div class="bg-[#FFFFFF] p-6 sm:p-10 rounded-3xl border border-[#DFD9CC] shadow-sm">
        
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-8">
          <div>
            <span class="font-mono text-xs uppercase tracking-widest text-[#088395] font-bold flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-[#088395] animate-pulse"></span>
              Live Manufacturing Atelier • SQLite Engine Connected
            </span>
            <h2 class="font-headline-lg text-2xl sm:text-3xl text-[#111417] font-bold uppercase mt-1">Track Your Order Status (ZAM-ID)</h2>
            <p class="font-body-sm text-sm text-[#6B675E] mt-1">
              Check real-time factory milestones, sublimation status, or wire transfer invoice clearance.
            </p>

            <!-- Quick Demo Pills -->
            <div class="flex items-center gap-2 mt-3 text-xs">
              <span class="text-[#6B675E] font-medium font-mono uppercase text-[11px]">Quick Demo Orders:</span>
              <button onclick="lookupOrder('ZAM-401-26')" class="px-2.5 py-1 rounded bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] font-bold font-mono transition-colors">ZAM-401-26</button>
              <button onclick="lookupOrder('ZAM-402-26')" class="px-2.5 py-1 rounded bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] font-bold font-mono transition-colors">ZAM-402-26</button>
              <button onclick="lookupOrder('ZAM-405-26')" class="px-2.5 py-1 rounded bg-[#EDE8DE] text-[#111417] hover:bg-[#E5E2DB] font-bold font-mono transition-colors">ZAM-405-26</button>
            </div>
          </div>

          <div class="flex items-center gap-2 max-w-md w-full">
            <div class="relative flex-1">
              <span class="material-symbols-outlined absolute left-3 top-2.5 text-[#75777B] text-[20px]">search</span>
              <input id="trackingInput" class="w-full pl-10 pr-3 py-2.5 bg-[#EDE8DE] rounded-lg text-sm font-bold text-[#111417] focus:outline-none uppercase border border-[#DFD9CC] focus:border-[#088395] transition-all font-mono" type="text" value="ZAM-401-26" placeholder="Enter ZAM-xxx-26" onkeydown="if(event.key==='Enter') lookupOrder()"/>
            </div>
            <button onclick="lookupOrder()" class="px-5 py-2.5 bg-[#111417] text-[#F4F1EA] rounded-lg text-xs font-bold uppercase tracking-wider hover:bg-[#088395] transition-colors shadow-sm flex items-center gap-1.5 flex-shrink-0 font-headline-sm">
              <span>Lookup</span>
            </button>
          </div>
        </div>

        <!-- Tracking Result Display Container -->
        <div id="trackingResultContainer" class="bg-[#F6F3EC] rounded-2xl p-6 border border-[#DFD9CC] transition-all duration-300">
          <!-- Populated dynamically by lookupOrder() -->
        </div>

      </div>
    </section>

  </main>

  <!-- EDITORIAL FOOTER (DESIGN.md Level 0 Surface with Fine Sandstone Rule) -->
  <footer class="w-full bg-[#EDE8DE] pt-16 pb-12 border-t border-[#DFD9CC]">
    <div class="max-w-[1360px] mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 pb-12 border-b border-[#DFD9CC]">
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-[#111417] text-[#F4F1EA] flex items-center justify-center font-bold text-sm">ZF</div>
            <span class="font-headline-sm text-lg font-bold tracking-tight text-[#111417] uppercase">ZamForward Combat</span>
          </div>
          <p class="font-body-md text-xs text-[#6B675E] max-w-sm">
            High-performance combat apparel and technical sublimation manufacturing for Brazilian Jiu-Jitsu, MMA, and Muay Thai academies worldwide.
          </p>
          <div class="font-mono text-xs text-[#088395] font-bold">
            ● Batch 43 Atelier Production Active • Global Dispatch
          </div>
        </div>

        <div class="space-y-3">
          <h4 class="font-category-caps text-xs text-[#111417] uppercase font-bold">Equipment</h4>
          <ul class="space-y-2 font-body-sm text-xs text-[#6B675E]">
            <li><a href="#catalog" class="hover:text-[#111417]">MMA Fight Shorts</a></li>
            <li><a href="#catalog" class="hover:text-[#111417]">Ranked Rashguards</a></li>
            <li><a href="#catalog" class="hover:text-[#111417]">BJJ Gis &amp; Belts</a></li>
            <li><a href="#catalog" class="hover:text-[#111417]">Muay Thai Shorts</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <h4 class="font-category-caps text-xs text-[#111417] uppercase font-bold">Atelier Tools</h4>
          <ul class="space-y-2 font-body-sm text-xs text-[#6B675E]">
            <li><button onclick="openAiStudioModal()" class="hover:text-[#111417] text-left">AI 3D Garment Studio</button></li>
            <li><button onclick="openCdrTemplateVault()" class="hover:text-[#111417] text-left">Master CorelDraw Vault</button></li>
            <li><a href="#workflow" class="hover:text-[#111417]">4-Step Workflow Guide</a></li>
            <li><a href="#tracking" class="hover:text-[#111417]">ZAM-ID Order Tracker</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <h4 class="font-category-caps text-xs text-[#111417] uppercase font-bold">Wholesale</h4>
          <p class="font-body-sm text-xs text-[#6B675E]">Academy volume manufacturing and custom federation team kits.</p>
          <button onclick="openCustomOrderModal()" class="px-4 py-2 rounded-lg bg-[#111417] text-[#F4F1EA] text-xs font-bold uppercase hover:bg-[#088395] transition-colors">
            Contact Atelier
          </button>
        </div>
      </div>

      <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 font-body-sm text-xs text-[#6B675E]">
        <p>© 2026 ZamForward Combat Manufacturing. All rights reserved.</p>
        <div class="flex items-center gap-6">
          <a href="#" class="hover:text-[#111417]">Fabric Specs &amp; GSM Standards</a>
          <a href="#" class="hover:text-[#111417]">Privacy Policy</a>
          <a href="#" class="hover:text-[#111417]">Terms of Production</a>
        </div>
      </div>
    </div>
  </footer>
'''

full_html = head_content + editorial_body + modals_and_js

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Applied 100% DESIGN.md specification to public/index.html and code.html successfully.")
