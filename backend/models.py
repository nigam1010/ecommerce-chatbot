# models.py
import sqlite3
from config import DATABASE

def create_tables():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            price REAL,
            description TEXT,
            stock INTEGER
        )
    ''')
    conn.commit()
    conn.close()
