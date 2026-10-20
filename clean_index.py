import re

# Read current public/index.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ----------------- 1. CLEAN HEADER NAVIGATION -----------------
clean_header = '''<header class="fixed top-0 w-full z-50 bg-surface/95 backdrop-blur-md border-b border-outline-variant/30 transition-all">
  <!-- Top Announcement Rail -->
  <div class="w-full bg-primary text-on-primary py-1.5 px-4 text-center font-label-md text-xs tracking-wider uppercase flex items-center justify-center gap-3">
    <span>Free Team Sample Swatch Kits &amp; Global Shipping on Orders over $250</span>
    <span class="opacity-40">•</span>
    <span class="text-secondary-fixed font-bold">Use Code ZAMCOMBAT</span>
    <span class="opacity-40 hidden md:inline">•</span>
    <span class="text-outline-variant hidden md:inline">Factory Direct Atelier</span>
  </div>

  <!-- Main Navbar -->
  <div class="h-18 max-w-[1360px] mx-auto px-4 md:px-8 flex items-center justify-between gap-4">
    <!-- Brand Logo -->
    <a href="#" class="flex items-center gap-2.5 flex-shrink-0 group">
      <div class="w-9 h-9 rounded-lg bg-primary text-on-primary flex items-center justify-center font-bold text-sm tracking-tighter group-hover:bg-secondary transition-colors">
        ZF
      </div>
      <div class="flex flex-col">
        <span class="font-headline-sm text-lg md:text-xl font-bold tracking-tight text-primary uppercase leading-tight">ZamForward</span>
        <span class="text-[10px] uppercase tracking-widest text-secondary font-bold -mt-0.5">Combat Atelier</span>
      </div>
    </a>

    <!-- Center Nav Links (Clean, Single Line, No Wrapping) -->
    <nav class="hidden lg:flex items-center gap-1 xl:gap-2">
      <a href="#" class="px-3 py-1.5 rounded-lg text-primary font-title-sm text-sm font-semibold hover:bg-surface-container transition-colors">Home</a>
      <a href="#catalog" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors">Catalog</a>
      <button onclick="openCustomOrderModal()" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors flex items-center gap-1">
        <span>Custom Studio</span>
        <span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
      </button>
      <a href="#tracking" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors">Order Tracker</a>
      <button onclick="openCdrTemplateVault()" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors">CDR Templates</button>
      <a href="#workflow" class="px-3 py-1.5 rounded-lg text-on-surface-variant font-title-sm text-sm font-medium hover:text-primary hover:bg-surface-container transition-colors">Workflow</a>
    </nav>

    <!-- Right Utility Actions -->
    <div class="flex items-center gap-3">
      <!-- Search Input -->
      <div class="hidden md:flex items-center bg-surface-container-low px-3 py-1.5 rounded-lg border border-outline-variant/30 focus-within:border-secondary transition-all">
        <span class="material-symbols-outlined text-outline text-[18px] mr-2">search</span>
        <input class="bg-transparent text-primary placeholder:text-outline text-xs font-body-sm focus:outline-none w-28 xl:w-40" placeholder="Search rashguards, Gis..." type="text"/>
      </div>

      <!-- Quick Action: Order Mockup -->
      <button onclick="openCustomOrderModal()" class="hidden sm:inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-secondary text-on-secondary font-label-md text-xs uppercase font-bold hover:opacity-90 transition-opacity shadow-sm">
        <span class="material-symbols-outlined text-[16px]">add_circle</span>
        <span>Custom Kit</span>
      </button>

      <!-- Account / Sign In -->
      <button onclick="openAuthModal()" class="flex items-center gap-2 pl-1 hover:opacity-90 transition-opacity text-left">
        <img alt="Profile" class="w-8 h-8 rounded-full object-cover ring-2 ring-secondary/30" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBkWmebPefwv2j9HM8pQzfJCt9GwqQwJnmH7m-9Gcf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ"/>
        <span id="headerUserLabel" class="hidden xl:inline-block font-title-sm text-xs text-primary font-semibold">Sign In</span>
      </button>

      <!-- Staff Console Drawer Shortcut -->
      <button onclick="toggleStaffDrawer()" title="Open Staff Console" class="w-8 h-8 rounded-lg bg-surface-container flex items-center justify-center text-primary hover:bg-primary hover:text-on-primary transition-colors">
        <span class="material-symbols-outlined text-[18px]">admin_panel_settings</span>
      </button>
    </div>
  </div>
</header>'''

