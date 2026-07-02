import os
import mysql.connector
from mysql.connector import Error
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

def connect_sql(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = None
        try:
            # Establish the database connection
            connection = mysql.connector.connect(
                host=os.environ['DB_HOST'],
                database=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD']
            )

            if connection.is_connected():
                print("Connected to MySQL Server")
                # Pass the connection and cursor to the decorated function
                cursor = connection.cursor()
                result = func(cursor, *args, **kwargs)  # Execute the decorated function
                connection.commit()  # Commit changes if any data was modified
                return result

        except Error as e:
            print(f"Database error: {e}")

        finally:
            # Clean up the connection
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("Disconnected from MySQL")

    return wrapper