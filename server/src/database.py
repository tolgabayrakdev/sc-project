from psycopg2 import connect

def get_cursor():
    conn = connect(
        host="localhost",
        database="postgres",
        user="root",
        password="root"
    )
    return conn.cursor()