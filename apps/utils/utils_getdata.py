import pandas as pd
import unidecode

def get_data(column_name):
       df=pd.read_csv("otro_test.csv",
                   usecols =column_name , low_memory = True)
       return df

def standarised_string(x):
    no_accents = unidecode.unidecode(x)
    return no_accents.replace("_"," ").lower().capitalize()

