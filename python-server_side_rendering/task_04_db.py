#!/usr/bin/python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask.
"""

import json
import csv
import sqlite3
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(file_path):
    """Reads product data from a JSON file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []


def read_csv_file(file_path):
    """Reads product data from a CSV file."""
    products = []
    if not os.path.exists(file_path):
        return products
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                except ValueError:
                    pass
                try:
                    row['price'] = float(row['price'])
                except ValueError:
                    pass
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products


def read_sqlite_db(db_path):
    """Reads product data from a SQLite database."""
    products = []
    if not os.path.exists(db_path):
        return products
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Enables column access by name
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                items_list = data.get("items", [])
        except Exception as e:
            print(f"Error reading JSON file: {e}")
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Handles product retrieval from JSON, CSV, or SQLite with optional filtering by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    error_msg = None
    product_list = []

    if source == 'json':
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        product_list = read_json_file(file_path)
    elif source == 'csv':
        file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        product_list = read_csv_file(file_path)
    elif source == 'sql':
        db_path = os.path.join(os.path.dirname(__file__), 'products.db')
        product_list = read_sqlite_db(db_path)
    else:
        error_msg = "Wrong source"

    # If source is valid, filter by id if provided
    if not error_msg and product_id is not None:
        try:
            target_id = int(product_id)
        except ValueError:
            target_id = product_id

        filtered_products = [
            p for p in product_list
            if int(p.get('id', 0)) == target_id or str(p.get('id')) == str(product_id)
        ]

        if not filtered_products:
            error_msg = "Product not found"
        else:
            product_list = filtered_products

    return render_template('product_display.html', products=product_list, error=error_msg)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
