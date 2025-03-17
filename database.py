import mysql.connector
from mysql.connector import Error
from functools import wraps

def connect_sql(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = None
        try:
            # Establish the database connection
            connection = mysql.connector.connect(
                host='34.143.201.40',
                database='industrial_robot',
                user='root',
                password='f67d2d008c6f8fb3f07cf6b1405e8bdb'
            )
            #xampp
            # connection = mysql.connector.connect(
            #     host='localhost',
            #     database='industrial_robot',
            #     user='root',
            #     password=''
            # )

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