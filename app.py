from flask import Flask, request, jsonify
import os
import main  # Import main.py logic

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Exercise Tracker API is running!"})

@app.route("/track", methods=["POST"])
def track_exercise():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    os.environ["USER_QUERY"] = data["query"]  # Pass input to main.py

    # Run main.py
    exec(open("main.py").read())

    return jsonify({"message": "Workout logged successfully!"}), 200

if __name__ == "__main__":
    app.run()
