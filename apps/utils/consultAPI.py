import requests
import pandas as pd
import json

def extract_data_to_predict(x):
    uso = [ 'ALTITUD','CONTENIDO_CENIZA_VOLCANICA','DRENAJE_NATURAL','EPIPEDON',  'FAMILIA_TEXTURAL', 'H1_ESPESOR', 'H1_RESULTADO_ph','H2_ESPESOR',
           'PROFUNDIDAD_MAXIMA']
    return x[uso]

def get_predictions(df):
    new_df=df.copy()
    url = 'http://0.0.0.0:8000/api/predict_many'
    data = extract_data_to_predict(new_df)
    x = requests.post(url,data=json.dumps(data.to_dict(orient="list")))
    new_df["ORDEN"]=pd.Series(x.json()["predictions"],name="ORDER")
    #print(new_df["ORDEN"])
    return new_df


#df=pd.read_csv("/Users/jamontanac/Documents/DS4A/Agustin-Codazzi-Project/Datos_finales.csv").drop(columns="ORDEN").sample(10)
#print(df.columns,len(df.columns))
#a=get_predictions(df)
#print(a)
#print(a.columns,len(a.columns))


#print(data)


