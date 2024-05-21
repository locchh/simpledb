'''
[postgres.ini] --> [config.py] --> [postgres_engine.py]
'''
import pandas as pd
from config import config_postgres
from sqlalchemy import create_engine

if __name__ == "__main__":

    params = config_postgres()

    # uri = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    uri = f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    print('uri=',uri)

    engine = create_engine(uri)

    query = 'SELECT * FROM PERSONS'

    df = pd.read_sql(query, engine)

    print(df)