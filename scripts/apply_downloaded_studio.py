import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Read the new modal HTML from Download file 1
with open(r'c:\Users\SALMAN\Downloads\gemini-code-1792480566682.html', 'r', encoding='utf-8', errors='ignore') as f:
    new_modal_html = f.read().strip()

# 2. Read the new engine script from Download file 2
with open(r'c:\Users\SALMAN\Downloads\gemini-code-1792480570142.html', 'r', encoding='utf-8', errors='ignore') as f:
    new_script_js = f.read().strip()

print(f"Loaded new modal HTML: {len(new_modal_html)} bytes")
print(f"Loaded new script JS: {len(new_script_js)} bytes")

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # --- A. Replace the modal HTML ---
    # Find start of aiStudioModal
    m_marker = '<!-- ================= AI 3D STUDIO FULL-SCREEN WORKSPACE MODAL ================= -->'
    pos_m_start = content.find(m_marker)
    if pos_m_start == -1:
        # fallback search for id="aiStudioModal"
        pos_id = content.find('id="aiStudioModal"')
        pos_m_start = content.rfind('<div', 0, pos_id)
    
    # Find end of aiStudioModal (right before MODALS & SLIDEOUT PANELS)
    end_marker = '<!-- ================= MODALS & SLIDEOUT PANELS ================= -->'
    pos_m_end = content.find(end_marker)
    if pos_m_end == -1:
        # fallback search for customOrderModal
        pos_custom = content.find('id="customOrderModal"')
        pos_m_end = content.rfind('<!--', 0, pos_custom)
    
    if pos_m_start != -1 and pos_m_end != -1:
        print(f"[{filename}] Replacing modal HTML from {pos_m_start} to {pos_m_end}")
        content = content[:pos_m_start] + new_modal_html + '\n\n' + content[pos_m_end:]
    else:
        print(f"[{filename}] ERROR: Could not locate modal boundaries: start={pos_m_start}, end={pos_m_end}")
        return False
    
    # --- B. Replace the studio engine script ---
    # Find start of old studio script
    s_marker = '/* =========================================================================\n   ZAMFORWARD AI 3D STUDIO & CDR PATTERN ENGINE (HIGH FIDELITY)'
    pos_s_start = content.find(s_marker)
    if pos_s_start != -1:
        # Find the <script> tag opening right before it
        pos_s_start = content.rfind('<script', 0, pos_s_start)
    else:
        # Fallback to search function openAiStudioModal
        fn_pos = content.find('function openAiStudioModal')
        pos_s_start = content.rfind('<script', 0, fn_pos)
    
    # Find end of old studio script: right before Order Tracker Engine
    tracker_marker = '/* ---------- Order Tracker Engine (Live SQLite API + Fallback Cache) ---------- */'
    pos_tracker = content.find(tracker_marker)
    if pos_tracker != -1:
        # Find </script> right before pos_tracker
        pos_s_end = content.rfind('</script>', pos_s_start, pos_tracker) + len('</script>')
    else:
        # Fallback search for lookupOrder
        lookup_pos = content.find('function lookupOrder')
        pos_s_end = content.rfind('</script>', pos_s_start, lookup_pos) + len('</script>')
    
    if pos_s_start != -1 and pos_s_end != -1:
        print(f"[{filename}] Replacing script JS from {pos_s_start} to {pos_s_end}")
        content = content[:pos_s_start] + new_script_js + '\n\n' + content[pos_s_end:]
    else:
        print(f"[{filename}] ERROR: Could not locate script boundaries: start={pos_s_start}, end={pos_s_end}")
        return False
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[{filename}] Successfully updated! New size: {len(content)} bytes")
    return True

# Update code.html and public/index.html
ok1 = update_file('code.html')
ok2 = update_file('public/index.html')

if ok1 and ok2:
    print("\nALL FILES SUCCESSFULLY UPDATED WITH NEW DESIGN FEATURE!")
