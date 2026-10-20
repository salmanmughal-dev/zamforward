import sqlite3

conn = sqlite3.connect('zamforward.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT id, order_number, status, total_amount, created_at FROM orders ORDER BY id DESC LIMIT 5")
rows = cursor.fetchall()

print(f"Total orders in DB: {len(rows)}")
for r in rows:
    print(dict(r))

last_id = rows[0]['id'] if rows else 0
next_seq = 400 + (last_id + 1)
print(f"Next sequential ZAM-ID will be: ZAM-{next_seq}-26")
conn.close()
