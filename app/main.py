from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
requests_handled = 0

# Serve index.html directly from app/ folder
@app.route('/')
def home():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "requests_handled": requests_handled})

@app.route('/data', methods=['POST'])
def data():
    global requests_handled
    requests_handled += 1
    message = request.json.get("message", "")
    return jsonify({"message": "Data received", "current_count": requests_handled})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)