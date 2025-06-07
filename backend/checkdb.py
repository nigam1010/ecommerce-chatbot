# view_products.py
import sqlite3
from config import DATABASE

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("SELECT id, name, category FROM products LIMIT 20")
rows = cursor.fetchall()

print("Sample products:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}")

conn.close()
