import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(
        dbname="testdb",
        user="user",
        password="password",
        host="postgres-service",  # Kubernetes Service-namnet
        port="5432"
    )

def fetch_data():
    conn = get_connection()
    query = "SELECT * FROM data;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def insert_data(name, value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (name, value) VALUES (%s, %s);", (name, value))
    conn.commit()
    conn.close()
