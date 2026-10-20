import sqlite3

# 1. Update public/index.html and code.html
with open('public/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the image src for Card 1 (Apex Sublimated Short-Sleeve Rashguard)
old_img = 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600'
new_img = '/images/PRODUCT.jpeg'

# In Card 1:
old_card_img = '''<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600" alt="Apex Pro Rashguard"/>'''
new_card_img = '''<img class="w-full h-full object-cover object-center transition-transform duration-500 group-hover:scale-105" src="/images/PRODUCT.jpeg" alt="Apex Pro Rashguard"/>'''

if old_card_img in text:
    text = text.replace(old_card_img, new_card_img)
    print("Replaced Card 1 image with /images/PRODUCT.jpeg")
else:
    text = text.replace(old_img, new_img)
    print("Replaced occurrences of old_img with /images/PRODUCT.jpeg")

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update SQLite database products table
conn = sqlite3.connect('zamforward.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE products 
SET image_url = '/images/PRODUCT.jpeg'
WHERE id = 1 OR sku = 'ZAM-RG-SS-01'
''')
conn.commit()

# Also verify updated row
updated_row = cursor.execute('SELECT id, name, sku, image_url FROM products WHERE id = 1').fetchone()
print("Updated database row 1:", updated_row)

conn.close()
print("Updated public/index.html, code.html, and SQLite database successfully.")
