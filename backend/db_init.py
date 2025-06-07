# db_init.py
import sqlite3
import random
from faker import Faker
from models import create_tables
from config import DATABASE

fake = Faker()

def generate_mock_products(n=100):
    categories = ['Electronics', 'Books', 'Textiles']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    for _ in range(n):
        name = fake.catch_phrase()
        category = random.choice(categories)
        price = round(random.uniform(10, 500), 2)
        description = fake.text(max_nb_chars=100)
        stock = random.randint(1, 100)

        cursor.execute('''
            INSERT INTO products (name, category, price, description, stock)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, category, price, description, stock))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    generate_mock_products()
