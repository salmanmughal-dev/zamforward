import sys

old_header_btn = """<button onclick="submitStudioOrder()" class="px-4 py-2 rounded-xl bg-[#088395] hover:bg-[#066c7b] text-white text-xs font-bold uppercase tracking-wider transition-all shadow-lg flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">rocket_launch</span>
        <span>Lock Specs &amp; Order</span>
      </button>"""

new_header_btn = """<button onclick="lockSpecsAndOrder()" id="btnLockSpecsHeader" class="px-4 py-2 rounded-xl bg-[#088395] hover:bg-[#066c7b] text-white text-xs font-bold uppercase tracking-wider transition-all shadow-lg flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">lock_clock</span>
        <span>Lock Specs &amp; Order</span>
      </button>"""

old_aside_btn = """<button onclick="openOrderFileReviewModal()" class="px-5 py-2.5 rounded-xl bg-[#088395] text-white text-xs uppercase font-bold hover:bg-[#066c7b] transition-all shadow-md flex items-center gap-1.5 group">
          <span class="material-symbols-outlined text-[16px]">lock_clock</span>
          <span>Lock &amp; Specs</span>
        </button>"""

new_aside_btn = """<button onclick="lockSpecsAndOrder()" id="btnLockSpecsAndOrder" class="px-5 py-2.5 rounded-xl bg-[#088395] text-white text-xs uppercase font-bold hover:bg-[#066c7b] transition-all shadow-md flex items-center gap-1.5 group">
          <span class="material-symbols-outlined text-[16px]">lock_clock</span>
          <span>Lock Specs &amp; Order</span>
        </button>"""

js_func_hook = """function openOrderFileReviewModal() {"""
new_js_func = """function lockSpecsAndOrder() {
  const patternCanvas = document.getElementById('studio2DCanvas');
  let snapshot = '';
  if (patternCanvas) {
    try {
      snapshot = patternCanvas.toDataURL('image/jpeg', 0.85);
    } catch (e) {
      console.warn('Canvas snapshot export:', e);
    }
  }

  const orderFilePayload = {
    ...studioState,
    snapshotData: snapshot,
    timestamp: Date.now()
  };

  try {
    localStorage.setItem('zam_order_file_state', JSON.stringify(orderFilePayload));
  } catch (e) {
    console.warn('LocalStorage error:', e);
  }

  window.location.href = '/order-file';
}

function openOrderFileReviewModal() {"""

modal_header_hook = """<span class="px-2 py-0.5 rounded bg-[#088395] text-white font-mono text-[10px] uppercase font-bold">FR-5 Spec</span>"""
modal_header_new = """<span class="px-2 py-0.5 rounded bg-[#088395] text-white font-mono text-[10px] uppercase font-bold">FR-5 Spec</span>
            <a href="/order-file" class="ml-2 px-2.5 py-0.5 rounded bg-white/10 hover:bg-white/20 text-white font-mono text-[10px] uppercase font-bold flex items-center gap-1 transition-all">
              <span>Open Standalone Page</span>
              <span class="material-symbols-outlined text-[12px]">open_in_new</span>
            </a>"""

for fname in ['code.html', 'public/index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    assert old_header_btn in content, f'old_header_btn not found in {fname}'
    assert old_aside_btn in content, f'old_aside_btn not found in {fname}'
    assert js_func_hook in content, f'js_func_hook not found in {fname}'

    content = content.replace(old_header_btn, new_header_btn, 1)
    content = content.replace(old_aside_btn, new_aside_btn, 1)
    content = content.replace(js_func_hook, new_js_func, 1)
    if modal_header_hook in content:
        content = content.replace(modal_header_hook, modal_header_new, 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Successfully updated {fname}')
