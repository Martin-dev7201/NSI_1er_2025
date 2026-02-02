message_secret = "VQ BQZEQ CGQ HAGE MHQL OAYBDUE BMEEQL M XM EGUFQ"
for cle in range(26): 
    resultat = ""
    for lettre in message_secret:
        code_ascii = ord(lettre)
        if 65 <= code_ascii <= 90:
            nouveau_code = code_ascii - cle
            if nouveau_code < 65:
                nouveau_code = nouveau_code + 26
            resultat = resultat + chr(nouveau_code)
        else:
            resultat = resultat + lettre
    print("Clé", cle, ":", resultat)
