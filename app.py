from flask import Flask, request, jsonify
from db_setup import fetch_data, insert_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Kubernetes with a Database!"

@app.route('/data', methods=['GET'])
def get_data():
    df = fetch_data()
    return df.to_json(orient="records")

@app.route('/data', methods=['POST'])
def add_data():
    name = request.json.get('name')
    value = request.json.get('value')
    insert_data(name, value)
    return jsonify({"message": "Data added successfully!"}), 201
