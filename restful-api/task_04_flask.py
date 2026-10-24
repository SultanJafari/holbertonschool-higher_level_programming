
#!/usr/bin/python3
"""Create a simple API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    """Return all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return a user by username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    user_data = request.get_json(silent=True)

    if not isinstance(user_data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
