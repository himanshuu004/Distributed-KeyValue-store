from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
store = {}

@app.route('/get/<key>', methods=['GET'])
def get(key):
    return jsonify({"value": store.get(key)})

@app.route('/put', methods=['POST'])
def put():
    data = request.json
    store[data["key"]] = data["value"]
    return jsonify({"status": "success"})

def run_server(port):
    app.run(port=port)

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1])  # Pass port like: `python server.py 5000`
    run_server(port)