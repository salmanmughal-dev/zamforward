with open(r'c:\Users\SALMAN\Downloads\gemini-code-1792480570142.html', 'r', encoding='utf-8', errors='ignore') as f:
    js_text = f.read()

funcs = [
    'openAiStudioModal',
    'closeAiStudioModal',
    'initStudio2DCanvas',
    'initThreeJS3D',
    'setStudioGarment',
    'update3DTexture',
    'handleStudioLogoUpload',
    'submitStudioOrder'
]

for fn in funcs:
    print(f"'{fn}' in new JS: {fn in js_text}")
