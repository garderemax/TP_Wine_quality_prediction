# Librairies
import pandas as pd
from sklearn.svm import SVC
from typing import List

from model.data_set import FILE

# Constantes
C = 1.75

# Fonctions
def createModel() :

    global FILE, C
    
    data = pd.read_csv(FILE)

    X = data.iloc[:, :-1]
    Y = data.iloc[:, -1]

    clf = SVC(C = C, gamma = "auto", class_weight = "balanced")
    clf.fit(X, Y)

    return clf

def parametersModel(model : SVC) :

    support_vectors = model.support_vectors_.tolist()

    dual_coef = model.dual_coef_.tolist()

    kernel = "Gaussian radial basis function"
    gamma = 1/model.n_features_in_

    intercept = model.intercept_.tolist()

    parameters = {"support vectors" : support_vectors,
                  "dual coefficients" : dual_coef, "kernel" : kernel,
                  "gamma" : gamma, "interception" : intercept}
    
    return parameters

def scoreModel(model : SVC) :

    global FILE
    
    data = pd.read_csv(FILE)

    X = data.iloc[:, :-1]
    Y = data.iloc[:, -1]

    score = {"score" : model.score(X, Y)}

    return score

def predictQuality(model : SVC, properties : List) :

    quality = model.predict(properties)

    return quality