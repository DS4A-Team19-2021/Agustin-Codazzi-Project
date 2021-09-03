import pandas as pd
import unidecode
from apps.configuration import sqlconnect
from app import app

TIMEOUT = 240
from flask_caching import Cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 20
})



@cache.memoize(timeout=TIMEOUT)
def get_data(column_name):
    my_query = 'SELECT ' + '"' + '", "'.join(column_name) + '"' + ' FROM "SUELOS";'
    df=pd.read_sql_query(my_query ,sqlconnect.connDB)
    return df

#def get_data(column_name):
#    df=pd.read_csv("Datos_finales.csv",usecols =column_name , low_memory = True)
#    return df

def standarised_string(x):
    no_accents = unidecode.unidecode(x)
    return no_accents.replace("_"," ").lower().capitalize()


