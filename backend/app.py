# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from config import DATABASE

app = Flask(__name__)
CORS(app)

@app.route('/api/products', methods=['GET'])
def get_products():
    query = request.args.get('query', '').lower()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products 
        WHERE LOWER(name) LIKE ? 
           OR LOWER(category) LIKE ? 
           OR LOWER(description) LIKE ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%"))

    rows = cursor.fetchall()
    conn.close()

    products = [{
        'id': row[0],
        'name': row[1],
        'category': row[2],
        'price': row[3],
        'description': row[4],
        'stock': row[5]
    } for row in rows]

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
