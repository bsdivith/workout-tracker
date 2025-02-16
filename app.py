from flask import Flask, request, jsonify
import main 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Exercise Tracker API!"})

@app.route("/track", methods=["POST"])
def track_exercise():
    """ Endpoint to log exercise data. """
    data = request.json
    if "query" not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    try:
        exercise_data = main.get_exercise_data(data["query"])
        log_result = main.log_to_sheet(exercise_data)
        return jsonify({"message": "Workout logged successfully!", "data": log_result})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
