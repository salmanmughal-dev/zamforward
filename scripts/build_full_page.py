import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

# 1. Load Navbar CSS
with open('scripts/navbar_component.css', 'r', encoding='utf-8') as f:
    nav_css = f.read().strip()

# Strip demo filler from CSS
nav_css = re.sub(r'/\*\s*Demo page filler\s*\*/.*$', '', nav_css, flags=re.DOTALL).strip()

# 2. Load Navbar HTML
with open('scripts/navbar_component.html', 'r', encoding='utf-8') as f:
    nav_html = f.read().strip()

# 3. Enhance nav_html with proper hooks to existing modal triggers and tracking
# Replace href="#" on CTA with openAiStudioModal()
nav_html = nav_html.replace(
    '<a class="cta" href="#">',
    '<a class="cta" href="#" onclick="openAiStudioModal(); return false;">'
)

# In mega menu feat card:
nav_html = nav_html.replace(
    '<a class="feat" href="#">',
    '<a class="feat" href="#" onclick="openAiStudioModal(); return false;">'
)

# AI 3D Studio nav links
nav_html = nav_html.replace(
    '<a class="nl" href="#"><svg class="i sparkle"><use href="#i-spark"/></svg>AI 3D Studio',
    '<a class="nl" href="#" onclick="openAiStudioModal(); return false;"><svg class="i sparkle"><use href="#i-spark"/></svg>AI 3D Studio'
)

# CDR Vault nav links
nav_html = nav_html.replace(
    '<a class="nl" href="#"><svg class="i"><use href="#i-vault"/></svg>CDR Vault</a>',
    '<a class="nl" href="#" onclick="openCdrTemplateVault(); return false;"><svg class="i"><use href="#i-vault"/></svg>CDR Vault</a>'
)

# Workflow nav links
nav_html = nav_html.replace(
    '<a class="nl" href="#"><svg class="i"><use href="#i-flow"/></svg>Workflow</a>',
    '<a class="nl" href="#workflow"><svg class="i"><use href="#i-flow"/></svg>Workflow</a>'
)

# Cart checkout button
nav_html = nav_html.replace(
    '<a class="btn p" href="#">Proceed to checkout</a>',
    '<a class="btn p" href="#" onclick="openCustomOrderModal(); drawer(cart, false); return false;">Proceed to checkout</a>'
)

# Mobile drawer "Start Designing"
nav_html = nav_html.replace(
    '<a class="btn p" href="#"><svg class="i" style="color:#7fdbe8"><use href="#i-spark"/></svg>Start Designing</a>',
    '<a class="btn p" href="#" onclick="openAiStudioModal(); drawer(mnav, false); return false;"><svg class="i" style="color:#7fdbe8"><use href="#i-spark"/></svg>Start Designing</a>'
)

# Mobile drawer "Sign in / Create account"
nav_html = nav_html.replace(
    '<a class="btn g" href="#">Sign in / Create account</a>',
    '<a class="btn g" href="#" onclick="openAuthModal(); drawer(mnav, false); return false;">Sign in / Create account</a>'
)

# Mobile drawer links
nav_html = nav_html.replace(
    '<a href="#">AI 3D Studio <span class="tag">CDR</span></a>',
    '<a href="#" onclick="openAiStudioModal(); drawer(mnav, false); return false;"><svg class="i sparkle" style="margin-right:6px"><use href="#i-spark"/></svg>AI 3D Studio <span class="tag">CDR</span></a>'
)
nav_html = nav_html.replace(
    '<a href="#">Workflow</a>',
    '<a href="#workflow" onclick="drawer(mnav, false);"><svg class="i" style="margin-right:6px"><use href="#i-flow"/></svg>Workflow</a>'
)
nav_html = nav_html.replace(
    '<a href="#">CDR Vault</a>',
    '<a href="#" onclick="openCdrTemplateVault(); drawer(mnav, false); return false;"><svg class="i" style="margin-right:6px"><use href="#i-vault"/></svg>CDR Vault</a>'
)
nav_html = nav_html.replace(
    '<a href="#">Track ZAM-ID</a>',
    '<a href="#tracking" data-go="track" onclick="drawer(mnav, false);"><svg class="i" style="margin-right:6px"><use href="#i-box"/></svg>Track ZAM-ID</a>'
)

