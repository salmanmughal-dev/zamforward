import re

# Read current public/index.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Fonts in <head> to Inter & Plus Jakarta Sans (warm, friendly, modern, normal casing)
friendly_head_fonts = '''<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>'''

# Replace font links
html = re.sub(r'<link href="https://fonts\.googleapis\.com".*?display=swap" rel="stylesheet"/>', friendly_head_fonts, html)

# Update Tailwind config to prioritize Plus Jakarta Sans & Inter for clean, human readability
tailwind_config_fix = '''<script id="tailwind-config">tailwind.config = {
    darkMode: "class",
    theme: {
      extend: {
        "colors": {
          "primary": "#0f172a",
          "primary-container": "#1e293b",
          "secondary": "#0284c7",
          "secondary-container": "#e0f2fe",
          "on-secondary-container": "#0369a1",
          "surface": "#f8fafc",
          "surface-container-lowest": "#ffffff",
          "surface-container-low": "#f1f5f9",
          "surface-container": "#e2e8f0",
          "surface-container-high": "#cbd5e1",
          "surface-container-highest": "#94a3b8",
          "on-surface": "#0f172a",
          "on-surface-variant": "#475569",
          "outline": "#94a3b8",
          "outline-variant": "#e2e8f0"
        },
        "fontFamily": {
          "sans": ["Plus Jakarta Sans", "Inter", "system-ui", "sans-serif"],
          "display": ["Plus Jakarta Sans", "Inter", "sans-serif"],
          "body": ["Plus Jakarta Sans", "Inter", "sans-serif"]
        }
      }
    }
  };</script>'''

html = re.sub(r'<script id="tailwind-config">.*?</script>', tailwind_config_fix, html, flags=re.DOTALL)

# 2. Friendly, Simple Navigation Header
friendly_header = '''<header class="fixed top-0 w-full z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all">
  <!-- Friendly Top Announcement -->
  <div class="w-full bg-slate-900 text-white py-1.5 px-4 text-center text-xs font-medium flex items-center justify-center gap-2 sm:gap-4">
    <span>✨ Free 3D Design Preview &amp; Worldwide Team Delivery</span>
    <span class="opacity-40">•</span>
    <span class="text-sky-300 font-semibold">No Minimum Order Quantity</span>
    <span class="opacity-40 hidden sm:inline">•</span>
    <span class="text-slate-300 hidden sm:inline">Easy Online Ordering</span>
  </div>

  <!-- Main Navbar -->
  <div class="h-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between gap-4">
    <!-- Brand Logo -->
    <a href="#" class="flex items-center gap-2.5 flex-shrink-0 group">
      <div class="w-9 h-9 rounded-xl bg-sky-600 text-white flex items-center justify-center font-extrabold text-base shadow-sm group-hover:bg-slate-900 transition-colors">
        ZF
      </div>
      <div class="flex flex-col">
        <span class="text-lg font-bold tracking-tight text-slate-900 leading-tight">ZamForward</span>
        <span class="text-[11px] font-medium text-sky-600 -mt-0.5">Custom Fight Gear</span>
      </div>
    </a>

    <!-- Center Navigation Links (Clean, Normal Casing, Friendly) -->
    <nav class="hidden md:flex items-center gap-1 lg:gap-2">
      <a href="#" class="px-3 py-2 rounded-lg text-sm font-semibold text-slate-900 hover:bg-slate-100 transition-colors">Home</a>
      <button onclick="openAiStudioModal()" class="px-3 py-2 rounded-lg text-sm font-bold text-sky-600 hover:bg-sky-50 transition-colors flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
        <span>Custom 3D Builder</span>
      </button>
      <a href="#how-it-works" class="px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors">How It Works</a>
      <a href="#catalog" class="px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors">Shop Gear</a>
      <a href="#tracking" class="px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors">Track Order</a>
    </nav>

    <!-- Right Actions -->
    <div class="flex items-center gap-3">
      <!-- Big Friendly Start Designing CTA -->
      <button onclick="openAiStudioModal()" class="px-4 py-2 rounded-xl bg-sky-600 text-white text-xs sm:text-sm font-bold hover:bg-sky-700 transition-all shadow-sm flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">palette</span>
        <span>Design in 3D</span>
      </button>

      <!-- Account / Sign In -->
      <button onclick="openAuthModal()" class="flex items-center gap-2 pl-2 text-slate-700 hover:text-slate-900 text-xs sm:text-sm font-medium">
        <div class="w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-600 border border-slate-200">
          <span class="material-symbols-outlined text-[18px]">person</span>
        </div>
        <span id="headerUserLabel" class="hidden xl:inline">Sign In</span>
      </button>
    </div>
  </div>
</header>'''

