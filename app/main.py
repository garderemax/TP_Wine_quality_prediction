from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional, Dict
from joblib import dump, load

from model.wine import Wine
import model.predictive_model as predictive_model


app = FastAPI()

@app.post("/api/predict")
async def predict_quality(wine: Wine = Body(..., embed = True)) -> int:
    model = load("model/model.joblib")

    dict_wine = wine.__dict__
    properties = [dict_wine["fixed_acidity"], dict_wine["volatile_acidity"],
                  dict_wine["citric_acid"], dict_wine["residual_sugar"],
                  dict_wine["chlorides"], dict_wine["free_sulfur_dioxide"],
                  dict_wine["total_sulfur_dioxide"], dict_wine["density"],
                  dict_wine["ph"], dict_wine["sulphates"], dict_wine["alcohol"]]

    quality = predictive_model.predictQuality(model, properties)

    return quality

@app.get("/api/predict")
async def perfect_win():

    model = load("model/model.joblib")
    wine = perfectWine(model)

    return wine

@app.get("/api/model")
async def get_model() -> str:

    model = createModel()
    dump(model, "model/model.joblib")

    return "Done"

@app.get("/api/model/description")
async def get_model_description() -> Dict:

    model = load("model/model.joblib")

    parameters = parametersModel(model)
    score = scoreModel(model)

    description = {**parameters, **score}

    return description

@app.put("/api/model")
async def add_wine(wine : Wine = Body(..., embed = True)) -> str:

    properties = wine.__dict__
    addWine(properties)

    return "Done"

@app.post("/api/model/retrain")
async def retrain_model() -> str:

    model = createModel()
    dump(model, "model/model.joblib")

    return "Done"