# Account dropdown links
nav_html = nav_html.replace(
    '<a href="#"><svg class="i"><use href="#i-box"/></svg>Track an order</a>',
    '<a href="#tracking" data-go="track"><svg class="i"><use href="#i-box"/></svg>Track an order</a>'
)
nav_html = nav_html.replace(
    '<a href="#"><svg class="i"><use href="#i-pen"/></svg>Custom design orders</a>',
    '<a href="#" onclick="openAiStudioModal(); aMenu.classList.remove(\'open\'); return false;"><svg class="i"><use href="#i-spark"/></svg>AI Studio Designs</a>'
)
nav_html = nav_html.replace(
    '<a href="#"><svg class="i"><use href="#i-clock"/></svg>Order history &amp; reorder</a>',
    '<a href="#" onclick="toggleStaffDrawer(); aMenu.classList.remove(\'open\'); return false;"><svg class="i"><use href="#i-shield"/></svg>Staff Atelier Console</a>'
)
nav_html = nav_html.replace(
    '<a href="#"><svg class="i"><use href="#i-logout"/></svg>Sign out</a>',
    '<a href="#" onclick="openAuthModal(); aMenu.classList.remove(\'open\'); return false;"><svg class="i"><use href="#i-logout"/></svg>Sign in / Account</a>'
)

