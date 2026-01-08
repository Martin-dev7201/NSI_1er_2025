# -*- coding: utf-8 -*-
import time

def occurences(texte):
    ''' Compte le nombre d’occurence de chaque mot d’un texte
    arg : texte : texte a etudier (string)
    retour : dictionnaire des mots (cle type str) associes au nombre d’occurence
    (valeur type int)
    '''
    dico_occur = {}
    for mot in texte.split():
        mot = mot.lower() # convertit le mot en minuscule
        mot = mot.strip(",.;!?-()«»_—") # enleve les ponctuations collees aux mots
        if mot in dico_occur: # teste si le mot est déja connu
            dico_occur[mot] += 1
        else:
            dico_occur[mot] = 1
    return dico_occur
    
def ouvrir_fichier(fichier):
    ''' Retourne le texte contenu dans un fichier texte
    Arg : fichier : non du fichier txt
    Retour : texte (type str)
    '''
    with open(fichier, 'r',encoding='utf-8') as f:
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

texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)
MOT = mot_le_plus_frequent(dico)
plus = plus_frequents(dico)
max_lettres = max(len(mot) for mot in dico)