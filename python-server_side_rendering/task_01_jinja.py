#!/usr/bin/python3
"""
Task 1: Creating a Basic HTML Template in Flask with Jinja.
"""

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