# 4. Construct complete Navbar JavaScript with enhanced search, smooth scrolling, and safe scoping
nav_js = """
/* ZamForward Navbar & Mega-Menu Logic */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* Announcement rotator */
  const annEl = $('#ann');
  if (annEl) {
    const m = $$('#ann p');
    if (m.length > 1) {
      let i = 0;
      setInterval(() => {
        m[i].classList.remove('on');
        i = (i + 1) % m.length;
        m[i].classList.add('on');
      }, 4200);
    }
  }

  /* Sticky shrink on scroll */
  const hdr = $('#hdr');
  if (hdr) {
    window.addEventListener('scroll', () => {
      hdr.classList.toggle('stuck', window.scrollY > 40);
    }, { passive: true });
  }

  /* Mega menu */
  const shopBtn = $('#shopBtn');
  const mega = $('#mega');
  const navrow = $('.navrow');
  let mt, pinned = false;

  window.closeMega = () => {
    if (!mega) return;
    clearTimeout(mt);
    pinned = false;
    mega.classList.remove('open');
    if (shopBtn) shopBtn.setAttribute('aria-expanded', 'false');
  };

  const openMega = o => {
    if (!mega) return;
    clearTimeout(mt);
    if (!o) pinned = false;
    mega.classList.toggle('open', o);
    if (shopBtn) shopBtn.setAttribute('aria-expanded', o ? 'true' : 'false');
  };

  if (shopBtn && mega && navrow) {
    navrow.style.position = 'relative';
    shopBtn.addEventListener('click', e => {
      e.preventDefault();
      if (mega.classList.contains('open') && pinned) openMega(false);
      else { openMega(true); pinned = true; }
    });
    shopBtn.addEventListener('mouseenter', () => {
      if (window.matchMedia('(hover:hover)').matches) openMega(true);
    });
    [shopBtn, mega].forEach(e => e.addEventListener('mouseleave', () => {
      if (!pinned) mt = setTimeout(() => openMega(false), 140);
    }));
    mega.addEventListener('mouseenter', () => clearTimeout(mt));
  }

  /* Account menu */
  const aBtn = $('#acctBtn'), aMenu = $('#acctMenu');
  if (aBtn && aMenu) {
    window.aMenu = aMenu;
    aBtn.addEventListener('click', e => {
      e.stopPropagation();
      const o = !aMenu.classList.contains('open');
      aMenu.classList.toggle('open', o);
      aBtn.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
  }

  /* Search suggestions */
  const q = $('#q'), sg = $('#sugg');
  const PRODUCTS = [
    ['Apex Stealth Compression Rashguard', 'Rashguards'],
    ['Hybrid Pro MMA Fight Shorts', 'MMA'],
    ['Imperial Pearl Weave BJJ Gi', 'BJJ'],
    ['Bangkok Retro Muay Thai Shorts', 'Muay Thai'],
    ['Ranked BJJ Long Sleeve Rashguard', 'BJJ'],
    ['Sub-Zero Thermal Grappling Spats', 'Compression'],
    ['Custom Sublimated Team Kit', 'Custom']
  ];

  const hl = (t, s) => {
    const i = t.toLowerCase().indexOf(s.toLowerCase());
    return i < 0 ? t : t.slice(0, i) + '<mark>' + t.slice(i, i + s.length) + '</mark>' + t.slice(i + s.length);
  };

  function paint() {
    if (!q || !sg) return;
    const v = q.value.trim();
    let h = '';
    if (!v) {
      h = `<h6>Popular searches</h6><div class="chips"><a href="#catalog" class="chip-item">Rashguards</a><a href="#catalog" class="chip-item">BJJ gi</a><a href="#catalog" class="chip-item">Fight shorts</a><a href="#catalog" class="chip-item">Muay Thai</a><a href="#catalog" class="chip-item">Team kits</a></div><h6>Trending</h6>` +
        PRODUCTS.slice(0, 3).map(p => `<a href="#catalog" class="sugg-prod" role="option" data-kw="${p[0]}"><svg class="i"><use href="#i-search"/></svg>${p[0]}<em>${p[1]}</em></a>`).join('');
    } else {
      const r = PRODUCTS.filter(p => p[0].toLowerCase().includes(v.toLowerCase()) || p[1].toLowerCase().includes(v.toLowerCase()));
      h = r.length ? `<h6>Products</h6>` + r.map(p => `<a href="#catalog" class="sugg-prod" role="option" data-kw="${p[0]}"><svg class="i"><use href="#i-tee"/></svg><span>${hl(p[0], v)}</span><em>${p[1]}</em></a>`).join('') :
        `<h6>No matches</h6><a href="#" class="sugg-custom" role="option"><svg class="i"><use href="#i-spark"/></svg>Design a custom "${v.replace(/[<>&]/g, '')}" with AI Studio</a>`;
    }
    sg.innerHTML = h;
    sg.classList.add('open');
    q.setAttribute('aria-expanded', 'true');
  }

  if (q && sg) {
    q.addEventListener('focus', paint);
    q.addEventListener('input', paint);
    q.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        e.preventDefault();
        sg.classList.remove('open');
        const cat = document.getElementById('catalog');
        if (cat) cat.scrollIntoView({ behavior: 'smooth' });
      }
    });

    sg.addEventListener('click', e => {
      const customLink = e.target.closest('.sugg-custom');
      if (customLink) {
        e.preventDefault();
        sg.classList.remove('open');
        if (window.openAiStudioModal) window.openAiStudioModal();
        return;
      }
      const prodLink = e.target.closest('.sugg-prod, .chip-item');
      if (prodLink) {
        e.preventDefault();
        sg.classList.remove('open');
        const kw = prodLink.dataset.kw || prodLink.innerText.trim();
        q.value = kw;
        const cat = document.getElementById('catalog');
        if (cat) cat.scrollIntoView({ behavior: 'smooth' });
        return;
      }
    });
  }

  /* Drawers */
  const scrim = $('#scrim');
  const cart = $('#cart');
  const mnav = $('#mnav');
  window.cart = cart;
  window.mnav = mnav;

  window.drawer = function(el, o) {
    if (!el) return;
    el.classList.toggle('open', o);
    el.setAttribute('aria-hidden', o ? 'false' : 'true');
    if (scrim) scrim.classList.toggle('on', o);
    document.body.style.overflow = o ? 'hidden' : '';
  };

  const closeAll = () => {
    $$('.drawer').forEach(d => drawer(d, false));
    if (mega) openMega(false);
    if (aMenu && aBtn) {
      aMenu.classList.remove('open');
      aBtn.setAttribute('aria-expanded', 'false');
    }
    if (sg && q) {
      sg.classList.remove('open');
      q.setAttribute('aria-expanded', 'false');
    }
  };
  window.closeAll = closeAll;

  const cartBtn = $('#cartBtn');
  if (cartBtn && cart) cartBtn.addEventListener('click', () => drawer(cart, true));

  const burger = $('#burger');
  if (burger && mnav) burger.addEventListener('click', () => drawer(mnav, true));

  if (scrim) scrim.addEventListener('click', closeAll);
  $$('[data-close]').forEach(b => b.addEventListener('click', closeAll));

  /* Smooth scroll to Order Tracking */
  window.scrollToTrack = function() {
    closeAll();
    const tr = document.getElementById('tracking') || document.querySelector('.zt');
    if (tr) {
      tr.scrollIntoView({ behavior: 'smooth', block: 'start' });
      const inp = document.getElementById('trackInput') || tr.querySelector('input');
      if (inp) setTimeout(() => inp.focus(), 600);
    }
  };

  document.addEventListener('click', e => {
    const trackTrigger = e.target.closest('[data-go="track"]');
    if (trackTrigger) {
      e.preventDefault();
      window.scrollToTrack();
      return;
    }

    if (aBtn && aMenu && !e.target.closest('.rel')) {
      aMenu.classList.remove('open');
      aBtn.setAttribute('aria-expanded', 'false');
    }
    if (q && sg && !e.target.closest('.search')) {
      sg.classList.remove('open');
      q.setAttribute('aria-expanded', 'false');
    }
    if (mega && shopBtn && !e.target.closest('.has-mega, .mega, #shopBtn')) {
      openMega(false);
    }
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeAll();
    }
    if (e.key === '/' && q && !/input|textarea/i.test(document.activeElement.tagName)) {
      e.preventDefault();
      q.focus();
    }
  });

  /* Wire cart +/- quantity buttons */
  if (cart) {
    cart.addEventListener('click', e => {
      const btn = e.target.closest('.qty button');
      if (btn) {
        e.preventDefault();
        const span = btn.parentElement.querySelector('span');
        if (span) {
          let count = parseInt(span.innerText, 10) || 1;
          if (btn.innerText.trim() === '+') count++;
          else if (btn.innerText.trim() === '-' && count > 1) count--;
          span.innerText = count;
        }
      }
    });
  }

  /* Prevent dead link jumping */
  $$('a[href="#"]').forEach(a => {
    if (!a.getAttribute('onclick')) {
      a.addEventListener('click', e => e.preventDefault());
    }
  });
})();
"""

