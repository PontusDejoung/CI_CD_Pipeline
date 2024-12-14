from flask import Flask, request, jsonify
import fastavro
from fastavro.schema import load_schema
import os

app = Flask(__name__)
app.config['DEBUG'] = True


import os
print(f"Current working directory: {os.getcwd()}")
print(f"Files in /app: {os.listdir('/app')}")

schema = load_schema('/app/data_schema.avsc')  

def write_to_avro(data):
    file_name = 'data.avro'
    with open(file_name, 'a+') as f:  
        writer = fastavro.writer(f, schema, data)

def read_from_avro():
    file_name = 'data.avro'

    if not os.path.exists(file_name):
        with open(file_name, 'wb') as f:
            pass

    data = []
    try:
        with open(file_name, 'rb') as f:
            reader = fastavro.reader(f, schema)
            for record in reader:
                data.append(record)
        print(f"Successfully read {len(data)} records from Avro file.")
    except ValueError as e:
        print(f"Error reading Avro file: {e}")
    except Exception as e:
        print(f"Unexpected error while reading Avro file: {e}")
    
    return data

def convert_to_utf8(data):
    """
    Försöker konvertera data till UTF-8 om det inte redan är i korrekt format.
    Om konverteringen misslyckas, returnerar den ett felmeddelande.
    """
    try:
        if isinstance(data, str):
            return data.encode('utf-8', 'ignore').decode('utf-8')
        elif isinstance(data, bytes):
        
            return data.decode('utf-8', 'ignore')
        else:
            return data
    except UnicodeDecodeError as e:
        print(f"Error decoding data: {e}")
        return None

@app.route('/')
def home():
    return "Hello, Flask with Avro!"

@app.route('/data', methods=['GET'])
def get_data():
    print("Attempting to fetch data from Avro file...")
    data = read_from_avro()
    print("Data fetched:", data)
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    try:
        name = request.json.get('name')
        value = request.json.get('value')

        name = convert_to_utf8(name)
        value = convert_to_utf8(value)

        # Logga de mottagna värdena
        print(f"Received data: name={name}, value={value}")
        
        if not name or not value:
            raise ValueError("Name and value are required!")

        new_data = [{"name": name, "value": value}]
        
        write_to_avro(new_data)

        print("Data written to Avro successfully.")
        
        return jsonify({"message": "Data added successfully!"}), 201
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"message": f"Error: {e}"}), 500


@app.route('/data/sum', methods=['GET'])
def sum_values():
    data = read_from_avro()
    total = sum(record['value'] for record in data)
    return jsonify({"total_value": total})

