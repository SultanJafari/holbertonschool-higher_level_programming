#!/usr/bin/python3
"""
Task 3: Reading Data from JSON or CSV Files in Flask with Query Parameters.
"""

import json
import csv
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
                # Convert types for consistency
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
    """Handles product retrieval from JSON or CSV with optional filtering by id and error handling."""
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
