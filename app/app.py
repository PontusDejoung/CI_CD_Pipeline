from flask import Flask, request, jsonify
import fastavro
from fastavro.schema import load_schema
import os

app = Flask(__name__)


schema = load_schema('data_schema.avsc')  

def write_to_avro(data):
    file_name = 'data.avro'
    with open(file_name, 'ab') as f:  
        writer = fastavro.writer(f, schema, data)

def read_from_avro():
    file_name = 'data.avro'
    data = []
    with open(file_name, 'rb') as f:
        reader = fastavro.reader(f, schema)
        for record in reader:
            data.append(record)
    return data

@app.route('/')
def home():
    return "Hello, Flask with Avro!"

@app.route('/data', methods=['GET'])
def get_data():
    data = read_from_avro()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    name = request.json.get('name')
    value = request.json.get('value')

    new_data = [{"name": name, "value": value}]
    
    write_to_avro(new_data)
    
    return jsonify({"message": "Data added successfully!"}), 201

@app.route('/data/sum', methods=['GET'])
def sum_values():
    data = read_from_avro()
    total = sum(record['value'] for record in data)
    return jsonify({"total_value": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
