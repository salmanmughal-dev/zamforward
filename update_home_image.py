with open('public/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''<div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="https://lh3.googleusercontent.com/aida-public/AB6AXuB0bh0920oDUW-DNllDkVgJHiLrVgCYZ1U9cpr5N63qaBsUAtRT3sFYzf9BVo3te9auHuUQN7s4M4SvKVBOjYOP6Qj6lb4U1-Tzh9OAsOZOuRxyOIVWldqggpafh8WCojkZKWozMX2EuTcS5LLeG804jVS_l-8ysyiLJmRx41ByWm7fks1csoTcV0MK1jokTkVCpcpPxJeYvTpTqqej6O26WVpjeSWahMf_SCPs8MjdrTD2rDDzkaw"/>'''

replacement = '''<div class="aspect-[4/5] w-full overflow-hidden relative">
              <img class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105" 
                   alt="ZamForward Pro Compression Combat Apparel" 
                   src="/images/home-page.jpg"/>'''

if target in text:
    text = text.replace(target, replacement)
    print("Replaced target with /images/home-page.jpg")
else:
    # fallback search
    import re
    text = re.sub(
        r'<div class="aspect-\[4/5\].*?src="https://lh3\.googleusercontent\.com[^"]+"',
        '<div class="aspect-[4/5] w-full overflow-hidden relative">\n              <img class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105" alt="ZamForward Pro Compression Combat Apparel" src="/images/home-page.jpg"',
        text,
        count=1,
        flags=re.DOTALL
    )
    print("Replaced with regex")

# Also ensure bullet character is clean
text = text.replace('450 GSM Poly-Spandex  Anti-slip silicone waist', '450 GSM Poly-Spandex • Anti-slip silicone waist')

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated public/index.html and code.html successfully.")
