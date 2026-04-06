from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"})

@app.route("/data", methods=["POST"])
def data():
    return jsonify({"received": request.json})

if __name__ == "__main__":
    print("Starting Flask app...")   # <-- debug line
    app.run(host="0.0.0.0", port=5000)
