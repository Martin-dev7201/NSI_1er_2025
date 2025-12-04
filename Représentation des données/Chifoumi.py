from random import *

#Choix du joueur
joueur = int(input('Votre choix ?\n[1] : Pierre\n[2] : Feuille\n[3] : Ciseaux\n'))
print('Vous avez choisi',end= ' ')
if joueur == 1 :
    print('pierre')
elif joueur == 2:
    print('feuille')
else :
    joueur = 3
    print('ciseaux')
#Choix de l’ordinateur
ordi = randint(1,3)
print('L’ordinateur a choisi ',end='')
if ordi == 1 :
    print('pierre')
elif ordi == 2:
    print('feuille')
else :
    ordi = 3
    print('ciseaux')
#Résultat du match
if joueur == ordi:
    print("Match nul")
elif (joueur == 1 and ordi == 3) or (joueur == 2 and ordi == 1) or (joueur == 3 and ordi == 2):
    print("Vous avez gagné")
else:
    print("Vous avez perdu")
