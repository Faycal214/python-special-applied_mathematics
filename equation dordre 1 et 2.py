import numpy as np
import time
import sys


print("bienvenue au programme !\n")
print("======================")

# ici j'ai poser qu'est que le programme peut faire et on demande de l'utilisateur de choisir entre les equations de 1ere ou 2eme degre
print("vous allez choisir entre la resolution des equations au premier ou deuxieme degrè :\n")
print("1. Equations au premier degrè\n2. Equations au deuxieme degrè :\n")

def premier_degre(): # l'appel de la fonction
    print("donc votre equation est de forme (AX + B)\n")
    
    # demander combien d'equation on va lui resoudre
    cpt = int(input("combien d'equations voulez vous resoudre : "))
    time.sleep(2)
    
    print("\n")
    
    for i in range(1, cpt+1) :
        print(f"equation {i} :\n")
        
        # remplire les coefficients de 'i'eme equation
        # je vais tester si la valeur fourni de A est nul par la clause try / except
        try :
            a = float(input("donner la valeur de A : "))
            b = float(input("donner la valeur de B : "))
            
            time.sleep(1)
            
            solution = -b / a
        except ZeroDivisionError:
            print('pas de solution pour cette equation ! dividion par zero')
            
        except (TypeError, ValueError):
            print("pas de solution pour cette equation ! erreur de type ou de valeur")
        else :
            print(f"solution de {a}*x + {b} est x= {solution}")
            print("======================\n")


def deuxieme_degre() :
    print("donc votre equation est de forme (AX*2 + BX + C)\n")
    
    cpt = int(input("combien d'equations voulez vous resoudre ? "))
    time.sleep(1)
    
    print("\n")
    
    for i in range(1, cpt+1) :
        print(f"equation {i} :\n")
        
        # remplir les coefficients
        try :
            a = float(input("donner la valeur de A : "))
            b = float(input("donner la valeur de B : "))
            c = float(input("donner la valeur de C : "))
        
            time.sleep(1)
        
            # calculer delta
            delta = b**2 - 4*a*c
        except (ValueError, TypeError) :
            print("pas de solution pour cette equation ! erreur de type ou de valeur")
        else :
            
            if delta < 0 : # si delta negatif
                print(f"pas de solution pour {a}x**2 + {b}x + {c} car delta= {delta} < 0\n")
        
            elif delta == 0 : # si delta est null
                try :
                    solution = (-b) / 2*a
                except ZeroDivisionError : # si on a dividion par zero 
                    print(f"l'equation n'a pas de solution ! division par zero")
                    
                else : # sinon voici la solution
                    print(f"solution de {a}x**2 + {b}x + {c} : x= {solution}")
            
            elif delta > 0: # si delta positif strictement
                try :
                    solution_1 = (-b + np.sqrt(delta)) / (2 * a)
                    solution_2 = (-b - np.sqrt(delta)) / (2 * a)
                except ZeroDivisionError : # exception de division par zero si A == 0
                    print(f"l'equation n'a pas de solution ! Devision pas zero")
                
                except RuntimeWarning : 
                    print(f"l'equation n'a pas de solution ! divide by zero encountered in scalar divide")
                
                except (TypeError, ValueError) :
                    print("l'equation n'a pas de solution ! Erreur de type ou de valeur")
                else :
                    print(f"solution de {a}x**2 + {b}x + {c} : x1= {solution_1} ||| x2= {solution_2}")
            

# inserer la reponse de l'utilisateur entre le choix 1 ou 2
reponse = int(input())

# si l'utilisateur n'a pas choisi les 2 choix voulu il doit redonner une autre valeur
while reponse not in [1, 2] :
    reponse = int(input("redonner une autre reponse : "))
    
    if reponse != 1 and reponse !=  2 :
        reponse = int(input("redonner une autre reponse : "))

# si la reponse est 1 alors appeler la fonction premier_degre()
if reponse == 1 :
    premier_degre()

# si la reponse est 2 alors appeler la fonction deuxieme_degre()
elif reponse == 2 :
    deuxieme_degre()

# afficher le message de fin du programme
print("fin de programme")