# Replace header in html
html = re.sub(r'<header.*?</header>', clean_header, html, flags=re.DOTALL)

# ----------------- 2. CLEAN, SPACIOUS, HERO SECTION -----------------
clean_hero = '''<!-- 1. HERO SECTION (Clean, Spacious Architectural Layout) -->
<section class="max-w-[1360px] mx-auto px-4 md:px-8 w-full pt-6 pb-16">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
    
    <!-- Left Column: Copy & High-Impact Value Proposition (7 Cols) -->
    <div class="lg:col-span-7 flex flex-col justify-center space-y-6">
      
      <!-- Atelier Badge -->
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-surface-container-high text-secondary font-label-md text-xs uppercase tracking-wider w-fit border border-outline-variant/30">
        <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
        <span class="font-bold">Official BJJ &amp; MMA Custom Apparel Atelier</span>
      </div>

      <!-- Main Master Headline -->
      <div class="space-y-1">
        <h1 class="font-display-hero text-4xl sm:text-5xl lg:text-6xl text-primary font-extrabold uppercase tracking-tight leading-[1.08]">
          Engineered for Combat.
        </h1>
        <h1 class="font-display-hero text-4xl sm:text-5xl lg:text-6xl text-secondary font-extrabold uppercase tracking-tight leading-[1.08] flex items-center gap-3">
          Built for Champions
          <span class="material-symbols-outlined text-[36px] sm:text-[48px] text-secondary">verified</span>
        </h1>
      </div>

      <!-- Crisp Editorial Subtitle -->
      <p class="font-body-lg text-base sm:text-lg text-on-surface-variant max-w-2xl leading-relaxed">
        High-performance custom sublimated rashguards, IBJJF-compliant Gis, and competition shorts engineered for fight academies worldwide. Zero minimums on bespoke team kits, 50% milestone deposits, and rapid global delivery.
      </p>

      <!-- Primary Action CTAs -->
      <div class="flex flex-wrap items-center gap-3 pt-2">
        <button onclick="openCustomOrderModal()" class="px-6 py-3.5 rounded-xl bg-primary text-on-primary font-label-lg text-sm uppercase font-bold hover:bg-primary-container transition-all shadow-md flex items-center gap-2 group">
          <span class="material-symbols-outlined text-[18px] group-hover:rotate-45 transition-transform">brush</span>
          <span>Start Custom Kit Order</span>
        </button>
        <a href="#tracking" class="px-5 py-3.5 rounded-xl bg-surface-container text-primary font-label-lg text-sm uppercase font-bold hover:bg-surface-container-highest transition-colors border border-outline-variant/40 flex items-center gap-2">
          <span class="material-symbols-outlined text-[18px] text-secondary">track_changes</span>
          <span>Track Order (ZAM-ID)</span>
        </a>
        <button onclick="openCdrTemplateVault()" class="px-4 py-3.5 rounded-xl bg-transparent text-on-surface-variant font-label-lg text-xs uppercase font-bold hover:text-primary transition-colors flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">draft</span>
          <span>CDR Templates</span>
        </button>
      </div>

      <!-- Clean Social Proof & Metric Badges Strip -->
      <div class="pt-4 border-t border-outline-variant/30 grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div>
          <div class="font-headline-sm text-xl font-bold text-primary">50,000+</div>
          <div class="text-xs text-on-surface-variant">Athletes Geared</div>
        </div>
        <div>
          <div class="font-headline-sm text-xl font-bold text-secondary">450 GSM</div>
          <div class="text-xs text-on-surface-variant">Sublimated Poly-Spandex</div>
        </div>
        <div>
          <div class="font-headline-sm text-xl font-bold text-primary">IBJJF Legal</div>
          <div class="text-xs text-on-surface-variant">5 Belt Ranks Supported</div>
        </div>
        <div>
          <div class="flex text-amber-500 items-center">
            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">star</span>
            <span class="material-symbols-outlined text-[16px]" style="font-variation-settings: 'FILL' 1;">star</span>
          </div>
          <div class="text-xs text-on-surface-variant">500+ Fight Gyms</div>
        </div>
      </div>

    </div>

    <!-- Right Column: Hero High-Res Product Spotlight (5 Cols, Clean & Unobstructed) -->
    <div class="lg:col-span-5 relative">
      <div class="relative rounded-2xl overflow-hidden shadow-xl bg-surface-container-low border border-outline-variant/40 group">
        
        <!-- Main Athlete Image (Clean, No Clashing Text Over Fighter) -->
        <div class="aspect-[4/5] w-full overflow-hidden relative">
          <img class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-105" 
               alt="Athlete wearing ZamForward custom sublimated rashguard" 
               src="https://lh3.googleusercontent.com/aida-public/AB6AXuB0bh0920oDUW-DNllDkVgJHiLrVgCYZ1U9cpr5N63qaBsUAtRT3sFYzf9BVo3te9auHuUQN7s4M4SvKVBOjYOP6Qj6lb4U1-Tzh9OAsOZOuRxyOIVWldqggpafh8WCojkZKWozMX2EuTcS5LLeG804jVS_l-8ysyiLJmRx41ByWm7fks1csoTcV0MK1jokTkVCpcpPxJeYvTpTqqej6O26WVpjeSWahMf_SCPs8MjdrTD2rDDzkaw"/>
          
          <!-- Top Floating Tag -->
          <div class="absolute top-4 left-4 z-10">
            <span class="px-3 py-1 rounded-full bg-primary/80 backdrop-blur-md text-on-primary font-mono text-[11px] uppercase font-bold tracking-wider flex items-center gap-1.5 shadow-sm">
              <span class="w-2 h-2 rounded-full bg-secondary animate-ping"></span>
              <span>Batch 43 Production Active</span>
            </span>
          </div>

          <!-- Top-Right Trust Badge -->
          <div class="absolute top-4 right-4 z-10">
            <span class="px-2.5 py-1 rounded-lg bg-surface/90 backdrop-blur-md text-primary font-label-md text-[11px] font-bold uppercase shadow-sm">
              6-Needle Flatlock
            </span>
          </div>
        </div>

        <!-- Clean Bottom Spec Strip (Outside Fighter's Face/Body) -->
        <div class="p-5 bg-surface-container-lowest border-t border-outline-variant/30 flex items-center justify-between gap-4">
          <div>
            <span class="text-[10px] uppercase tracking-wider font-bold text-secondary">Featured Product</span>
            <h4 class="font-title-md text-base text-primary font-bold uppercase">Apex Pro Compression Rashguard</h4>
            <p class="text-xs text-on-surface-variant">450 GSM Sublimated Poly-Spandex • Anti-slip silicone waist</p>
          </div>
          <button onclick="openCustomOrderModal(1)" class="px-3.5 py-2 rounded-lg bg-primary text-on-primary font-label-md text-xs uppercase font-bold hover:bg-secondary transition-colors whitespace-nowrap flex items-center gap-1">
            <span>Configure</span>
            <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
          </button>
        </div>

      </div>
    </div>

  </div>
</section>'''

