from typing import Optional
from pydantic import BaseModel, Field
from joblib import dump, load
from model.predictive_model import predictQuality, createModel, parametersModel, scoreModel
from model.data_set import addWine


class Wine(BaseModel) :

    fixed_acidity : float = Field(..., ge = 0,
                                  title = "The fixed acidity of the wine",
                                  description = "The fixed acidity must be positive")
    volatile_acidity : float = Field(..., ge = 0,
                                     title = "The volatile acidity of the wine",
                                     description = "The volatile acidity must be positive")
    citric_acid : float = Field(..., ge = 0,
                                title = "The citric acid concentration of the wine",
                                description = "The citric acid must be positive")
    residual_sugar : float = Field(..., ge = 0,
                                   title = "The residual sugar concentration of the wine",
                                   description = "The residual sugar must be positive")
    chlorides : float = Field(..., ge = 0,
                              title = "The chlorides concentration of the wine",
                              description = "The chlorides must be positive")
    free_sulfur_dioxide : int = Field(..., ge = 0,
                                      title = "The free sulphites concentration of the wine",
                                      description = "The free sulfur dioxide must be positive")
    total_sulfur_dioxide : int = Field(..., ge = 0,
                                       title = "The free sulphites concentration and the sulphites concentration related to reaction with other molecules of the wine",
                                       description = "The total sulfur dioxide must be positive")
    density : float = Field(..., ge = 0,
                            title = "The density of the wine (g/L)",
                            description = "The density must be positive")
    ph : float = Field(..., ge = 0, le = 14,
                       title = "The acidity of the wine",
                       description = "The ph must be between zero and fourteen")
    sulphates : float = Field(..., ge = 0,
                              title = "The sulphates concentration of the wine",
                              description = "The sulphates must be positive")
    alcohol : float = Field(..., ge = 0,
                            title = "The alcohol level of the wine",
                            description = "The alcohol must be positive")
    quality : Optional[int] = Field(None, ge = 0, le = 10,
                                    title = "The quality of the wine",
                                    description = "The quality must be between zero and ten")
