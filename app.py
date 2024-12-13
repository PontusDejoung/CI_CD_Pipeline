from flask import Flask, request, jsonify
from db_setup import fetch_data, insert_data, get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Kubernetes with a Database!"

@app.route('/data', methods=['GET'])
def get_data():
    df = fetch_data()
    return df.to_json(orient="records")

@app.route('/data/sum', methods=['GET'])
def sum_values():
    df = fetch_data()
    total = df['value'].sum()
    return jsonify({"total_value": total})

@app.route('/data', methods=['POST'])
def add_data():
    name = request.json.get('name')
    value = request.json.get('value')
    insert_data(name, value)
    return jsonify({"message": "Data added successfully!"}), 201

@app.route('/dbtest', methods=['GET'])
def db_test():
    try:
        conn = get_connection()
        conn.close()
        return jsonify({"message": "Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error connecting to database: {e}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

