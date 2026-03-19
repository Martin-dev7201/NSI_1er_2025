from manipulationImage import *
img = ouvrirImage("image_base.ppm")
img_2= ouvrirImage ("fine.ppm")
img_Cachee = img.copy()
img_fusion = ouvrirImage("img_fusion.ppm")

def extraction():
    hauteur = len(img_fusion)
    largeur = len(img_fusion[0])
    
    for ligne in range(hauteur):
        for colonne in range(largeur):
            r = img_fusion[ligne][colonne][0]
            v = img_fusion[ligne][colonne][1]
            b = img_fusion[ligne][colonne][2]
            
            r_extrait = (r & 7) << 5
            v_extrait = (v & 7) << 5
            b_extrait = (b & 7) << 5
            
            img_Cachee[ligne][colonne] = [r_extrait, v_extrait, b_extrait]
    
    afficherImage(img_Cachee)
    
def fusion(image_visible, image_à_caché):
    hauteur = len(img)
    largeur = len(img[0])
    liste = len (img[0][0])
    img_fusion = image_visible
    for ligne in range(hauteur):
        for colonne in range(largeur):
            for valeur in range(liste):
                img_fusion[ligne][colonne][valeur] = ((image_visible[ligne][colonne][valeur] & 248)) + ((image_à_caché[ligne][colonne][valeur]&224)>>5)
    sauveImage(img_fusion,"img_fusion.jpg")
    afficherImage(img_fusion)