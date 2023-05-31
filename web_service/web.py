from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    products = requests.get('http://product:5000/').json()
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)