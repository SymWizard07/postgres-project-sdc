# app.py
import psycopg2
from psycopg2 import sql
import random

# Connection settings (match docker-compose.yml)
DB_NAME = "demo_db"
DB_USER = "demo_user"
DB_PASSWORD = "demo_pass"
DB_HOST = "localhost"  # Docker exposes PostgreSQL on localhost

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

def main():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id SERIAL PRIMARY KEY,
            description TEXT,
            num INTEGER
        );
    """)
    
    # Insert demo data
    random_number = random.randint(0, 100)
    cursor.execute(
        "INSERT INTO data (description, num) VALUES (%s, %s);",
        ("Random number", random_number)
    )
    
    # Query data
    cursor.execute("SELECT * FROM data;")
    print("Data:", cursor.fetchall())
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()