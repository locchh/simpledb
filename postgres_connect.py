'''
[postgres.ini] --> [config.py] --> [postgres_connect.py]
'''
import pandas
import psycopg2
from config import config_postgres

def connect():
    # init
    connection = None

    try:    
        params = config_postgres()
        print('Connecting to postgresql database...')
        
        # create the connection
        connection = psycopg2.connect(**params)
        
        # create a cursor
        cursor = connection.cursor()
        
        # query by cursor
        print('Postgresql database version: ')
        query = 'SELECT version()'
        cursor.execute(query)
        db_version = cursor.fetchone()
        print(db_version)

        # select all table
        print('Get table PERSONS')
        query = 'SELECT * FROM PERSONS;'
        cursor.execute(query)
        outputs = cursor.fetchall()
        print(outputs)

        # close the cursor
        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error:',error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated')

if __name__ == "__main__":
    
    connect()
