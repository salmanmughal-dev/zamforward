with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

modal_start = text.find('id="aiStudioModal"')
tag_start = text.rfind('<div', 0, modal_start)
next_comment = text.find('<!-- 2. INVOICE MODAL', modal_start)
print(f"Modal tag starts at: {tag_start}")
print(f"Next comment starts at: {next_comment}")
print("Snippet before next comment:")
print(text[next_comment-150:next_comment])

# Now check the script
script_start = text.find('// ------------------- HIGH FIDELITY THREE.JS 3D ENGINE')
if script_start == -1:
    script_start = text.find('function openAiStudioModal')
print(f"Script starts around: {script_start}")
print(text[script_start-50:script_start+200])

# Where does the studio script end?
# Let's see what comes after the studio script
next_script_marker = text.find('// Global lookupOrder hook', script_start)
if next_script_marker == -1:
    next_script_marker = text.find('/* ZamForward Navbar', script_start)
print(f"Next script marker at: {next_script_marker}")
print("Snippet around next marker:")
print(text[next_script_marker-150:next_script_marker+150])