# 5. Insert CSS into <head>
head_close = orig_html.find('</head>')
if head_close == -1:
    raise Exception("No </head> found")

style_block = f"""
  <!-- ZamForward Navbar Component Styles -->
  <style id="zam-navbar-style">
{nav_css}
  </style>
"""

html_with_css = orig_html[:head_close] + style_block + orig_html[head_close:]

# 6. Replace old announcement and header in <body>
# Old announcement begins with: <!-- TOP UTILITY RAIL
# Old header ends with: </header>
old_ann_idx = html_with_css.find('<!-- TOP UTILITY RAIL')
if old_ann_idx == -1:
    # Alternative locator
    old_ann_idx = html_with_css.find('<div class="w-full bg-[#111417]')

header_end_idx = html_with_css.find('</header>') + len('</header>')

print(f"Replacing old announcement & header from index {old_ann_idx} to {header_end_idx}")
print("Old snippet being replaced:")
print(html_with_css[old_ann_idx:old_ann_idx+200])

new_header_block = f"""
  <!-- ==================== UPGRADED NAVIGATION & ANNOUNCEMENT ==================== -->
{nav_html}
  <!-- ==================== END NAVIGATION & ANNOUNCEMENT ==================== -->
"""

html_with_nav = html_with_css[:old_ann_idx] + new_header_block + html_with_css[header_end_idx:]

# 7. Insert Navbar Script before </body>
body_close = html_with_nav.rfind('</body>')
if body_close == -1:
    raise Exception("No </body> found")

script_block = f"""
  <!-- ZamForward Navbar Interactive Controller -->
  <script id="zam-navbar-script">
{nav_js}
  </script>
"""

final_html = html_with_nav[:body_close] + script_block + html_with_nav[body_close:]

# 8. Write to public/index.html and code.html
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully written updated navbar to public/index.html and code.html!")
print("New index.html length:", len(final_html))
