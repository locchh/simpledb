'''
[postgres.ini] --> [config.py] --> [postgres_engine.py]
'''
import pandas as pd
from config import config_mysql
from sqlalchemy import create_engine

if __name__ == "__main__":

    params = config_mysql()

    uri = f"mysql+pymysql://{params['user']}:{params['password']}@{params['host']}/{params['database']}"
    print('uri=',uri)

    engine = create_engine(uri)

    query = 'SELECT * FROM PERSONS'

    df = pd.read_sql(query, engine)

    print(df)