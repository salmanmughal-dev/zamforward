with open(r'c:\Users\SALMAN\Downloads\gemini-code-1792480566682.html', 'r', encoding='utf-8', errors='ignore') as f:
    html1 = f.read()

print("File 1 length:", len(html1))
print("First 500 chars:")
print(html1[:500])
print("\n--- Middle 500 chars ---")
print(html1[len(html1)//2 : len(html1)//2 + 500])
print("\n--- Last 500 chars ---")
print(html1[-500:])
