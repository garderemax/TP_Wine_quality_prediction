# TP_Wine_quality_prediction
 
La qualité du vin étant assimilable à des classes notées de 0 à 10, nous avons choisi
d'avoir recour à une méthode classification. Nous avons essayé les modèles d'arbre de
décision, des k plus proches voisins et des machines à vecteurs de support.

Ce dernier modèle nous a apporté les meilleurs résultats lors de nos essais, est
relativement efficace pour les classes les plus extrémales et permet de tenir compte du
déséquilibre des classes présent dans les données.

Le choix des paramètres du noyaux et de la pénalité d'apprentissage c'est porté sur
ceux qui nous donnaient le score le plus élevé (le noyau gaussien était
significativement plus performant que les autres et la pénalité a été testée parmi
toutes celles possibles entre 0 et 2.5 avec un pas de 0.25).

Pour lancer le démarrage de l'API en local, il suffit d'utiliser la commande : python -m uvicorn main:app