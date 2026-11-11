#!/usr/bin/python3
"""
Task 2: Dynamic Template with Loops and Conditions in Flask.
"""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Reads items from items.json and renders them dynamically."""
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
