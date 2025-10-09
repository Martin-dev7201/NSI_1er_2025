def leet_speak(texte):
    # On crée un dictionnaire avec les remplacements à faire
    remplacements = {
        'A': '4',
        'B': '8',
        'X': '8',
        'E': '3',
        'I': '1',
        'L': '1',
        'K': 'X',
        'S': '5',
        'T': '7',
        'O': '0'
    }

    # On met tout le texte en majuscules pour simplifier
    texte = texte.upper()

    # On crée une nouvelle chaîne vide pour stocker le résultat
    resultat = ""

    # On parcourt chaque lettre du texte
    for lettre in texte:
        if lettre in remplacements:
            # Si la lettre est dans le dictionnaire, on la remplace
            resultat += remplacements[lettre]
        else:
            # Sinon, on garde la lettre telle quelle
            resultat += lettre

    # On renvoie le texte transformé
    return resultat
