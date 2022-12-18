from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Wine(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

    quality: Optional[int]


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/api/predict")
async def post_predict(wine: Wine):
    return {"prediction": 10}

@app.get("/api/predict", response_model=Wine)
async def get_predict():
    wine = Wine()
    return wine

@app.get("/api/model")
async def get_model():
    return {"model": {}}

@app.get("/api/model/description")
async def get_model_description():
    return {"modelDescription": {}}

@app.put("/api/model")
async def put_model(wine: Wine):
    return {"wine": wine}

@app.post("/api/model/retrain")
async def post_model_retrain():
    return {"idk": 100}
