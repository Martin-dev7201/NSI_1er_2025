message_a_crypter = "GAULOIS"
a = 3
b = 7

resultat = ""

for lettre in message_a_crypter:
    x = ord(lettre) - 65
    
    valeur_codee = (a * x + b) % 26
    
    nouvelle_lettre = chr(valeur_codee + 65)
    resultat = resultat + nouvelle_lettre

print("Message crypte :", resultat)print("Résultat du cryptage affine :")
print(message_final)