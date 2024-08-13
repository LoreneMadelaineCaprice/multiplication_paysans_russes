import math 
import pandas as pd #permet manipuler tableaux
n1 = 89
n2 = 18

moitie = [n1] #colonne moitie
double = [n2] #colonne double
print(math.floor(moitie[0]/2)) #math.floor renvoie le nombre entier inférieur

while(min(moitie) > 1): #chaque itération calcule la valeur suivante de la colonne moitié jusqu'à moitié=1
    moitie.append(math.floor(min(moitie)/2))

while(len(double) < len(moitie)):
    double.append(max(double) * 2)

moitie_double = pd.DataFrame(zip(moitie,double))

moitie_double = moitie_double.loc[moitie_double[0]%2 == 1,:] #loc permet de selectionner uniquement les lignes voulues [ligne,colonne]

reponse = sum(moitie_double.loc[:,1])

print(reponse)