html = re.sub(r'<header.*?</header>', friendly_header, html, flags=re.DOTALL)

# 3. Friendly, Welcoming Hero Section
friendly_hero = '''<!-- 1. HERO SECTION (Friendly, Clear, Intuitive for Everyone) -->
<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-16">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
    
    <!-- Left Column: Simple, Clear Value Proposition (7 Cols) -->
    <div class="lg:col-span-7 space-y-6">
      
      <!-- Friendly Pill -->
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-sky-50 text-sky-700 text-xs font-semibold border border-sky-200/60">
        <span class="w-2 h-2 rounded-full bg-sky-500 animate-pulse"></span>
        <span>Custom Fight Apparel Made Simple</span>
      </div>

      <!-- Main Headline (Friendly, Clear, Normal Human Casing) -->
      <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 tracking-tight leading-[1.15]">
        Design Custom Fight Gear for Your Gym or Team.
      </h1>

      <!-- Simple Subtitle in Plain English -->
      <p class="text-base sm:text-lg text-slate-600 max-w-2xl leading-relaxed">
        Create custom MMA shorts, rashguards, and BJJ Gis in minutes with our easy 3D designer. Upload your gym logo, choose your colors, and get high-quality gear made and shipped right to your door.
      </p>

      <!-- Primary Action Buttons (Intuitive, Simple) -->
      <div class="flex flex-wrap items-center gap-3 pt-1">
        <button onclick="openAiStudioModal()" class="px-6 py-3.5 rounded-xl bg-sky-600 text-white text-sm font-bold hover:bg-sky-700 transition-all shadow-md hover:shadow-lg flex items-center gap-2 group">
          <span class="material-symbols-outlined text-[20px] group-hover:scale-110 transition-transform">auto_fix_high</span>
          <span>Start Designing in 3D (Free)</span>
        </button>
        
        <a href="#tracking" class="px-5 py-3.5 rounded-xl bg-slate-100 text-slate-800 text-sm font-semibold hover:bg-slate-200 transition-colors flex items-center gap-2 border border-slate-200">
          <span class="material-symbols-outlined text-[18px] text-slate-500">search</span>
          <span>Track My Order</span>
        </a>
      </div>

      <!-- Trust Badges (Plain English, Normal People) -->
      <div class="pt-4 border-t border-slate-200 grid grid-cols-2 sm:grid-cols-4 gap-4 text-slate-700">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-sky-600 text-[20px]">check_circle</span>
          <span class="text-xs font-semibold">No Minimums</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-sky-600 text-[20px]">view_in_ar</span>
          <span class="text-xs font-semibold">Live 3D Preview</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-sky-600 text-[20px]">local_shipping</span>
          <span class="text-xs font-semibold">Worldwide Delivery</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-sky-600 text-[20px]">verified</span>
          <span class="text-xs font-semibold">500+ Gyms Trust Us</span>
        </div>
      </div>

    </div>

    <!-- Right Column: Interactive 3D Teaser Card (5 Cols) -->
    <div class="lg:col-span-5">
      <div class="bg-gradient-to-b from-slate-50 to-slate-100 rounded-3xl p-6 border border-slate-200 shadow-xl relative overflow-hidden group">
        
        <!-- Top Status Tag -->
        <div class="flex items-center justify-between pb-4 border-b border-slate-200 text-xs">
          <div class="flex items-center gap-2 font-bold text-slate-800">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
            <span>Easy 3D Customizer</span>
          </div>
          <span class="px-2.5 py-1 rounded-full bg-sky-100 text-sky-700 font-bold text-[11px]">Ready in 3 Steps</span>
        </div>

        <!-- Visual Preview -->
        <div class="py-6 flex flex-col items-center justify-center relative cursor-pointer" onclick="openAiStudioModal()">
          <img src="/uploads/templates/zam_cdr_thumbnail.png" alt="Fight Shorts Design Preview" class="h-48 object-contain drop-shadow-lg group-hover:scale-105 transition-transform duration-500"/>
          
          <!-- Helpful Click Hint -->
          <div class="mt-4 px-4 py-2 rounded-xl bg-slate-900 text-white text-xs font-bold shadow-md flex items-center gap-2 group-hover:bg-sky-600 transition-colors">
            <span class="material-symbols-outlined text-[18px]">touch_app</span>
            <span>Click to Open 3D Designer</span>
          </div>
        </div>

        <!-- 3 Simple Friendly Steps Pill Bar -->
        <div class="pt-4 border-t border-slate-200 grid grid-cols-3 gap-2 text-center text-xs">
          <div class="p-2 rounded-xl bg-white shadow-sm border border-slate-100">
            <span class="block font-bold text-slate-900">1. Colors</span>
            <span class="text-[11px] text-slate-500">Pick fabric</span>
          </div>
          <div class="p-2 rounded-xl bg-white shadow-sm border border-slate-100">
            <span class="block font-bold text-slate-900">2. Logo</span>
            <span class="text-[11px] text-slate-500">Upload art</span>
          </div>
          <div class="p-2 rounded-xl bg-white shadow-sm border border-slate-100">
            <span class="block font-bold text-slate-900">3. Order</span>
            <span class="text-[11px] text-slate-500">Shipped fast</span>
          </div>
        </div>

      </div>
    </div>

  </div>
</section>'''

