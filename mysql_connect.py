import pymysql
from config import config_mysql


def connect():

    # init
    connection = None

    try:
        params = config_mysql()
        
        # Establishing the connection
        connection = pymysql.connect(
            host=params['host'],
            port=int(params['port']),
            user=params['user'],
            password=params['password'],
            database=params['database'],
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Connection successful!")

        # Creating a cursor object
        with connection.cursor() as cursor:
            # Define the SQL query
            sql_query = "SELECT * FROM PERSONS"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch all the rows
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL Platform: {e}")

    finally:
        if connection:
            connection.close()
            print("Connection closed.")

if __name__ == '__main__':
    
    connect()
