texte= 'CE SOIR ON ATTAQUE LES GAULOIS'
d=3
crypt= 'FH VRLU RQ DWWDTXH OHV JDXORLV'
def cryptage(text, d):
    crypte=""
    for c in text :
        c = ord(c)
        c = c + d
        if c == 32 + d:
           c = 32
        elif c>90:
            c = c-26
        elif c<65:
            c=c+26
        c = chr(c)
        crypte = crypte + c
    
    print('texte crypté : '+crypte)

def décryptage(crypt, d):
    return cryptage (crypt,-d)