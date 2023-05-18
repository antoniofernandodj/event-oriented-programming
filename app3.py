import pymysql

# Establish a connection to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='antonio',
    password='senha123',
)

try:
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a simple SELECT query
    query = "create database example"
    cursor.execute(query)


finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
