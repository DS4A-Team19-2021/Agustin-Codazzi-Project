from sqlalchemy import create_engine

x=json.load(open("database_keys.json","r"))
host = x["host"]
port = x["port"]
user = x["user"]
password = x["password"]
database = x["database"]
connDB = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
conn = connDB.raw_connection()
cur = conn.cursor()