html = re.sub(
    r'<!-- 1\. HERO SECTION.*?<!-- 2\. CATEGORY QUICK MARQUEE',
    friendly_hero + '\n<!-- 2. CATEGORY QUICK MARQUEE',
    html,
    flags=re.DOTALL
)

# 4. Friendly "How It Works" in 3 Simple Steps
friendly_how_it_works = '''<!-- 2. HOW IT WORKS (Simple, Plain English for Non-Technical Users) -->
<section class="w-full bg-slate-50 py-16 border-y border-slate-200" id="how-it-works">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center max-w-2xl mx-auto mb-12">
      <span class="text-xs font-bold uppercase tracking-wider text-sky-600 bg-sky-50 px-3 py-1 rounded-full border border-sky-100">Simple 3-Step Process</span>
      <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mt-3">How Custom Ordering Works</h2>
      <p class="text-sm sm:text-base text-slate-600 mt-2">You don't need any design skills. Our interactive 3D builder makes it easy for anyone.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Step 1 -->
      <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative group hover:border-sky-300 transition-all">
        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-lg mb-4">
          1
        </div>
        <h3 class="text-base font-bold text-slate-900 mb-1">Pick Gear &amp; Colors</h3>
        <p class="text-xs text-slate-600 leading-relaxed">Choose MMA shorts, rashguards, or BJJ Gis, and select your favorite team colors with one click.</p>
      </div>

      <!-- Step 2 -->
      <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative group hover:border-sky-300 transition-all">
        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-lg mb-4">
          2
        </div>
        <h3 class="text-base font-bold text-slate-900 mb-1">Add Logo &amp; See in 3D</h3>
        <p class="text-xs text-slate-600 leading-relaxed">Upload your gym logo, type your team name, and spin the 3D model to see exactly how it looks.</p>
      </div>

      <!-- Step 3 -->
      <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative group hover:border-sky-300 transition-all">
        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-lg mb-4">
          3
        </div>
        <h3 class="text-base font-bold text-slate-900 mb-1">We Craft &amp; Deliver</h3>
        <p class="text-xs text-slate-600 leading-relaxed">Confirm your order with 50% deposit. Our factory crafts your gear and ships it directly to your door.</p>
      </div>

    </div>

    <!-- Quick Launch Bar -->
    <div class="mt-12 text-center">
      <button onclick="openAiStudioModal()" class="px-6 py-3 rounded-xl bg-slate-900 text-white font-bold text-sm hover:bg-sky-600 transition-colors shadow-sm inline-flex items-center gap-2">
        <span class="material-symbols-outlined text-[18px]">play_circle</span>
        <span>Try the 3D Designer Now</span>
      </button>
    </div>

  </div>
</section>'''

html = re.sub(
    r'<!-- 2\. CATEGORY QUICK MARQUEE.*?<!-- 3\. BEST SELLERS',
    friendly_how_it_works + '\n<!-- 3. BEST SELLERS',
    html,
    flags=re.DOTALL
)

