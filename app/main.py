from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simple in-memory store
data_store = []

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running", "requests_handled": len(data_store)})

@app.route("/data", methods=["POST"])
def post_data():
    try:
        payload = request.json
        data_store.append(payload)
        return jsonify({"message": "Data received", "current_count": len(data_store)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Run app with host 0.0.0.0 to be accessible in container
    app.run(host="0.0.0.0", port=5000, threaded=True)