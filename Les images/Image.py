from manipulationImage import *
img=ouvrirImage("nb.png")

def négatif():
    hauteur = len(img)
    largeur=len(img[0])
    for ligne in range(hauteur) :
        for colonne in range (largeur):
            img[ligne][colonne] = 255-img[ligne][colonne]
    afficherImage(img)

def bw():
    hauteur = len(img)
    largeur = len(img[0])
    for ligne in range(hauteur):
        for colonne in range(largeur):
            if img[ligne][colonne] >= 127.5:
                img[ligne][colonne]= 255
            else:
                img[ligne][colonne] = 0
    afficherImage(img)
    
def assombre():
    hauteur = len(img)
    largeur = len(img[0])
    for ligne in range(hauteur):
        for colonne in range(largeur):
            img[ligne][colonne]= img[ligne][colonne]-30
            if img[ligne][colonne]<0:
                img[ligne][colonne]+=30
    afficherImage(img)

def ligne():
    hauteur = len(img)
    largeur = len(img[0])
    for ligne in range(hauteur):
        for colonne in range(largeur):
            point_depart = hauteur // 2
            epaisseur = 15 
            for i in range(point_depart, point_depart + epaisseur):
                if i < hauteur:
                    img[i] = [255] * largeur
    afficherImage(img)
    
def mirroir():
    hauteur = len(img)
    largeur = len(img[0])
    for ligne in range(hauteur):
        img[ligne] = img[ligne][::-1]
    
    afficherImage(img)

# Accueil du menu
print("#######################################")
print("#           Menu d'image              #")
print("#######################################")
print("1 : Négatif")
print("2 : Noir et Blanc (BW)")
print("3 : Assombrir")
print("4 : Tracer une ligne")
print("5 : Miroir")
print("#######################################")

choix = input(" Choisissez la transformation de votres image:")

if choix == "1":
    négatif()
elif choix == "2":
    bw()
elif choix == "3":
    assombre()
elif choix == "4":
    ligne()
elif choix == "5":
    mirroir()
else:
    print("Désolé, ce bouton ne fait pas partie du setlist !")