# 5. Simplify Catalog Section (Clean normal text, friendly buttons)
catalog_header_friendly = '''<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16" id="catalog">
  <div class="text-center max-w-xl mx-auto mb-10">
    <span class="text-xs font-bold uppercase tracking-wider text-sky-600 bg-sky-50 px-3 py-1 rounded-full border border-sky-100">Quality Gear</span>
    <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2">Popular Custom Fight Apparel</h2>
    <p class="text-sm text-slate-600 mt-1">Select any item to customize in 3D with your gym logo.</p>
  </div>'''

html = re.sub(
    r'<section class="max-w-\[1360px\] mx-auto px-margin-mobile md:px-margin w-full mb-space-3xl" id="catalog">.*?<!-- Product Grid 3x2 -->',
    catalog_header_friendly + '\n<!-- Product Grid 3x2 -->',
    html,
    flags=re.DOTALL
)

# 6. Simplify Order Tracker Section (Non-Technical, Easy for Normal People)
friendly_tracker = '''<!-- 8. RECENT ORDERS LIVE TRACKER WIDGET (Easy for Normal People) -->
<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16" id="tracking">
  <div class="bg-white p-6 sm:p-10 rounded-3xl border border-slate-200 shadow-lg">
    
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-8">
      <div>
        <span class="text-xs font-bold uppercase tracking-wider text-sky-600 bg-sky-50 px-3 py-1 rounded-full border border-sky-100 flex items-center gap-1.5 w-fit">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          Live Order Tracking
        </span>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2">Track Your Order Status</h2>
        <p class="text-sm text-slate-600 mt-1">
          Enter your Order Number below to check production progress and tracking updates.
        </p>

        <!-- Quick Demo Orders -->
        <div class="flex items-center gap-2 mt-3 text-xs">
          <span class="text-slate-500 font-medium">Try a demo order:</span>
          <button onclick="lookupOrder('ZAM-401-26')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 hover:bg-slate-200 font-bold font-mono transition-colors">ZAM-401-26</button>
          <button onclick="lookupOrder('ZAM-402-26')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 hover:bg-slate-200 font-bold font-mono transition-colors">ZAM-402-26</button>
          <button onclick="lookupOrder('ZAM-405-26')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 hover:bg-slate-200 font-bold font-mono transition-colors">ZAM-405-26</button>
        </div>
      </div>

      <div class="flex items-center gap-2 max-w-md w-full">
        <div class="relative flex-1">
          <span class="material-symbols-outlined absolute left-3 top-2.5 text-slate-400 text-[20px]">search</span>
          <input id="trackingInput" class="w-full pl-10 pr-3 py-2.5 bg-slate-50 rounded-xl text-sm font-semibold text-slate-900 focus:outline-none uppercase border border-slate-200 focus:border-sky-500 transition-all" type="text" value="ZAM-401-26" placeholder="Enter ZAM-xxx-26" onkeydown="if(event.key==='Enter') lookupOrder()"/>
        </div>
        <button onclick="lookupOrder()" class="px-5 py-2.5 bg-sky-600 text-white rounded-xl text-xs sm:text-sm font-bold hover:bg-sky-700 transition-colors shadow-sm flex items-center gap-1.5 flex-shrink-0">
          <span>Find Order</span>
        </button>
      </div>
    </div>

    <!-- Tracking Result Display -->
    <div id="trackingResultContainer" class="bg-slate-50 rounded-2xl p-6 border border-slate-200 transition-all duration-300">
      <!-- Populated dynamically by lookupOrder() -->
    </div>

  </div>
</section>'''

html = re.sub(
    r'<!-- 8\. RECENT ORDERS LIVE TRACKER WIDGET.*?<!-- 9\. WHOLESALE',
    friendly_tracker + '\n<!-- 9. WHOLESALE',
    html,
    flags=re.DOTALL
)

# 7. Update AI Studio Modal with Normal-Person Friendly Copy & Tips
html = html.replace(
    'MMA Fight Shorts Cut &amp; Sew Blueprint',
    'Custom MMA Fight Shorts — Click &amp; Drag Any Logo or Text to Move It'
)
html = html.replace(
    'Live 3D Garment View',
    'Interactive 3D Preview (Drag to spin)'
)
html = html.replace(
    'CorelDraw Vector Pattern',
    'Easy Customizer'
)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("public/index.html updated with friendly, human, non-technical UI!")
