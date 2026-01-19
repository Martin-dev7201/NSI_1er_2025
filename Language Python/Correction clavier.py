def correcteur(clavier_voulu, clavier_reel, texte_affiche):
    resultat = ""
    for caractere in texte_affiche:
        lettre_trouvee = False
        for i in range(len(clavier_reel)):
            if caractere == clavier_reel[i]:
                resultat += clavier_voulu[i]
                lettre_trouvee = True
        
        if not lettre_trouvee:
            resultat += caractere
            
    return resultat

print(correcteur('QZAW', 'AWQZ', 'LE ZQGON EST HQWQRDEUX !'))
print(correcteur('TBA', 'BAT', 'LES ATBETUX SONB AETUX'))