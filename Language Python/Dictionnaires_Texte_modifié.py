# -*- coding: utf-8 -*-
import time

def occurences(texte):
    ''' Compte le nombre d’occurence de chaque mot d’un texte '''
    dico_occur = {}
    
    # On remplace les apostrophes par des espaces pour séparer "l'homme" en "l" et "homme"
    texte = texte.replace("'", " ") 
    
    for mot in texte.split():
        mot = mot.lower() # convertit le mot en minuscule
        mot = mot.strip(",.;!?-()«»_+—/@") # enleve les ponctuations collees aux mots
        
        # --- MODIFICATION ICI ---
        # On vérifie que le mot n'est pas vide ET qu'il ne contient que des lettres
        # (isalpha renvoie True si le mot contient a-z, é, à, etc.)
        if mot == "" or not mot.isalpha():
            continue
        # ------------------------

        if mot in dico_occur: 
            dico_occur[mot] += 1
        else:
            dico_occur[mot] = 1
    return dico_occur
    
def ouvrir_fichier(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    return texte

def mot_le_plus_frequent(dico):
    max_occurences = 0
    mot_frequent = ""
    for mot in dico:
        if dico[mot] > max_occurences:
            max_occurences = dico[mot]
            mot_frequent = mot
    return mot_frequent 

def le_plus_frequent(dico, n):
    max_occurences = 0
    mot_frequent = ""
    for mot in dico:
        if len(mot) == n:
            if dico[mot] > max_occurences:
                max_occurences = dico[mot]
                mot_frequent = mot
    return mot_frequent

def plus_frequents(dico):
    longueur_max = 0
    for mot in dico:
        if len(mot) > longueur_max:
            longueur_max = len(mot)
            
    for n in range(1, longueur_max + 1):
        resultat = le_plus_frequent(dico, n)
        if resultat != "":
            nb = dico[resultat]
            print(f"{n} lettre(s): {resultat} avec {nb}")

# Partie principale
try:
    nom_du_fichier = "lesMiserables.txt" # Cela permet de changer de txte facilement
    texteAEtudier = ouvrir_fichier(nom_du_fichier)
    dico = occurences(texteAEtudier)
    MOT = mot_le_plus_frequent(dico)
    
    print("--- Analyse des fréquences ---")
    plus = plus_frequents(dico)
    
    max_lettres = max(len(mot) for mot in dico)

except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_du_fichier}' est introuvable.")

    print("Vérifiez que le fichier est bien dans le même dossier que le script.")
