import re

# Read base code.html
with open('code.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Enhance header sign-in button
html = html.replace(
    '<a class="flex items-center gap-space-sm pl-space-xs hover:opacity-90 transition-opacity" data-path="account" href="#"><img alt="Profile" class="w-8 h-8 rounded-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBkWmebPefwv2j9HM8pQzfJCt9GwqQwJnmH7m-9Gcf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ"/><span class="hidden lg:inline-block font-title-sm text-title-sm text-on-surface">Sign In</span></a>',
    '<button onclick="openAuthModal()" class="flex items-center gap-space-sm pl-space-xs hover:opacity-90 transition-opacity text-left"><img alt="Profile" class="w-8 h-8 rounded-full object-cover ring-2 ring-secondary/30" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBkWmebPefwv2j9HM8pQzfJCt9GwqQwJnmH7m-9Gcf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ"/><span id="headerUserLabel" class="hidden lg:inline-block font-title-sm text-title-sm text-on-surface font-semibold">Sign In / Register</span></button>'
)

# 2. Enhance Navigation buttons
html = html.replace(
    '<a class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm" data-path="custom-ai-studio" href="#">Custom AI Studio</a>',
    '<button onclick="openCustomOrderModal()" class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm">Custom AI Studio</button>'
)
html = html.replace(
    '<a class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm" data-path="order-workflow-tracking" href="#">Order Workflow &amp; Tracking</a>',
    '<a class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm" href="#tracking">Order Workflow &amp; Tracking</a>'
)
html = html.replace(
    '<a class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm" data-path="templates-bulk" href="#">Templates &amp; Bulk</a>',
    '<button onclick="openCdrTemplateVault()" class="px-space-md py-space-xs rounded text-on-surface-variant hover:text-on-surface transition-colors font-title-sm text-title-sm">CDR Templates &amp; Bulk</button>'
)

# 3. Enhance Featured Product buttons in section 4
html = html.replace(
    '<button class="w-full py-space-sm bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors shadow-sm">Add To Bag</button>',
    '<button onclick="openCustomOrderModal(1)" class="w-full py-space-sm bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors shadow-sm flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">shopping_bag</span> Order Custom Mockup</button>'
)
html = html.replace(
    '<button class="w-full py-space-sm bg-surface-container rounded-lg font-label-lg text-label-lg uppercase text-primary hover:bg-surface-container-highest transition-colors">Download Spec Sheet</button>',
    '<button onclick="openCdrTemplateVault(\'CDR-RG-01\')" class="w-full py-space-sm bg-surface-container rounded-lg font-label-lg text-label-lg uppercase text-primary hover:bg-surface-container-highest transition-colors flex items-center justify-center gap-1"><span class="material-symbols-outlined text-[18px]">draft</span> View CDR Markup Specs</button>'
)

# 4. Enhance Studio interactive mockup button in section 6
html = html.replace(
    '<button class="w-full py-space-sm bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors flex items-center justify-center gap-space-xs">Apply To 3D Mockup <span class="material-symbols-outlined text-[16px]">arrow_forward</span></button>',
    '<button onclick="openCustomOrderModal(1)" class="w-full py-space-sm bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors flex items-center justify-center gap-space-xs">Place Custom Order With Design <span class="material-symbols-outlined text-[16px]">arrow_forward</span></button>'
)

# 5. Enhance Tracking Section
tracking_target = '''<!-- 8. RECENT ORDERS LIVE TRACKER WIDGET (ZAM-ID Verification) -->
<section class="max-w-[1360px] mx-auto px-margin-mobile md:px-margin w-full mb-space-3xl" id="tracking">
<div class="bg-surface-container-lowest p-space-lg md:p-space-xl rounded-2xl shadow-sm">
<div class="flex flex-col md:flex-row md:items-center justify-between gap-space-md mb-space-lg">
<div>
<span class="font-label-md text-label-md uppercase text-secondary font-bold tracking-widest">Live Manufacturing Atelier</span>
<h2 class="font-headline-md text-headline-md text-primary uppercase">Track Your Order Status (ZAM-ID)</h2>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1">
            Check real-time factory milestone, sublimation status, or wire transfer invoice clearance.
          </p>
</div>
<div class="flex items-center gap-2 max-w-md w-full">
<div class="relative flex-1">
<span class="material-symbols-outlined absolute left-3 top-2.5 text-outline text-[18px]">search</span>
<input class="w-full pl-9 pr-3 py-2 bg-surface-container rounded-lg font-title-sm text-title-sm text-primary focus:outline-none uppercase" type="text" value="ZAM-401-26"/>
</div>
<button class="px-space-md py-2 bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors">
            Lookup
          </button>
</div>
</div>
<!-- Live Tracking Card Sample -->
<div class="bg-surface-container-low rounded-xl p-space-md md:p-space-lg">
<div class="flex flex-wrap items-center justify-between gap-space-sm pb-space-md mb-space-md">
<div class="flex items-center gap-space-sm">
<div class="w-10 h-10 rounded-lg bg-primary text-on-primary flex items-center justify-center font-bold text-sm">
              #401
            </div>
<div>
<div class="flex items-center gap-2">
<h4 class="font-title-md text-title-md text-primary uppercase">Order #ZAM-401-26 • Apex MMA Academy</h4>
<span class="px-2 py-0.5 rounded bg-secondary-container text-on-secondary-container font-label-md text-label-md uppercase font-bold">In Production</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">45 Pcs Custom Short Sleeve Rashguards • 45 Pcs Hybrid Fight Shorts</p>
</div>
</div>
<div class="flex items-center gap-space-sm">
<button class="px-space-sm py-1.5 rounded bg-surface-container font-label-md text-label-md uppercase text-primary hover:bg-surface-container-highest transition-colors flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">receipt</span> View 50% Invoice
            </button>
<button class="px-space-sm py-1.5 rounded bg-primary text-on-primary font-label-md text-label-md uppercase hover:bg-primary-container transition-colors flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">replay</span> 1-Click Reorder
            </button>
</div>
</div>
<!-- 5-Step Visual Progress Bar -->
<div class="relative py-space-sm">
<div class="w-full bg-surface-container-highest h-2 rounded-full overflow-hidden mb-space-md">
<div class="bg-secondary h-full rounded-full w-[65%] transition-all duration-1000"></div>
</div>
<div class="grid grid-cols-2 md:grid-cols-5 gap-space-sm text-center">
<div class="flex flex-col items-center">
<span class="w-6 h-6 rounded-full bg-secondary text-on-secondary text-xs flex items-center justify-center mb-1 font-bold">✓</span>
<span class="font-title-sm text-xs text-primary uppercase">Order File Created</span>
<span class="text-[11px] text-outline">May 12 • Specs Locked</span>
</div>
<div class="flex flex-col items-center">
<span class="w-6 h-6 rounded-full bg-secondary text-on-secondary text-xs flex items-center justify-center mb-1 font-bold">✓</span>
<span class="font-title-sm text-xs text-primary uppercase">50% Deposit Cleared</span>
<span class="text-[11px] text-outline">May 14 • Slip Verified</span>
</div>
<div class="flex flex-col items-center">
<span class="w-6 h-6 rounded-full bg-secondary text-on-secondary text-xs flex items-center justify-center mb-1 font-bold animate-pulse">●</span>
<span class="font-title-sm text-xs text-secondary font-bold uppercase">Sublimation &amp; Sewing</span>
<span class="text-[11px] text-secondary font-bold">Active in Atelier</span>
</div>
<div class="flex flex-col items-center opacity-40">
<span class="w-6 h-6 rounded-full bg-surface-container-highest text-outline text-xs flex items-center justify-center mb-1">4</span>
<span class="font-title-sm text-xs text-on-surface uppercase">QC &amp; Dispatch</span>
<span class="text-[11px] text-outline">Target: In 14 Days</span>
</div>
<div class="flex flex-col items-center opacity-40">
<span class="w-6 h-6 rounded-full bg-surface-container-highest text-outline text-xs flex items-center justify-center mb-1">5</span>
<span class="font-title-sm text-xs text-on-surface uppercase">Door Delivery</span>
<span class="text-[11px] text-outline">DHL Global Express</span>
</div>
</div>
</div>
</div>
</div>
</section>'''

tracking_replacement = '''<!-- 8. RECENT ORDERS LIVE TRACKER WIDGET (ZAM-ID Verification) -->
<section class="max-w-[1360px] mx-auto px-margin-mobile md:px-margin w-full mb-space-3xl" id="tracking">
<div class="bg-surface-container-lowest p-space-lg md:p-space-xl rounded-2xl shadow-sm border border-outline-variant/30">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-space-md mb-space-lg">
    <div>
      <span class="font-label-md text-label-md uppercase text-secondary font-bold tracking-widest flex items-center gap-1.5">
        <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
        Live Manufacturing Atelier • SQLite Engine Connected
      </span>
      <h2 class="font-headline-md text-headline-md text-primary uppercase mt-1">Track Your Order Status (ZAM-ID)</h2>
      <p class="font-body-sm text-body-sm text-on-surface-variant mt-1">
        Check real-time factory milestones, sublimation status, or wire transfer invoice clearance.
      </p>
      <!-- Quick Pills -->
      <div class="flex items-center gap-2 mt-3 text-xs">
        <span class="text-outline uppercase font-semibold">Quick Demo Orders:</span>
        <button onclick="lookupOrder('ZAM-401-26')" class="px-2.5 py-1 rounded bg-surface-container font-mono text-primary hover:bg-surface-container-highest font-bold transition-colors">ZAM-401-26</button>
        <button onclick="lookupOrder('ZAM-402-26')" class="px-2.5 py-1 rounded bg-surface-container font-mono text-primary hover:bg-surface-container-highest font-bold transition-colors">ZAM-402-26</button>
        <button onclick="lookupOrder('ZAM-403-26')" class="px-2.5 py-1 rounded bg-surface-container font-mono text-primary hover:bg-surface-container-highest font-bold transition-colors">ZAM-403-26</button>
      </div>
    </div>
    <div class="flex items-center gap-2 max-w-md w-full">
      <div class="relative flex-1">
        <span class="material-symbols-outlined absolute left-3 top-2.5 text-outline text-[18px]">search</span>
        <input id="trackingInput" class="w-full pl-9 pr-3 py-2 bg-surface-container rounded-lg font-title-sm text-title-sm text-primary focus:outline-none uppercase border border-transparent focus:border-secondary transition-all" type="text" value="ZAM-401-26" placeholder="Enter ZAM-xxx-26" onkeydown="if(event.key==='Enter') lookupOrder()"/>
      </div>
      <button onclick="lookupOrder()" class="px-space-md py-2 bg-primary text-on-primary rounded-lg font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors shadow-sm flex items-center gap-1">
        <span class="material-symbols-outlined text-[18px]">track_changes</span> Lookup
      </button>
    </div>
  </div>

  <!-- Dynamic Live Tracking Card Container -->
  <div id="trackingResultContainer" class="bg-surface-container-low rounded-xl p-space-md md:p-space-lg transition-all duration-300">
    <!-- Populated dynamically by lookupOrder() -->
  </div>
</div>
</section>'''

html = html.replace(tracking_target, tracking_replacement)

# 6. Add Modals, Staff Operations Drawer, and Client Script before </body>
modals_and_scripts = '''
<!-- ================= MODALS & SLIDEOUT PANELS ================= -->

<!-- 1. CUSTOM ORDER / DESIGN STUDIO MODAL -->
<div id="customOrderModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4 overflow-y-auto">
  <div class="bg-surface-container-lowest max-w-2xl w-full rounded-2xl shadow-2xl border border-outline-variant/40 p-6 md:p-8 my-8 relative">
    <button onclick="closeModal('customOrderModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
    <div class="flex items-center gap-2 mb-1">
      <span class="px-2.5 py-0.5 rounded-full bg-secondary-container text-on-secondary-container font-label-md text-label-md uppercase font-bold">ZamOne Atelier Engine</span>
      <span class="text-xs text-outline">• Direct Order Placement</span>
    </div>
    <h3 class="font-headline-md text-headline-md text-primary uppercase">Order Custom Combat Garment</h3>
    <p class="font-body-sm text-on-surface-variant mb-6">Configure your combat kit, upload custom vectors or logos, and send file directly to ZamForward.</p>
    
    <form id="orderForm" onsubmit="submitCustomOrder(event)" class="space-y-4">
      <div>
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Select Garment / Product</label>
        <select id="modalProductSelect" onchange="onModalProductChange()" class="w-full bg-surface-container px-3 py-2.5 rounded-lg font-title-sm text-title-sm text-primary focus:outline-none border border-outline-variant">
          <!-- Populated by script -->
        </select>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Size Cut</label>
          <select id="modalSizeSelect" class="w-full bg-surface-container px-3 py-2.5 rounded-lg font-title-sm text-title-sm text-primary focus:outline-none border border-outline-variant">
            <option value="XS">XS (Extra Small)</option>
            <option value="S">S (Small)</option>
            <option value="M" selected>M (Medium)</option>
            <option value="L">L (Large)</option>
            <option value="XL">XL (Extra Large)</option>
            <option value="2XL">2XL (Double Extra Large)</option>
          </select>
        </div>
        <div>
          <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Garment Color / Rank</label>
          <select id="modalColorSelect" class="w-full bg-surface-container px-3 py-2.5 rounded-lg font-title-sm text-title-sm text-primary focus:outline-none border border-outline-variant">
            <option value="Carbon Black">Carbon Black</option>
            <option value="Combat Cyan">Combat Cyan</option>
            <option value="Bone Sandstone">Bone Sandstone</option>
            <option value="White Belt Rank">White Belt Rank (IBJJF)</option>
            <option value="Blue Belt Rank">Blue Belt Rank (IBJJF)</option>
            <option value="Purple Belt Rank">Purple Belt Rank (IBJJF)</option>
            <option value="Brown Belt Rank">Brown Belt Rank (IBJJF)</option>
            <option value="Black Belt Rank">Black Belt Rank (IBJJF)</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Batch Quantity</label>
          <input id="modalQuantity" type="number" min="1" max="1000" value="10" oninput="updateModalPricing()" class="w-full bg-surface-container px-3 py-2.5 rounded-lg font-title-sm text-title-sm text-primary focus:outline-none border border-outline-variant"/>
        </div>
        <div>
          <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Unit Price / Subtotal</label>
          <div class="bg-surface-container-high px-3 py-2 rounded-lg flex items-center justify-between">
            <span id="modalUnitPrice" class="font-mono text-sm text-on-surface-variant">$54.00 / pc</span>
            <span id="modalEstimatedSubtotal" class="font-headline-sm text-headline-sm text-primary font-bold">$540.00</span>
          </div>
        </div>
      </div>

      <!-- Local File Management: Artwork Upload -->
      <div class="p-4 rounded-xl bg-surface-container-low border border-dashed border-outline-variant">
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1 flex items-center justify-between">
          <span>Upload Custom Design / Logo (Local Storage)</span>
          <span class="text-xs text-secondary font-bold">CDR / AI / PNG / PDF</span>
        </label>
        <input type="file" id="modalDesignFile" accept=".png,.jpg,.jpeg,.svg,.ai,.cdr,.eps,.pdf" class="w-full text-xs text-on-surface-variant file:mr-3 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-primary file:text-on-primary hover:file:bg-primary-container cursor-pointer"/>
        <p class="text-[11px] text-outline mt-1.5">Files are automatically saved locally into <code>uploads/designs/</code> and cataloged in SQLite.</p>
      </div>

      <!-- Customer Details -->
      <div class="pt-2 border-t border-outline-variant/40">
        <h4 class="font-label-md text-label-md uppercase text-secondary font-bold tracking-wider mb-2">Customer & Delivery Contact</h4>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
          <input id="modalCustName" type="text" placeholder="Athlete / Academy Name" required class="bg-surface-container px-3 py-2 rounded-lg text-xs font-title-sm text-primary focus:outline-none border border-outline-variant" value="Apex Fight Academy"/>
          <input id="modalCustEmail" type="email" placeholder="Email Address" required class="bg-surface-container px-3 py-2 rounded-lg text-xs font-title-sm text-primary focus:outline-none border border-outline-variant" value="coach@apexmmatraining.com"/>
          <input id="modalCustPhone" type="text" placeholder="Country Code + Phone" required class="bg-surface-container px-3 py-2 rounded-lg text-xs font-title-sm text-primary focus:outline-none border border-outline-variant" value="+1 800-555-0199"/>
        </div>
      </div>

      <div>
        <textarea id="modalOrderNotes" rows="2" placeholder="Special requirements, chest crest placement, neck taping text, deadline request..." class="w-full bg-surface-container p-3 rounded-lg text-xs font-title-sm text-primary focus:outline-none border border-outline-variant"></textarea>
      </div>

      <div class="flex items-center justify-end gap-3 pt-3">
        <button type="button" onclick="closeModal('customOrderModal')" class="px-5 py-2.5 rounded-lg bg-surface-container text-primary font-label-lg text-label-lg uppercase hover:bg-surface-container-high transition-colors">Cancel</button>
        <button type="submit" id="btnSubmitOrder" class="px-6 py-2.5 rounded-lg bg-primary text-on-primary font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors shadow-sm flex items-center gap-2">
          <span class="material-symbols-outlined text-[18px]">send</span> Confirm Order &amp; Generate ZAM-ID
        </button>
      </div>
    </form>
  </div>
</div>

<!-- 2. INVOICE VIEW MODAL -->
<div id="invoiceModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4 overflow-y-auto">
  <div class="bg-surface-container-lowest max-w-xl w-full rounded-2xl shadow-2xl border border-outline-variant/40 p-6 md:p-8 my-8 relative">
    <button onclick="closeModal('invoiceModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
    <div id="invoiceModalContent">
      <!-- Populated dynamically -->
    </div>
  </div>
</div>

<!-- 3. 50% PAYMENT SLIP UPLOAD MODAL -->
<div id="uploadSlipModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
  <div class="bg-surface-container-lowest max-w-lg w-full rounded-2xl shadow-2xl border border-outline-variant/40 p-6 relative">
    <button onclick="closeModal('uploadSlipModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
    <div class="flex items-center gap-2 mb-2">
      <span class="px-2.5 py-0.5 rounded-full bg-secondary-container text-on-secondary-container font-label-md text-label-md uppercase font-bold">Local File Management</span>
    </div>
    <h3 class="font-headline-md text-headline-md text-primary uppercase">Upload 50% Payment Slip</h3>
    <p class="font-body-sm text-on-surface-variant mb-4">Upload your bank transfer receipt or wire transfer confirmation to clear invoice and move to Production.</p>
    
    <form id="slipForm" onsubmit="submitPaymentSlip(event)" class="space-y-4">
      <input type="hidden" id="slipOrderNumber"/>
      <div>
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Order Reference</label>
        <input type="text" id="slipOrderDisplay" readonly class="w-full bg-surface-container-high px-3 py-2 rounded-lg font-mono font-bold text-primary"/>
      </div>
      <div>
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Transfer Amount ($ USD)</label>
        <input type="number" step="0.01" id="slipAmount" required class="w-full bg-surface-container px-3 py-2 rounded-lg font-title-sm text-primary focus:outline-none border border-outline-variant"/>
      </div>
      <div>
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Bank Reference / Wire Code</label>
        <input type="text" id="slipBankRef" placeholder="e.g. WIRE-CHASE-9921" required class="w-full bg-surface-container px-3 py-2 rounded-lg font-title-sm text-primary focus:outline-none border border-outline-variant"/>
      </div>
      <div class="p-4 rounded-xl bg-surface-container-low border border-dashed border-outline-variant">
        <label class="block font-label-lg text-label-lg text-primary uppercase mb-1">Select Slip File (PDF / Image)</label>
        <input type="file" id="slipFileInput" accept=".pdf,.png,.jpg,.jpeg" required class="w-full text-xs text-on-surface-variant file:mr-3 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-primary file:text-on-primary hover:file:bg-primary-container cursor-pointer"/>
        <p class="text-[11px] text-outline mt-1.5">File is saved locally in <code>uploads/payment_slips/</code> and tied to the order in SQLite.</p>
      </div>
      <div class="flex items-center justify-end gap-3 pt-2">
        <button type="button" onclick="closeModal('uploadSlipModal')" class="px-5 py-2.5 rounded-lg bg-surface-container text-primary font-label-lg text-label-lg uppercase hover:bg-surface-container-high transition-colors">Cancel</button>
        <button type="submit" class="px-6 py-2.5 rounded-lg bg-secondary text-on-secondary font-label-lg text-label-lg uppercase hover:opacity-90 transition-opacity flex items-center gap-2">
          <span class="material-symbols-outlined text-[18px]">cloud_upload</span> Submit Slip
        </button>
      </div>
    </form>
  </div>
</div>

<!-- 4. CDR TEMPLATE SPECIFICATIONS VAULT MODAL -->
<div id="cdrTemplateModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4 overflow-y-auto">
  <div class="bg-surface-container-lowest max-w-3xl w-full rounded-2xl shadow-2xl border border-outline-variant/40 p-6 md:p-8 my-8 relative">
    <button onclick="closeModal('cdrTemplateModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
    <div class="flex items-center gap-2 mb-1">
      <span class="px-2.5 py-0.5 rounded-full bg-tertiary-container text-on-tertiary-container font-label-md text-label-md uppercase font-bold">Phase 2 Markup Blueprint</span>
      <span class="text-xs text-outline">• CorelDraw (.CDR) Vector Suite</span>
    </div>
    <h3 class="font-headline-md text-headline-md text-primary uppercase">CorelDraw Template Markup Architecture</h3>
    <p class="font-body-sm text-on-surface-variant mb-6">Database-backed technical garment vector patterns with predefined sublimation zones, bleed margins, and cut lines.</p>
    <div id="cdrTemplateList" class="space-y-4">
      <!-- Populated dynamically -->
    </div>
  </div>
</div>

<!-- 5. CUSTOMER AUTH MODAL -->
<div id="authModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
  <div class="bg-surface-container-lowest max-w-md w-full rounded-2xl shadow-2xl border border-outline-variant/40 p-6 md:p-8 relative">
    <button onclick="closeModal('authModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
    <span class="font-label-md text-label-md uppercase text-secondary font-bold tracking-widest">ZamForward Identity</span>
    <h3 class="font-headline-md text-headline-md text-primary uppercase mt-1 mb-2">Athlete / Gym Sign Up</h3>
    <p class="font-body-sm text-on-surface-variant mb-4">Create your account with email verification to save custom designs and access wholesale pricing.</p>
    
    <form id="authForm" onsubmit="handleAuthSubmit(event)" class="space-y-3">
      <div class="grid grid-cols-2 gap-2">
        <input id="authFirstName" type="text" placeholder="First Name" required class="bg-surface-container px-3 py-2 rounded-lg text-sm text-primary focus:outline-none border border-outline-variant"/>
        <input id="authLastName" type="text" placeholder="Last Name" required class="bg-surface-container px-3 py-2 rounded-lg text-sm text-primary focus:outline-none border border-outline-variant"/>
      </div>
      <input id="authEmail" type="email" placeholder="Email Address" required class="w-full bg-surface-container px-3 py-2 rounded-lg text-sm text-primary focus:outline-none border border-outline-variant"/>
      <div class="grid grid-cols-3 gap-2">
        <input id="authCountryCode" type="text" value="+1" placeholder="Code" class="bg-surface-container px-3 py-2 rounded-lg text-sm text-primary text-center focus:outline-none border border-outline-variant"/>
        <input id="authPhone" type="text" placeholder="Phone Number" required class="col-span-2 bg-surface-container px-3 py-2 rounded-lg text-sm text-primary focus:outline-none border border-outline-variant"/>
      </div>
      <div class="p-3 bg-surface-container-low rounded-lg text-xs text-on-surface-variant flex items-center gap-2">
        <span class="material-symbols-outlined text-secondary text-[18px]">verified</span>
        <span>Auto-verifying email address through ZamOne verification service.</span>
      </div>
      <button type="submit" class="w-full py-2.5 rounded-lg bg-primary text-on-primary font-label-lg text-label-lg uppercase hover:bg-primary-container transition-colors shadow-sm">
        Register &amp; Access Atelier
      </button>
    </form>
  </div>
</div>

<!-- 6. STAFF ATELIER OPERATIONS CONSOLE (SLIDE-OVER DRAWER) -->
<div id="staffConsoleDrawer" class="fixed inset-y-0 right-0 z-50 w-full max-w-xl bg-surface-container-lowest shadow-2xl border-l border-outline-variant/40 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
  <div class="p-5 border-b border-outline-variant/40 flex items-center justify-between bg-surface-container-low">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-secondary animate-pulse"></span>
      <h3 class="font-headline-sm text-headline-sm text-primary uppercase">ZamForward Staff Atelier Console</h3>
    </div>
    <button onclick="toggleStaffDrawer()" class="w-8 h-8 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-surface-container-high transition-colors">
      <span class="material-symbols-outlined text-[18px]">close</span>
    </button>
  </div>
  
  <div class="p-5 flex-1 overflow-y-auto space-y-6">
    <!-- Live Stats -->
    <div class="grid grid-cols-3 gap-3">
      <div class="p-3 rounded-xl bg-surface-container text-center">
        <span class="text-xs text-outline uppercase font-semibold">Total Orders</span>
        <div id="adminStatOrders" class="font-headline-sm text-headline-sm text-primary font-bold">3</div>
      </div>
      <div class="p-3 rounded-xl bg-surface-container text-center">
        <span class="text-xs text-outline uppercase font-semibold">In Production</span>
        <div id="adminStatProduction" class="font-headline-sm text-headline-sm text-secondary font-bold">1</div>
      </div>
      <div class="p-3 rounded-xl bg-surface-container text-center">
        <span class="text-xs text-outline uppercase font-semibold">Total Volume</span>
        <div id="adminStatVolume" class="font-headline-sm text-headline-sm text-primary font-bold">$1,495</div>
      </div>
    </div>

    <div>
      <div class="flex items-center justify-between mb-3">
        <h4 class="font-label-lg text-label-lg uppercase text-primary font-bold">All Live SQLite Orders</h4>
        <button onclick="loadAdminOrders()" class="text-xs text-secondary hover:underline flex items-center gap-1 font-semibold">
          <span class="material-symbols-outlined text-[14px]">refresh</span> Refresh
        </button>
      </div>
      <div id="adminOrdersList" class="space-y-3">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>
</div>

<!-- FLOATING TRIGGER PILL FOR STAFF OPERATIONS -->
<div class="fixed bottom-6 right-6 z-40">
  <button onclick="toggleStaffDrawer()" class="px-4 py-2.5 rounded-full bg-primary text-on-primary font-label-md text-label-md uppercase tracking-wider shadow-xl hover:bg-primary-container transition-all flex items-center gap-2 border border-outline-variant/30">
    <span class="w-2.5 h-2.5 rounded-full bg-secondary animate-ping"></span>
    <span class="material-symbols-outlined text-[18px]">manufacturing</span>
    <span>Staff Atelier Console</span>
  </button>
</div>

<!-- TOAST CONTAINER -->
<div id="toastContainer" class="fixed top-6 right-6 z-50 space-y-2 pointer-events-none"></div>

<!-- ================= FRONTEND LOGIC SCRIPT ================= -->
<script>
let globalProducts = [];
let currentTrackingOrder = null;

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  fetchProducts();
  fetchTemplates();
  lookupOrder('ZAM-401-26');
  loadAdminOrders();
});

function showToast(msg, type = 'info') {
  const container = document.getElementById('toastContainer');
  const toast = document.createElement('div');
  const bg = type === 'success' ? 'bg-secondary text-on-secondary' : (type === 'error' ? 'bg-error text-on-error' : 'bg-primary text-on-primary');
  toast.className = `${bg} px-4 py-3 rounded-xl shadow-xl font-title-sm text-sm flex items-center gap-2 transform transition-all duration-300 pointer-events-auto`;
  toast.innerHTML = `<span class="material-symbols-outlined text-[18px]">${type === 'success' ? 'check_circle' : 'info'}</span><span>${msg}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('hidden');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('hidden');
}

function toggleStaffDrawer() {
  const drawer = document.getElementById('staffConsoleDrawer');
  if (drawer.classList.contains('translate-x-full')) {
    drawer.classList.remove('translate-x-full');
    loadAdminOrders();
  } else {
    drawer.classList.add('translate-x-full');
  }
}

function openAuthModal() {
  openModal('authModal');
}

function handleAuthSubmit(e) {
  e.preventDefault();
  const fName = document.getElementById('authFirstName').value;
  const lName = document.getElementById('authLastName').value;
  const email = document.getElementById('authEmail').value;
  const cCode = document.getElementById('authCountryCode').value;
  const phone = document.getElementById('authPhone').value;

  fetch('/api/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ first_name: fName, last_name: lName, email: email, country_code: cCode, phone: phone })
  })
  .then(res => res.json())
  .then(data => {
    if (data.user) {
      document.getElementById('headerUserLabel').innerText = `${fName} (${email})`;
      showToast(`Welcome ${fName}! Email verified and account ready.`, 'success');
      closeModal('authModal');
    } else {
      showToast(data.error || 'Registration failed', 'error');
    }
  })
  .catch(err => showToast(err.message, 'error'));
}

function fetchProducts() {
  fetch('/api/products')
    .then(r => r.json())
    .then(products => {
      globalProducts = products;
      const select = document.getElementById('modalProductSelect');
      select.innerHTML = products.map(p => `<option value="${p.id}" data-price="${p.base_price}">${p.name} ($${p.base_price.toFixed(2)})</option>`).join('');
      updateModalPricing();
    });
}

function onModalProductChange() {
  updateModalPricing();
}

function updateModalPricing() {
  const select = document.getElementById('modalProductSelect');
  const opt = select.options[select.selectedIndex];
  if (!opt) return;
  const unitPrice = parseFloat(opt.getAttribute('data-price') || 54);
  const qty = parseInt(document.getElementById('modalQuantity').value) || 1;
  const total = unitPrice * qty;
  document.getElementById('modalUnitPrice').innerText = `$${unitPrice.toFixed(2)} / pc`;
  document.getElementById('modalEstimatedSubtotal').innerText = `$${total.toFixed(2)}`;
}

function openCustomOrderModal(productId = null) {
  openModal('customOrderModal');
  if (productId) {
    const select = document.getElementById('modalProductSelect');
    select.value = productId;
    updateModalPricing();
  }
}

async function submitCustomOrder(e) {
  e.preventDefault();
  const btn = document.getElementById('btnSubmitOrder');
  btn.disabled = true;
  btn.innerHTML = 'Registering Order...';

  const select = document.getElementById('modalProductSelect');
  const opt = select.options[select.selectedIndex];
  const pId = parseInt(select.value);
  const pName = opt.text.split(' ($')[0];
  const unitPrice = parseFloat(opt.getAttribute('data-price') || 54);
  const size = document.getElementById('modalSizeSelect').value;
  const color = document.getElementById('modalColorSelect').value;
  const qty = parseInt(document.getElementById('modalQuantity').value) || 1;
  const custName = document.getElementById('modalCustName').value;
  const custEmail = document.getElementById('modalCustEmail').value;
  const custPhone = document.getElementById('modalCustPhone').value;
  const notes = document.getElementById('modalOrderNotes').value;

  const payload = {
    customer_name: custName,
    customer_email: custEmail,
    customer_phone: custPhone,
    notes: notes,
    items: [{
      product_id: pId,
      product_name: pName,
      quantity: qty,
      size: size,
      color: color,
      unit_price: unitPrice,
      design_config: { custom_color: color, requested_size: size }
    }]
  };

  try {
    const res = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    
    if (result.order_number) {
      // If a design file was attached, upload it locally
      const fileInput = document.getElementById('modalDesignFile');
      if (fileInput.files.length > 0) {
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('category', 'designs');
        formData.append('order_number', result.order_number);
        await fetch('/api/upload', { method: 'POST', body: formData });
      }

      showToast(`Order ${result.order_number} confirmed! Saved to SQLite database.`, 'success');
      closeModal('customOrderModal');
      document.getElementById('trackingInput').value = result.order_number;
      lookupOrder(result.order_number);
      loadAdminOrders();
    } else {
      showToast(result.error || 'Order placement failed', 'error');
    }
  } catch (err) {
    showToast(err.message, 'error');
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<span class="material-symbols-outlined text-[18px]">send</span> Confirm Order & Generate ZAM-ID';
  }
}

// Order Status Flow definition
const STATUS_STEPS = [
  { key: 'Confirmed', label: 'Order File Created', sub: 'Specs Registered' },
  { key: 'Received by ZAM', label: 'Received by ZAM', sub: 'Atelier Queued' },
  { key: 'Invoice Cleared', label: '50% Deposit Cleared', sub: 'Slip Verified' },
  { key: 'In Progress', label: 'In Progress', sub: 'Cut Scheduled' },
  { key: 'Production', label: 'Sublimation & Sewing', sub: 'Active in Atelier' },
  { key: 'Dispatched', label: 'QC & Dispatched', sub: 'DHL In Transit' },
  { key: 'Completed', label: 'Door Delivery', sub: 'Order Completed' }
];

function getStatusIndex(status) {
  const norm = (status || '').toLowerCase();
  if (norm.includes('confirm')) return 0;
  if (norm.includes('received')) return 1;
  if (norm.includes('invoice sent')) return 1.5;
  if (norm.includes('clear') || norm.includes('deposit')) return 2;
  if (norm.includes('progress')) return 3;
  if (norm.includes('production')) return 4;
  if (norm.includes('dispatch')) return 5;
  if (norm.includes('complet')) return 6;
  return 0;
}

function lookupOrder(orderId = null) {
  const query = (orderId || document.getElementById('trackingInput').value || '').trim().toUpperCase();
  if (!query) return;

  const container = document.getElementById('trackingResultContainer');
  container.innerHTML = `<div class="p-8 text-center text-outline"><span class="material-symbols-outlined animate-spin text-[32px]">progress_activity</span><p class="mt-2 text-xs">Querying SQLite order database for ${query}...</p></div>`;

  fetch(`/api/orders/${query}`)
    .then(r => {
      if (!r.ok) throw new Error(`Order ${query} not found in database.`);
      return r.json();
    })
    .then(order => {
      currentTrackingOrder = order;
      renderTrackingCard(order);
    })
    .catch(err => {
      container.innerHTML = `
        <div class="p-6 text-center bg-surface-container rounded-xl">
          <span class="material-symbols-outlined text-error text-[36px]">error_outline</span>
          <h4 class="font-title-md text-primary mt-2 uppercase font-bold">${err.message}</h4>
          <p class="text-xs text-on-surface-variant mt-1">Try one of the active demo orders: <strong>ZAM-401-26</strong>, <strong>ZAM-402-26</strong>, or place a new custom mockup above.</p>
        </div>`;
    });
}

function renderTrackingCard(order) {
  const container = document.getElementById('trackingResultContainer');
  const sIdx = getStatusIndex(order.status);
  const progressPercent = Math.min(100, Math.round(((sIdx + 1) / STATUS_STEPS.length) * 100));

  const itemsDesc = order.items.map(i => `${i.quantity}x ${i.product_name} (${i.size}, ${i.color})`).join(' • ');

  let statusBadgeColor = 'bg-secondary-container text-on-secondary-container';
  if (order.status === 'Confirmed') statusBadgeColor = 'bg-surface-container-high text-primary';
  if (order.status === 'Completed') statusBadgeColor = 'bg-green-100 text-green-800';

  let html = `
    <div class="flex flex-wrap items-center justify-between gap-space-sm pb-space-md mb-space-md border-b border-outline-variant/30">
      <div class="flex items-center gap-space-sm">
        <div class="w-12 h-12 rounded-xl bg-primary text-on-primary flex flex-col items-center justify-center font-bold text-xs">
          <span class="text-[10px] text-outline opacity-80">ZAM</span>
          <span>#${order.order_number.split('-')[1] || '401'}</span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h4 class="font-title-md text-title-md text-primary uppercase font-bold">Order #${order.order_number} • ${order.customer_name}</h4>
            <span class="px-2.5 py-0.5 rounded ${statusBadgeColor} font-label-md text-label-md uppercase font-bold">${order.status}</span>
          </div>
          <p class="font-body-sm text-body-sm text-on-surface-variant mt-0.5">${itemsDesc || 'Custom Combat Items'}</p>
          <div class="flex items-center gap-4 mt-1 text-xs text-outline">
            <span>Deadline: <strong class="text-primary font-mono">${order.production_deadline || 'Scheduled upon deposit'}</strong></span>
            ${order.tracking_number ? `<span>Tracking: <strong class="text-secondary font-mono">${order.courier || 'DHL'}: ${order.tracking_number}</strong></span>` : ''}
          </div>
        </div>
      </div>
      <div class="flex items-center gap-2 flex-wrap">
        <button onclick="openInvoiceModal('${order.order_number}')" class="px-3 py-1.5 rounded bg-surface-container font-label-md text-label-md uppercase text-primary hover:bg-surface-container-highest transition-colors flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">receipt</span> View Invoice
        </button>
        <button onclick="openSlipModal('${order.order_number}', ${order.invoice ? order.invoice.deposit_required : 200})" class="px-3 py-1.5 rounded bg-secondary text-on-secondary font-label-md text-label-md uppercase hover:opacity-90 transition-opacity flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">upload_file</span> Upload 50% Slip
        </button>
        <button onclick="reorderFast('${order.order_number}')" class="px-3 py-1.5 rounded bg-primary text-on-primary font-label-md text-label-md uppercase hover:bg-primary-container transition-colors flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">replay</span> 1-Click Reorder
        </button>
      </div>
    </div>

    <!-- Multi-Step Visual Progress Bar -->
    <div class="relative py-2">
      <div class="w-full bg-surface-container-highest h-2 rounded-full overflow-hidden mb-4">
        <div class="bg-secondary h-full rounded-full transition-all duration-700" style="width: ${progressPercent}%"></div>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-7 gap-2 text-center">
        ${STATUS_STEPS.map((step, idx) => {
          const isDone = sIdx >= idx;
          const isCurrent = Math.floor(sIdx) === idx;
          const circleClass = isDone ? 'bg-secondary text-on-secondary' : 'bg-surface-container-highest text-outline';
          const pulse = isCurrent ? 'animate-pulse ring-2 ring-secondary/50' : '';
          const opacity = isDone ? '' : 'opacity-40';
          return `
            <div class="flex flex-col items-center ${opacity}">
              <span class="w-6 h-6 rounded-full ${circleClass} ${pulse} text-xs flex items-center justify-center mb-1 font-bold">
                ${isDone && !isCurrent ? '✓' : (idx + 1)}
              </span>
              <span class="font-title-sm text-[11px] text-primary uppercase font-bold leading-tight">${step.label}</span>
              <span class="text-[10px] text-outline mt-0.5">${step.sub}</span>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;

  container.innerHTML = html;
}

function openInvoiceModal(orderNumber) {
  if (!currentTrackingOrder || currentTrackingOrder.order_number !== orderNumber) {
    fetch(`/api/orders/${orderNumber}`)
      .then(r => r.json())
      .then(order => {
        currentTrackingOrder = order;
        renderInvoiceModalContent(order);
        openModal('invoiceModal');
      });
  } else {
    renderInvoiceModalContent(currentTrackingOrder);
    openModal('invoiceModal');
  }
}

function renderInvoiceModalContent(order) {
  const inv = order.invoice || {
    invoice_number: `INV-${order.order_number}`,
    subtotal: order.total_amount,
    tax_amount: 0,
    discount: 0,
    total: order.total_amount,
    deposit_required: order.total_amount * 0.5,
    status: 'Pending 50% Deposit',
    line_items: order.items.map(i => ({ desc: `${i.quantity}x ${i.product_name} (${i.size})`, total: i.subtotal }))
  };

  const content = document.getElementById('invoiceModalContent');
  content.innerHTML = `
    <div class="border-b border-outline-variant/40 pb-4 mb-4 flex items-center justify-between">
      <div>
        <span class="font-label-md text-xs uppercase text-secondary font-bold">ZamForward Combat Manufacturing</span>
        <h3 class="font-headline-sm text-headline-sm text-primary uppercase mt-0.5">${inv.invoice_number}</h3>
      </div>
      <span class="px-3 py-1 rounded-full bg-secondary-container text-on-secondary-container font-label-md text-xs uppercase font-bold">${inv.status}</span>
    </div>
    
    <div class="grid grid-cols-2 gap-4 text-xs mb-4">
      <div>
        <span class="text-outline uppercase block font-semibold">Billed To:</span>
        <strong class="text-primary">${order.customer_name}</strong>
        <p class="text-on-surface-variant">${order.customer_email}<br/>${order.customer_phone || ''}</p>
      </div>
      <div class="text-right">
        <span class="text-outline uppercase block font-semibold">Order ID:</span>
        <strong class="text-primary font-mono">${order.order_number}</strong>
        <p class="text-on-surface-variant">Due: 50% Upfront Wire Clearance</p>
      </div>
    </div>

    <div class="bg-surface-container rounded-xl p-3 mb-4">
      <table class="w-full text-xs">
        <thead>
          <tr class="text-outline border-b border-outline-variant/30 text-left">
            <th class="py-1">Description</th>
            <th class="py-1 text-right">Amount</th>
          </tr>
        </thead>
        <tbody>
          ${(inv.line_items || []).map(li => `
            <tr class="border-b border-outline-variant/10 text-primary">
              <td class="py-2">${li.desc}</td>
              <td class="py-2 text-right font-mono font-bold">$${parseFloat(li.total).toFixed(2)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>

    <div class="space-y-1.5 text-xs text-right border-t border-outline-variant/30 pt-3">
      <div class="flex justify-between">
        <span class="text-outline">Subtotal:</span>
        <span class="font-mono">$${parseFloat(inv.subtotal).toFixed(2)}</span>
      </div>
      <div class="flex justify-between">
        <span class="text-outline">Total Order Value:</span>
        <span class="font-mono font-bold text-sm text-primary">$${parseFloat(inv.total).toFixed(2)}</span>
      </div>
      <div class="flex justify-between p-2 rounded bg-secondary-container/40 text-secondary mt-2">
        <span class="font-bold uppercase">50% Deposit Required to Start:</span>
        <span class="font-mono font-bold text-base text-primary">$${parseFloat(inv.deposit_required).toFixed(2)}</span>
      </div>
    </div>

    <div class="mt-6 flex justify-end gap-2">
      <button onclick="closeModal('invoiceModal')" class="px-4 py-2 rounded-lg bg-surface-container text-primary font-label-md uppercase text-xs">Close</button>
      <button onclick="closeModal('invoiceModal'); openSlipModal('${order.order_number}', ${inv.deposit_required});" class="px-4 py-2 rounded-lg bg-secondary text-on-secondary font-label-md uppercase text-xs flex items-center gap-1 font-bold">
        <span class="material-symbols-outlined text-[16px]">upload</span> Upload Payment Proof Slip
      </button>
    </div>
  `;
}

function openSlipModal(orderNumber, depositAmount) {
  document.getElementById('slipOrderNumber').value = orderNumber;
  document.getElementById('slipOrderDisplay').value = orderNumber;
  document.getElementById('slipAmount').value = depositAmount ? depositAmount.toFixed(2) : '200.00';
  openModal('uploadSlipModal');
}

async function submitPaymentSlip(e) {
  e.preventDefault();
  const orderNum = document.getElementById('slipOrderNumber').value;
  const amount = document.getElementById('slipAmount').value;
  const bankRef = document.getElementById('slipBankRef').value;
  const fileInput = document.getElementById('slipFileInput');

  if (fileInput.files.length === 0) {
    showToast('Please select a payment slip file', 'error');
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  formData.append('category', 'payment_slips');
  formData.append('order_number', orderNum);
  formData.append('amount', amount);
  formData.append('bank_reference', bankRef);

  try {
    const res = await fetch('/api/upload', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    if (res.ok) {
      showToast('50% payment slip stored locally & submitted for review!', 'success');
      closeModal('uploadSlipModal');
      lookupOrder(orderNum);
      loadAdminOrders();
    } else {
      showToast(data.error || 'Failed to upload slip', 'error');
    }
  } catch (err) {
    showToast(err.message, 'error');
  }
}

function reorderFast(orderNumber) {
  fetch(`/api/orders/${orderNumber}`)
    .then(r => r.json())
    .then(order => {
      openCustomOrderModal(order.items[0]?.product_id || 1);
      document.getElementById('modalCustName').value = order.customer_name;
      document.getElementById('modalCustEmail').value = order.customer_email;
      document.getElementById('modalCustPhone').value = order.customer_phone || '';
      document.getElementById('modalOrderNotes').value = `Reorder based on ${orderNumber}. Same vector crest and cut specs.`;
      showToast(`Prefilled customizer with past order ${orderNumber} assets.`, 'info');
    });
}

function fetchTemplates() {
  fetch('/api/templates')
    .then(r => r.json())
    .then(templates => {
      window.cachedTemplates = templates;
    });
}

function openCdrTemplateVault(highlightCode = null) {
  const container = document.getElementById('cdrTemplateList');
  const templates = window.cachedTemplates || [];

  container.innerHTML = templates.map(t => {
    const zones = t.zones.zones || [];
    const meta = t.cdr_metadata || {};
    return `
      <div class="p-4 rounded-xl bg-surface-container border border-outline-variant/30 flex flex-col md:flex-row gap-4 justify-between">
        <div class="flex-1">
          <div class="flex items-center gap-2 mb-1">
            <span class="px-2 py-0.5 rounded bg-primary text-on-primary font-mono text-xs font-bold">${t.template_code}</span>
            <h4 class="font-title-md text-primary font-bold">${t.name}</h4>
          </div>
          <p class="text-xs text-on-surface-variant">Version: <strong>${meta.cdr_version || 'CorelDraw X7/2024'}</strong> • Color Profile: <strong>${meta.color_space || 'CMYK'}</strong> • Bleed: <strong>${meta.bleed_margin_mm || 15}mm</strong></p>
          <div class="mt-2 flex flex-wrap gap-1.5">
            ${zones.map(z => `<span class="px-2 py-0.5 rounded bg-surface-container-high text-[11px] text-primary font-mono">${z.name} (${z.max_w_mm}x${z.max_h_mm}mm)</span>`).join('')}
          </div>
        </div>
        <div class="flex md:flex-col justify-end items-end gap-2">
          <a href="${t.file_path || '#'}" download class="px-3 py-1.5 rounded bg-secondary text-on-secondary font-label-md text-xs uppercase flex items-center gap-1 hover:opacity-90 transition-opacity">
            <span class="material-symbols-outlined text-[16px]">download</span> Download .CDR
          </a>
          <button onclick="openCustomOrderModal()" class="px-3 py-1.5 rounded bg-surface-container-highest text-primary font-label-md text-xs uppercase hover:bg-outline-variant/30">
            Use in Mockup
          </button>
        </div>
      </div>
    `;
  }).join('');

  openModal('cdrTemplateModal');
}

// Staff / Admin Console functions
function loadAdminOrders() {
  fetch('/api/orders')
    .then(r => r.json())
    .then(orders => {
      document.getElementById('adminStatOrders').innerText = orders.length;
      document.getElementById('adminStatProduction').innerText = orders.filter(o => o.status === 'Production').length;
      const vol = orders.reduce((acc, o) => acc + (o.total_amount || 0), 0);
      document.getElementById('adminStatVolume').innerText = `$${vol.toFixed(0)}`;

      const list = document.getElementById('adminOrdersList');
      list.innerHTML = orders.map(o => `
        <div class="p-3.5 rounded-xl bg-surface-container border border-outline-variant/30">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono font-bold text-xs text-primary">${o.order_number}</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-surface-container-high text-primary">${o.status}</span>
          </div>
          <p class="text-xs font-semibold text-primary">${o.customer_name} <span class="text-outline font-normal">(${o.customer_email})</span></p>
          <div class="flex items-center justify-between text-xs text-outline mt-1">
            <span>Total: <strong class="text-primary font-mono">$${parseFloat(o.total_amount).toFixed(2)}</strong></span>
            <span>Deadline: <strong class="text-primary">${o.production_deadline || 'None'}</strong></span>
          </div>

          <!-- Quick Status Actions -->
          <div class="mt-3 pt-2 border-t border-outline-variant/20 flex flex-wrap items-center gap-1.5">
            <button onclick="adminChangeStatus('${o.order_number}', 'Received by ZAM')" class="px-2 py-1 rounded bg-surface-container-high text-[11px] font-semibold hover:bg-surface-container-highest">Mark Received</button>
            <button onclick="adminChangeStatus('${o.order_number}', 'Invoice Cleared')" class="px-2 py-1 rounded bg-surface-container-high text-[11px] font-semibold hover:bg-surface-container-highest">Clear Invoice</button>
            <button onclick="adminSetProduction('${o.order_number}')" class="px-2 py-1 rounded bg-secondary-container text-on-secondary-container text-[11px] font-bold">Start Production</button>
            <button onclick="adminSetDispatch('${o.order_number}')" class="px-2 py-1 rounded bg-primary text-on-primary text-[11px] font-bold">Dispatch</button>
          </div>
        </div>
      `).join('');
    });
}

function adminChangeStatus(orderNumber, status) {
  fetch(`/api/orders/${orderNumber}/status`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: status })
  })
  .then(r => r.json())
  .then(res => {
    showToast(res.message, 'success');
    loadAdminOrders();
    if (currentTrackingOrder && currentTrackingOrder.order_number === orderNumber) {
      lookupOrder(orderNumber);
    }
  });
}

function adminSetProduction(orderNumber) {
  const deadline = prompt(`Set Production Deadline for ${orderNumber} (e.g. 2026-11-20):`, '2026-11-20');
  if (!deadline) return;

  fetch(`/api/orders/${orderNumber}/status`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'Production', deadline: deadline })
  })
  .then(r => r.json())
  .then(res => {
    showToast(`Order ${orderNumber} in Production! Deadline set to ${deadline}.`, 'success');
    loadAdminOrders();
    lookupOrder(orderNumber);
  });
}

function adminSetDispatch(orderNumber) {
  const tracking = prompt(`Enter Courier Tracking Number for ${orderNumber} (e.g. DHL-EXP-889102):`, 'DHL-EXP-889102');
  if (!tracking) return;

  fetch(`/api/orders/${orderNumber}/status`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'Dispatched', tracking_number: tracking, courier: 'DHL Express' })
  })
  .then(r => r.json())
  .then(res => {
    showToast(`Order ${orderNumber} Dispatched via DHL (${tracking})!`, 'success');
    loadAdminOrders();
    lookupOrder(orderNumber);
  });
}
</script>
'''

html = html.replace('</body></html>', modals_and_scripts + '\n</body></html>')

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("public/index.html generated successfully with all interactive features.")
