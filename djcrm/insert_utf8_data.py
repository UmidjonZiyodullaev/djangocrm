import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Establish a connection to the database with UTF-8 encoding
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    options='-c client_encoding=UTF8'
)

# Create a cursor object
cur = conn.cursor()

# Insert UTF-8 encoded data
utf8_data = "Тестовые данные"
cur.execute("INSERT INTO test_encoding (data) VALUES (%s)", (utf8_data,))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
