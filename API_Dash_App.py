import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from typing import Optional
from Dash_IGAC.index import create_dash_app
from pydantic import BaseModel
from Dash_IGAC.callbacks import register_callbacks
import pickle
import numpy as np

app = FastAPI()

@app.get("/api")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/api/status", "summary": "App status"},
            {"method": "POST", "path": "/api/predict", "predict": "Get prediction"},
        ]
    }

@app.get("/api/status")
def get_status():
    return {"status": "ok"}

dash_app = create_dash_app(routes_pathname_prefix="/")
register_callbacks(dash_app)
app.mount("/", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":

    # Run the app with uvicorn ASGI server asyncio frameworks. That basically responds to request on parallel and faster

    uvicorn.run("API_Dash_App:app", host="0.0.0.0", port=8000, reload=True,log_level="info")

