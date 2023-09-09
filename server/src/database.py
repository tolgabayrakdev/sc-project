import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="root",
        password="root",
        host="localhost",
        port="5432"
    )
    return connection
