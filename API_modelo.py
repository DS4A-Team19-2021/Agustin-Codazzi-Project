import uvicorn
from fastapi import FastAPI
from typing import Optional
from typing import List
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd



class RandomForest_modelBase(BaseModel):

    """
    Clase utilizada para representar lo datos que vamos a usar

    ...

    Attributes
    ----------
    DRENAJE_NATURAL de tipo nominal categórica, cuyas variables dummies son:
        'DRENAJE_NATURAL_Bien_drenado',
        'DRENAJE_NATURAL_Excesivo',
        'DRENAJE_NATURAL_Imperfecto',
        'DRENAJE_NATURAL_Moderadamente_bien_drenado',
        'DRENAJE_NATURAL_Moderadamente_excesivo',
        'DRENAJE_NATURAL_Moderado',
        'DRENAJE_NATURAL_Muy_pobre',
        'DRENAJE_NATURAL_Pobre',
    CONTENIDO_CENIZA_VOLCANICA, categórica booleana toma valores true o false y sus dummies son:
        CONTENIDO_CENIZA_VOLCANICA_True
        CONTENIDO_CENIZA_VOLCANICA_False
    FAMILIA TEXTURAL, categoríca sus dummies son:
        'FAMILIA_TEXTURAL_Arcillosa',
        'FAMILIA_TEXTURAL_Arenosa',
        'FAMILIA_TEXTURAL_Disica',
        'FAMILIA_TEXTURAL_Esqueletica',
        'FAMILIA_TEXTURAL_Euica',
        'FAMILIA_TEXTURAL_Fina',
        'FAMILIA_TEXTURAL_Fragmental',
        'FAMILIA_TEXTURAL_Franca',
        'FAMILIA_TEXTURAL_Gruesa_sobre_fragmental',
        'FAMILIA_TEXTURAL_Hidrosa',
        'FAMILIA_TEXTURAL_Limosa',
        'FAMILIA_TEXTURAL_Medial',
    EPIPEDON, categórica sus dummies son:
        'EPIPEDON_Cambico',
        'EPIPEDON_Folistico',
        'EPIPEDON_Histico',
        'EPIPEDON_Melanico',
        'EPIPEDON_Molico',
        'EPIPEDON_Ocrico',
        'EPIPEDON_Umbrico',
        
    PROFUNDIDAD_MAXIMA, Variable numérica, float64
    ALTITUD, Variable numérica, float64
    H2_ESPESOR, Variable numérica, float64
    H1_RESULTADO_ph, Variable numérica, float64
    H1_ESPESOR, Variable numérica, float64


    """
    ALTITUD: float
    CONTENIDO_CENIZA_VOLCANICA: str
    DRENAJE_NATURAL: str
    EPIPEDON: str
    FAMILIA_TEXTURAL: str
    H1_ESPESOR: float
    H1_RESULTADO_ph: float
    H2_ESPESOR: float
    PROFUNDIDAD_MAXIMA: float
class RandomForest_modelList(BaseModel):
    """
    Esta clase se define para poder hacer consultas de muchas clases.
    Dado que aveces tenemos que predecir una gran cantidad de observaciones
    se hace necesario que haya la menor cantidad de conexiones pra así
    reducir la cantidad de llamados que se hacen, de esta forma lograr tener
    una respuesta más natural para la aplicacion

    """
    ALTITUD: List[float]
    CONTENIDO_CENIZA_VOLCANICA: List[str]
    DRENAJE_NATURAL: List[str]
    EPIPEDON: List[str]
    FAMILIA_TEXTURAL: List[str]
    H1_ESPESOR: List[float]
    H1_RESULTADO_ph: List[float]
    H2_ESPESOR: List[float]
    PROFUNDIDAD_MAXIMA: List[float]
    #data:List[RandomForest_modelBase]
    
    


# Load the pre trained model
filename = "CATS_pipeline.pk"
with open(filename,"rb") as f:
    loaded_model = pickle.load(f)
filename = "CATS_label_encoder.pk"
with open(filename,"rb") as f:
    label_encoder = pickle.load(f)

app = FastAPI()



# Use @app.get() decorator to define a GET request endpoint with the "main status and predict of the api"
@app.get("/api")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/api/status", "summary": "Estado de la API"},
            {"method": "POST", "path": "/api/predict", "predict": "Obtener una prediccion"},
            {"method": "POST", "path": "/api/predict_many", "predict": "Obtener predicciones de varias observaciones"}
        ]
    }

# Api status exposed on the /api/status endpoint
@app.get("/api/status")
def get_status():
    return {"status": "ok"}

# Use @app.post() decorator to define a POST request endpoint that lets passing a body on the request and returns a json
@app.post("/api/predict")
def predict_taxonomy(igac:RandomForest_modelBase):
    data = igac.dict()
    new_data=dict([(key,data[key]) for key in sorted(data)])
    df=pd.DataFrame(data=np.array(list(new_data.values())).reshape(1, -1),columns=list(new_data.keys()))
    prediction=loaded_model.predict(df)
    name_prediction=label_encoder.inverse_transform(prediction)[0]
    classes_names=label_encoder.inverse_transform(loaded_model.classes_.T)
    probability=zip(
        [str(classes) for classes in classes_names],loaded_model.predict_proba(df)[0])

    return {"prediction":name_prediction,"Probability":dict(probability)}

@app.post("/api/predict_many")
def predict_taxonomy_many(igac:RandomForest_modelList):
    data=igac.dict()
    new_data=dict([(key,data[key]) for key in sorted(data)])
    df=pd.DataFrame(new_data)
    prediction=loaded_model.predict(df)
    name_prediction=label_encoder.inverse_transform(prediction).tolist()
    classes_names=label_encoder.inverse_transform(loaded_model.classes_.T)
    probabilities=pd.DataFrame(loaded_model.predict_proba(df),columns=classes_names)
    #probability=[dict((classes,i) for classes in 
    #    label_encoder.inverse_transform(loaded_model.classes_.T))
    #     for i in loaded_model.predict_proba(pd.DataFrame(df)).tolist()]

    return {"predictions":name_prediction,"Probabilities":probabilities}

if __name__ == "__main__":

    # Run the app with uvicorn ASGI server asyncio frameworks. That basically responds to request on parallel and faster

    uvicorn.run("API_modelo:app", host="0.0.0.0", port=8000, reload=True)
