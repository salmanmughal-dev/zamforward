import sqlite3
import re

# 1. Update public/index.html and code.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Card 2 image
target_card2 = '''<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAY1r2qM1B994s91o1676v2T4iYc3k_1o6h7m-89cf7qSvgO2pjHkh-p3vEPnz-dTrM8-r-wKou4jPi7YBu9QlSvHjoj3dNr-S7YDinn_1eFfGnriWlelCrl8Xuy3a_b7zt_qIw5uawbEdlBy98oUjGRiJM7vapnasd3egmRmQ-SokmnXdFgZpzknlL_jnqKO5eX-d3ovY4q4o8kXJHX_IV2BhQFmbgWULCLnX-ZVMVnu27iqqTfjQ" alt="Apex Combat MMA Shorts"/>'''
replacement_card2 = '''<img class="w-full h-full object-cover object-center transition-transform duration-500 group-hover:scale-105" src="/images/PRODUCT.jpeg" alt="Apex Combat MMA Shorts"/>'''

if target_card2 in text:
    text = text.replace(target_card2, replacement_card2)
    print("Replaced Card 2 image with /images/PRODUCT.jpeg")
else:
    # fallback regex
    text = re.sub(
        r'<img class="w-full h-full object-cover[^"]*" src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuAY1r2qM1B994s91o1676[^"]*" alt="Apex Combat MMA Shorts"/>',
        replacement_card2,
        text
    )
    print("Replaced Card 2 with regex")

# Replace Card 3 image
target_card3 = '''<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600" alt="BJJ Competition Gi"/>'''
replacement_card3 = '''<img class="w-full h-full object-cover object-center transition-transform duration-500 group-hover:scale-105" src="/images/PRODUCT.jpeg" alt="BJJ Competition Gi"/>'''

if target_card3 in text:
    text = text.replace(target_card3, replacement_card3)
    print("Replaced Card 3 image with /images/PRODUCT.jpeg")
else:
    text = text.replace('https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600', '/images/PRODUCT.jpeg')
    print("Replaced Card 3 url fallback")

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update SQLite database products table for MMA Shorts and BJJ Gi
conn = sqlite3.connect('zamforward.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE products 
SET image_url = '/images/PRODUCT.jpeg'
WHERE sku IN ('ZAM-MMA-SH-01', 'ZAM-BJJ-GI-01') OR id IN (3, 4)
''')
conn.commit()

# Verify updated rows in SQLite
rows = cursor.execute('SELECT id, name, sku, image_url FROM products WHERE id IN (1, 3, 4)').fetchall()
for r in rows:
    print("Database row:", r)

conn.close()
print("All product cards and database records updated successfully.")
