from sqlalchemy import create_engine

host = 'historico.cu8inytluu1x.us-east-1.rds.amazonaws.com'
port = 5432
user = 'postgres'
password = 'datascience4all-equipo19'
database = 'postgres'
connDB = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
conn = connDB.raw_connection()
cur = conn.cursor()
