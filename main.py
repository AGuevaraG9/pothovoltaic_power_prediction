from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from routers import photovoltaic

app = FastAPI(
    title="Photovoltaic Power Prediction API",
    description="API para prediccion de potencia fotovoltaica usando Machine Learning, FastAPI y SQLAlchem.",
    version="1.0.0",
)

app.include_router(photovoltaic.router)

@app.get("/")
def index():
    return {
        "title": "FASTAPI PHOTOVOLTAIC_PREDICTION API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }
    
Base.metadata.create_all(engine)
