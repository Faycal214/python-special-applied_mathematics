import numpy as np
import time

# creation de la liste sac a dos 
sac = [] # vecteur sac a dos

poids_max = int(input("donner le poids max de sac : "))

while poids_max < 0 or poids_max > 16:
    poids_max = int(input("redonner une autre valeur : "))

time.sleep(1)

# creation de la matrice[objects, utilistè, poids]
objects = ["Pomme", "Banane", "Orange", "Poire", "Fraise"]
utilites = [2, 3, 1, 4, 6]
poids = [3, 2, 5, 3, 4]

maliste = np.array([objects, utilites, poids])

print(f"voici notre liste (object/utilitès/poids) :\n{maliste}\n") # afficher la matrice

# trier la matrice selon l'utilitès des objects
M = maliste.shape[1] # nombre d'objects dans la matrice

# fonction qui tri la matrice (j'ai utiliser le tri par bulles pour celci)
def tri_matrice(liste):
    for i in range(M-1, 0, -1) :
        for j in range(0, i) :
            if (liste[1, j] < liste[1, j+1]) : # verifier si l'utilitè de j'eme object est inferieur de j+1'eme object
                cmt = liste[:, j].copy() #permuter le j'eme colonne et j+1'eme colonne avec la variable intermidiare cmt
                liste[:, j] = liste[:, j+1]
                liste[:, j+1] = cmt
    
    return liste # retourner la matrice trier

new_matrice = tri_matrice(maliste)
print(f"la nouvelle matrice trièr est comme suite : \n{new_matrice}\n")

# on va remplire le sac selon l'utilitès des objects toute on respectons la capacitè de sac
def remplire_sac(liste) :
    global poids_max # pour changer le contenu de la variable global poids_max du facon permanate
    
    for i in range(0, M-1)  :
        poids_max -= int(liste[2, i])
        if poids_max >= 0 :
            sac.append(liste[0, i])
        elif poids_max < 0 :
            break

remplire_sac(new_matrice)

print(f"le sac apres le remplisage : \n{sac}\navec son poids restent {poids_max}")
