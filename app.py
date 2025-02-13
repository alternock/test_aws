
from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/time')
def current_time():
    return jsonify({"time": datetime.now().isoformat()})

@app.route('/api/random')
def random_number():
    return jsonify({"number": random.randint(1, 100)})

if __name__ == '__main__':
    app.run(debug=True)
