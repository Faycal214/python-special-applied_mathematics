# probleme de plus proche voisin 
# on depart par un point initiale de coordonèes (0 ,0) et on chechre la plus proche ville du point actuelle ont calculons les distances avec toutes les villes 

import numpy as np #importer numpy
import matplotlib.pyplot as plt

def distance(point1,point2) : # fonction qui calcule la distance entre le point 1 et point 2
    dis = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return dis

def creer_matrice(points): # fonction qui creer une matrice des distances
    
    matrice = [] # la matrice des distances vide
    m = len(points) # la taille de la matrice (nombre de points)

    for i in range(m) : # une boucle qui parcourre les lignes
        
        lignes = [] # a chaque iteration on va remplire une ligne par les distances
        
        for j in range(m) : # boucle qui parcoure les colonnes 
            dis = 0 # initialiser la variable distance par 0
            
            if i == j : # si on tambe dans la case i=j (dans la diagonale)
                lignes.append(0) # on met 0
            
            else : 
                dis = distance(points[i], points[j]) # sinon calculer la distance de i eme point avec j eme point
                lignes.append(dis) # remplire la liste ligne par les distances
        
        matrice.append(lignes) # inserer a chaque iteration une ligne dans la matrice
    return matrice

def minimum(M) :
    m = len(M[0]) # ou bien m = M[1] car c'est une matrice symetrique
    chemin = [] # vecteur contient le plus court chemin
    
    for i in range(m):
        
        if i not in chemin : # si le point i ne se trouve pas dans le chemin
            chemin.append(i)
            
        mine = 100
        mine_index = 0
        
        for j in range(m):
            if i == j or j in chemin: # si on est dans la diagonale ou bien le point j est dans le chemin alors passer au prochaine iteration
                continue
            
            if M[i][j] < mine : # sinon si la distance entre ieme point et jeme point est inferieur de minimum
                mine = M[i][j]
                mine_index = j # le point j est se lui avec la plus courte distance avec point i
        
        chemin.append(mine_index) # ajouter le point j dans le chemin
                
    return chemin

n = int(input("donner le nombre de villes :"))

points = []
for i in range(1, n+1) :
    valeurs = input(f"donner les coordonnèes de ville {i} : ")
    valeurs_separees = valeurs.split(',')
    coordonnees = tuple(int(valeur) for valeur in valeurs_separees)
    points.append(coordonnees)

print(points)
print("\n")

M = creer_matrice(points) # faire appelle a la fonction qui retourne la matrice crèe
print(f"coici la matrice des distances :\n{M}")

chemin = minimum(M) #trouver le plus court chemin en debutant par le premier point
print("voici le plus court chemin qui par parrcour les sommets suivants :")
for sommet in chemin :
    print(f"ville {sommet}")

# Extraction des coordonnées x et y pour le tracé
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Extraction des coordonnées du chemin pour le tracé
x_chemin = [points[i][0] for i in chemin]
y_chemin = [points[i][1] for i in chemin]

# Tracé des points et du chemin
plt.figure()
plt.scatter(x_coords, y_coords, color='blue')  # Points
plt.plot(x_chemin, y_chemin, color='red')      # Chemin
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plus court chemin entre les points')
plt.grid(True)
plt.show()
 