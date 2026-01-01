#!/usr/bin/python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# تخزين المستخدمين في الذاكرة (فارغ بالبداية)
users = {}


@app.route("/", methods=["GET"])
def home():
    """الصفحة الرئيسية"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """حالة الـ API"""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """
    إرجاع قائمة بأسماء المستخدمين فقط
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    إرجاع بيانات مستخدم معين
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    إضافة مستخدم جديد عبر POST
    """
    # التحقق من أن الطلب يحتوي JSON صالح
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # التحقق من وجود username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # التحقق من عدم تكرار username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # إضافة المستخدم
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
