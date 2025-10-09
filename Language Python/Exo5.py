def leet_speak(texte):
    # Dictionnaire avec les remplacements pour minuscules et majuscules
    remplacements = {
        'A': '4', 'a': '4',
        'B': '8', 'b': '8',
        'X': '8', 'x': '8',
        'E': '3', 'e': '3',
        'I': '1', 'i': '1',
        'L': '1', 'l': '1',
        'K': 'X', 'k': 'x',   # on remplace K par X (respecte la casse)
        'S': '5', 's': '5',
        'T': '7', 't': '7',
        'O': '0', 'o': '0'
    }

    resultat = ""
    for caractere in texte:
        # .get renvoie la valeur correspondante ou le caractère lui-même
        resultat += remplacements.get(caractere, caractere)
    return resultat