# Replace Hero Section
html = re.sub(
    r'<!-- 1\. HERO SECTION.*?<!-- 2\. CATEGORY QUICK MARQUEE',
    clean_hero + '\n<!-- 2. CATEGORY QUICK MARQUEE',
    html,
    flags=re.DOTALL
)

# ----------------- 3. CLEAN CATEGORY MARQUEE & PILLS -----------------
clean_category_section = '''<!-- 2. CATEGORY QUICK MARQUEE & VALUE TILES (Clean & Cohesive) -->
<section class="w-full bg-surface-container-low/70 py-6 mb-16 border-y border-outline-variant/30">
  <div class="max-w-[1360px] mx-auto px-4 md:px-8">
    
    <!-- Clean Horizontal Category Strip -->
    <div class="flex items-center justify-between gap-3 overflow-x-auto pb-2 no-scrollbar">
      <a class="flex items-center gap-2.5 px-4 py-2 bg-surface-container-lowest rounded-xl whitespace-nowrap hover:bg-primary hover:text-on-primary transition-all shadow-sm border border-outline-variant/20 font-category-caps text-xs uppercase font-bold" href="#catalog">
        <span class="material-symbols-outlined text-[18px] text-secondary">fitness_center</span>
        <span>Rashguards</span>
      </a>
      <a class="flex items-center gap-2.5 px-4 py-2 bg-surface-container-lowest rounded-xl whitespace-nowrap hover:bg-primary hover:text-on-primary transition-all shadow-sm border border-outline-variant/20 font-category-caps text-xs uppercase font-bold" href="#catalog">
        <span class="material-symbols-outlined text-[18px] text-secondary">sports_mma</span>
        <span>MMA Fight Shorts</span>
      </a>
      <a class="flex items-center gap-2.5 px-4 py-2 bg-surface-container-lowest rounded-xl whitespace-nowrap hover:bg-primary hover:text-on-primary transition-all shadow-sm border border-outline-variant/20 font-category-caps text-xs uppercase font-bold" href="#catalog">
        <span class="material-symbols-outlined text-[18px] text-secondary">military_tech</span>
        <span>BJJ Gis &amp; Belts</span>
      </a>
      <a class="flex items-center gap-2.5 px-4 py-2 bg-surface-container-lowest rounded-xl whitespace-nowrap hover:bg-primary hover:text-on-primary transition-all shadow-sm border border-outline-variant/20 font-category-caps text-xs uppercase font-bold" href="#catalog">
        <span class="material-symbols-outlined text-[18px] text-secondary">sports_kabaddi</span>
        <span>Muay Thai Retro</span>
      </a>
      <a class="flex items-center gap-2.5 px-4 py-2 bg-surface-container-lowest rounded-xl whitespace-nowrap hover:bg-primary hover:text-on-primary transition-all shadow-sm border border-outline-variant/20 font-category-caps text-xs uppercase font-bold" href="#catalog">
        <span class="material-symbols-outlined text-[18px] text-secondary">accessibility_new</span>
        <span>Compression Spats</span>
      </a>
      <button onclick="openCustomOrderModal()" class="flex items-center gap-2.5 px-4 py-2 bg-secondary text-on-secondary rounded-xl whitespace-nowrap hover:opacity-90 transition-all shadow-sm font-category-caps text-xs uppercase font-bold">
        <span class="material-symbols-outlined text-[18px]">palette</span>
        <span>Custom Team Mockup</span>
      </button>
    </div>

    <!-- 4 Clean Value Proposition Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
      <div class="bg-surface-container-lowest p-4 rounded-xl flex items-center gap-3 shadow-sm border border-outline-variant/20">
        <div class="w-10 h-10 rounded-xl bg-surface-container flex items-center justify-center text-secondary flex-shrink-0">
          <span class="material-symbols-outlined text-[20px]">timer</span>
        </div>
        <div>
          <h5 class="font-title-sm text-xs text-primary uppercase font-bold">Guaranteed Lead-Time</h5>
          <p class="font-body-sm text-[11px] text-on-surface-variant">60-day complete production run</p>
        </div>
      </div>

      <div class="bg-surface-container-lowest p-4 rounded-xl flex items-center gap-3 shadow-sm border border-outline-variant/20">
        <div class="w-10 h-10 rounded-xl bg-surface-container flex items-center justify-center text-secondary flex-shrink-0">
          <span class="material-symbols-outlined text-[20px]">payments</span>
        </div>
        <div>
          <h5 class="font-title-sm text-xs text-primary uppercase font-bold">50% Milestone Invoicing</h5>
          <p class="font-body-sm text-[11px] text-on-surface-variant">Clear deposit on wire slip upload</p>
        </div>
      </div>

      <div class="bg-surface-container-lowest p-4 rounded-xl flex items-center gap-3 shadow-sm border border-outline-variant/20">
        <div class="w-10 h-10 rounded-xl bg-surface-container flex items-center justify-center text-secondary flex-shrink-0">
          <span class="material-symbols-outlined text-[20px]">architecture</span>
        </div>
        <div>
          <h5 class="font-title-sm text-xs text-primary uppercase font-bold">Corel (.CDR) Vector Suite</h5>
          <p class="font-body-sm text-[11px] text-on-surface-variant">Direct vector cut &amp; zone markup</p>
        </div>
      </div>

      <div class="bg-surface-container-lowest p-4 rounded-xl flex items-center gap-3 shadow-sm border border-outline-variant/20">
        <div class="w-10 h-10 rounded-xl bg-surface-container flex items-center justify-center text-secondary flex-shrink-0">
          <span class="material-symbols-outlined text-[20px]">local_shipping</span>
        </div>
        <div>
          <h5 class="font-title-sm text-xs text-primary uppercase font-bold">Real-Time ZAM-ID</h5>
          <p class="font-body-sm text-[11px] text-on-surface-variant">Factory milestone &amp; DHL tracking</p>
        </div>
      </div>
    </div>

  </div>
</section>'''

