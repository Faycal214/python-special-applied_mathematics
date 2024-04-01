import sys

print("DM gestionnaire des taches")
print("zn binome Alikacem faycal G1 et Benhadid nouha G2\n")

def ajouter_tache(taches) : # fonction qui ajoute une tache au liste des taches
    new_tache = str(input("Nouvelle tache : ")) # l'utilisateur doit fournir une tache(chaine de caractère)
    new_tache_splitted = new_tache.split(",") # sèparer les mots entre vèrgule 
    taches.append(new_tache_splitted) # ajouter la tache a la liste

def affichage_tache(taches, n) : # afficher les elements de la liste taches
    if n == 0 : # si la liste des taches est vide
        print("Il n'exist aucune tache pour le moment!")
    else : #sinon afficher les taches 
        print("Taches :")
        for i, tache in zip(range(1, n+1), taches) : # parcourir deux sèquence en mème temps (liste des taches et le compteur i)
            print(f"{i}. {tache[0]} - {tache[1]} - {tache[2]}")

def terminer_tache(taches, n) : # modifier l'ètat des taches a partir de cette fonction
    choix = int(input("Entrez le numéro de la tâche à marquer comme terminée:")) # fournir le numèro de la tache
    if choix >n or choix < 0 :
        print("La tache n'existe pas !")
    elif taches[choix-1][2] == "terminer" : # si la tache sèlectionnè est dèja en ètat terminèe 
        print(f"la tache {taches[choix-1][0]}est dèja terminer!")
    else : # sinon
        taches[choix-1][2] = "terminée"
        print(f"La tâche '{taches[choix-1][0]}' a été marquée comme terminée.")
        
def supprimer_tache(taches, n): # supprimer une tache de la liste taches
    choix = int(input("Entrez le numéro de la tâche à supprimer:")) # demander le numèro de la tache
    if choix > n or choix < 0: 
        print("elle n'existe pas cette tache")
    else : # supprimer la tache sèlectionner
        print(f"La tâche '{taches[choix-1][0]}' a été supprimée.")
        taches.pop(choix - 1)

def sortir() :
    print("Merci davoir utilisé le gestionnaire de tâches. Au revoir!")
    sys.exit() # faire appele a la fonction exit() pour terminer le programme

def gestionnaire_des_taches() : # le programme principale commence apres l'appelle de cette fonction
    taches = [] # creation de la liste des taches
    print("bienvenue au programme !")
    x = int(input("donner le nombre de taches au dèbut : ")) # ici on va initialiser la liste par des taches, le nombre des taches est a choisir
    for i in range(x) :
        ajouter_tache(taches)
    while True: # parcourrir le programme sans aucune condition de debut, comme ca ont peux le terminer quand ont execute la 5ème commande 
        n = len(taches) #calculer la taille de la liste
        print("\nMenu:") # le menu
        print("1. Ajouter une nouvelle tâche")
        print("2. Afficher toutes les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter le programme")
        reponse = int(input("\nEntrez le numéro de l'option : ")) # inserer le numero de commande
        if reponse == 1:
            ajouter_tache(taches)
        elif reponse == 2:
            affichage_tache(taches, n)
        elif reponse == 3:
            terminer_tache(taches, n)
        elif reponse == 4:
            supprimer_tache(taches, n)
        elif reponse == 5:
            sortir()
        else:
            print("Option invalide. Veuillez choisir une option valide.") # cette commande n'existe pas dans les choix de menu
gestionnaire_des_taches()