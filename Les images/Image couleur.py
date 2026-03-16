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
    largeur = len(img[0])
    img_resultat = Image.new("RGB", (largeur, hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            pixel_base = img[y][x]
            pixel_m = img_2[y][x]
            val_m = pixel_m[0] if isinstance(pixel_m, (list, tuple)) else pixel_m
            nouveaux_canaux = []
            for c in pixel_base:
                if c < 128:
                    res = (2 * c * val_m) // 255
                else:
                    res = 255 - (2 * (255 - c) * (255 - val_m)) // 255
                nouveaux_canaux.append(max(0, min(255, int(res))))
            img_resultat.putpixel((x, y), tuple(nouveaux_canaux))        
    afficherImage(img_resultat)
    