# Replace Category section
html = re.sub(
    r'<!-- 2\. CATEGORY QUICK MARQUEE.*?<!-- 3\. BEST SELLERS',
    clean_category_section + '\n<!-- 3. BEST SELLERS',
    html,
    flags=re.DOTALL
)

# ----------------- 4. CLEAN THE FLOATING STAFF BUTTON -----------------
# Replace the old large intrusive pill with a sleek, compact floating button that doesn't overlap
old_floating = '''<!-- FLOATING TRIGGER PILL FOR STAFF OPERATIONS -->
<div class="fixed bottom-6 right-6 z-40">
  <button onclick="toggleStaffDrawer()" class="px-4 py-2.5 rounded-full bg-primary text-on-primary font-label-md text-label-md uppercase tracking-wider shadow-xl hover:bg-primary-container transition-all flex items-center gap-2 border border-outline-variant/30">
    <span class="w-2.5 h-2.5 rounded-full bg-secondary animate-ping"></span>
    <span class="material-symbols-outlined text-[18px]">manufacturing</span>
    <span>Staff Atelier Console</span>
  </button>
</div>'''

clean_floating = '''<!-- FLOATING TRIGGER PILL FOR STAFF OPERATIONS -->
<div class="fixed bottom-5 right-5 z-40">
  <button onclick="toggleStaffDrawer()" class="px-3.5 py-2 rounded-full bg-primary/95 backdrop-blur-md text-on-primary font-label-md text-xs uppercase tracking-wider shadow-xl hover:bg-secondary transition-all flex items-center gap-2 border border-outline-variant/40 hover:scale-105">
    <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
    <span class="material-symbols-outlined text-[16px]">tune</span>
    <span class="font-bold">Atelier Console</span>
  </button>
</div>'''

html = html.replace(old_floating, clean_floating)

# Write to public/index.html
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("public/index.html cleaned up with modern, spacious, non-cluttered design!")
