# -*- coding: utf-8 -*-

"""
Puissance 4
Travail sur les tableaux à deux dimensions
"""
from random import randint

# ----------------------------
# Les définitions de fonctions
# ----------------------------

def grille_vide():
    '''
    Fonction grille_vide(): construit un tableau à deux dimensions
    de taille 6 x 7 : 6 lignes et 7 colonnes.
    Chaque case contient la valeur 0.
    La fonction ne prend pas d'argument.
    La fonction renvoie le tableau.
    '''
    return [[0 for _ in range(7)] for _ in range(6)]
    

def affiche(gril):
    '''
    Fonction affiche(gril): affiche une grille de 6 lignes sur 7 colonnes.
    La fonction prend en argument un tableau de taille 6 x 7.

    Une ligne est notée ligne et prend une valeur entre 0 et 5,
    la ligne 0 étant située en bas.
    Une colonne est notée col et prend une valeur entre 0 et 6,
    la colonne 0 étant située à  gauche.
    Dans la grille:
        la valeur 0 représente une case vide, représentée par un . 
        la valeur 1 représente un pion du joueur 1, représenté par un X.
        la valeur 2 représente un pion du joueur 2, représenté par un O.
    '''
    print("   0 1 2 3 4 5 6 ")
    print("  ---------------")
    for ligne in range(5, -1, -1): 
        print(str(ligne) + " |", end="")
        for elt in gril[ligne]:
            if elt == 1:
                print('X', end=' ')
            elif elt == 2:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()
    

def coup_possible(gril, col):
    '''
    Fonction coup_possible(gril, col) :
        Détermine si il est possible de jouer dans la colonne col.
        Renvoie True si il est possible de jouer dans la colonne col.
        Prend en argument la grille, tableau de 6x7, avec la position des pions des joueurs et
        un entier, le numéro de colonne entre 0 et 6.
        Il est possible de jouer dans la colonne col, si il existe une case
        avec la valeur 0 dans cette colonne.
    '''
    if 0 <= col <= 6:
        return gril[5][col] == 0
    return False


def jouer(gril, j, col):
    '''
    Fonction jouer(gril, j, col):
        Fonction qui joue un coup du joueur j dans la colonne col de la grille.
        Arguments: gril est la grille de 6 x 7 avec le pions des joueurs
        j est un entier qui a la valeur 1 ou 2 suivant le joueur.
        col est un entier entre 0 et 6 et désigne une colonne non pleine de la grille.
        Si j vaut 1 la première case vide de la colonne col prendra la valeur 1
        Si j vaut 2 la première case vide de la colonne col prendra la valeur 2
    '''
    if coup_possible(gril, col):
        for ligne in range(6):  # On part du bas (ligne 0)
            if gril[ligne][col] == 0:
                gril[ligne][col] = j
                break
            
def horiz(gril, j):
    '''
    Fonction horiz(gril, j):
        Détermine si il y a un alignement horizontal de 4 pions du joueur j
        arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie True si c'est le cas.
        !!! La recherche se fait de gauche à  droite !!!
    '''
    for ligne in range(6):
        for col in range(4):  # On regarde 4 cases consécutives
            if all(gril[ligne][col+i] == j for i in range(4)):
                return True
    return False
                    


def vert(gril, j):
    '''
    Fonction vert(gril, j):
        Détermine si il y a un alignement vertical de 4 pions du joueur j
        arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie True si c'est le cas.
        !!! La recherche se fait de bas en haut !!!
    '''
    for ligne in range(3):  # On regarde les 4 cases vers le haut
        for col in range(7):
            if all(gril[ligne+k][col] == j for k in range(4)):
                return True
    return False
            

def diag_haut(gril, j):
    '''
    Fonction diag_haut(gril, j):
        Détermine si il y a un alignement diagonal vers le haut de 4 pions du joueur j
        arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie True si c'est le cas, False sinon.
     '''
    for ligne in range(3, 6):
        for col in range(4):
            if all(gril[ligne-i][col+i] == j for i in range(4)):
                return True
    return False

def diag_bas(gril, j):
    '''
    Fonction diag_bas(gril, j):
        Détermine si il y a un alignement diagonal vers le bas de 4 pions du joueur j
        arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie True si c'est le cas, False sinon.
     '''
    for ligne in range(3):
        for col in range(4):
            if all(gril[ligne+k][col+k] == j for k in range(4)):
                return True
    return False


def victoire(gril, j):
    '''
    fonction victoire(gril, j):
        determine si il y victoire ou non.
        Arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie un booléen True si le joueur j a gagné, False sinon.
        Fait appel aux fonctions horiz(), vert(), diag_haut() et diag_bas()
    '''
    gagne = horiz(gril, j) or vert(gril, j) or diag_haut(gril, j) or diag_bas(gril, j)
    if gagne:
        print('Terminé ! Le Joueur', j, 'a gagné')
    return gagne
    

def match_nul(gril):
    '''
    Fonction match_nul(gril):
        Détermine si il y a match nul ou pas
        Argument:  gril la grille avec les pions.
        Renvoie True si la partie est nulle, c'est à  dire si
        la ligne du haut est remplie, False sinon.
    '''
    if all(gril[5][col] != 0 for col in range(7)):
        print('Match nul - Bravo à vous deux !')
        return True
    return False

def coup_aleatoire(gril,j):
    '''
    Fonction coup_aleatoire(gril,j):
        Choisi une valeur de colonne au hasard mais dans laquelle il est possible de jouer.
        Arguments:  gril la grille avec les pions.
                    j le joueur, un entier avec la valeur 1 ou 2
        Renvoie col la valeur de colonne dans laquelle jouer automatiquement.
    '''
    col = randint(0,6)
    while not coup_possible(gril,col):
        col = randint(0,6)
    return col
      


# -------------------
# Programme principal

##### Programme principal  ##########

# Accueil du jeu
print("#######################################")
print("#         Puissance 4                 #")
print("#######################################")
print("La partie se joue à deux joueurs : joueur 1 et joueur 2")
print("Le joueur 1 commence la partie.")

#Jeu
g = grille_vide()
affiche(g)
coup = 0
j = [1, 2]

while not victoire(g, j[coup % 2]) and not match_nul(g):
    joueur = j[coup % 2]
    print('Joueur', joueur, 'à vous de jouer')
    col = int(input('Choisissez une colonne (0 à 6, 10 pour aléatoire) : '))
    
    if col == 10:
        col = coup_aleatoire(g, joueur)  

    while not coup_possible(g, col):
        col = int(input('Colonne pleine ou invalide, choisissez une autre : '))

    jouer(g, joueur, col) 
    affiche(g)
    coup += 1

