from manipulationImage import *
img=ouvrirImage("imageCouleur.png")
img_2=ouvrirImage("masque.png")

def négatif():
    hauteur = len(img)
    largeur=len(img[0])
    liste=len(img[0][0])
    for ligne in range(hauteur) :
        for colonne in range (largeur):
            for valeur in range(liste):
                img[ligne][colonne][valeur] = 255-img[ligne][colonne][valeur]
    afficherImage(img)

def rgb():
    choix = int(input("Quelle couleur garder ? (0 pour Rouge, 1 pour Vert, 2 pour Bleu) : ")) 
    hauteur = len(img)
    largeur = len(img[0])
    for ligne in range(hauteur):
        for colonne in range(largeur):
            pixel = img[ligne][colonne]
            valeur_gardee = pixel[choix]
            nouveau_pixel = [0, 0, 0]
            nouveau_pixel[choix] = valeur_gardee
            img[ligne][colonne] = nouveau_pixel
    afficherImage(img)
    
def symetrie_verticale():
    hauteur = len(img)
    largeur=len(img[0])
    liste=len(img[0][0])
    for ligne in range(hauteur) :
        for colonne in range (largeur):
            for valeur in range(liste):
                img[ligne][largeur-colonne-1][valeur] = img[ligne][colonne][valeur]
    afficherImage(img)

def appliquer_masque():
   hauteur = len(img)
    largeur=len(img[0])
    liste=len(img[0][0])
    for ligne in range(hauteur) :
        for colonne in range (largeur):
            for color in range(liste):
                if masque[ligne][colonne]==255:
                    img[ligne][colonne][color]=img[ligne][colonne][color]-30
                if img[ligne][colonne][color]<0:
                    img[ligne][colonne][color]=0
    afficherImage(img)
    
