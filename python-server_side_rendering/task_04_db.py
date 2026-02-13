from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# قراءة JSON
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

# قراءة CSV
def read_csv_file(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

# قراءة من SQLite
def read_sqlite_db(db_file):
    products = []
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite database: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products_list = []

    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    elif source == 'sql':
        products_list = read_sqlite_db('products.db')
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        filtered = [p for p in products_list if p['id'] == product_id]
        if filtered:
            products_list = filtered
        else:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
