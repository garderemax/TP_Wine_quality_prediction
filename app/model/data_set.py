# Librairies
import pandas as pd
from typing import List



# Constantes
FILE = "Wines.csv"



# Fonctions
def deleteId() :

    global FILE
    
    data = pd.read_csv(FILE)

    if "Id" in data.columns :

        data = data.drop("Id", axis = 1)
        data = data.drop_duplicates()
        data.to_csv(FILE, index = False)

# TO DO
def addWine(properties : List) :

    global FILE
    
    data = pd.read_csv(FILE)