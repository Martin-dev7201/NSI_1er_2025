def decoupeNbreShad(nombreShadocks):
    nbreDecoupe = nombreShadocks.split(" ")
    return nbreDecoupe

def chiffreShadDec(chiffreShad):
    if chiffreShad == 'GA':
        return 0
    elif chiffreShad == 'BU':
        return 1
    elif chiffreShad == 'ZO':
        return 2
    elif chiffreShad == 'MEU':
        return 3

def convShadDec(nbreShadocks):
    chiffres = nbreShadocks.split(" ")
    resultat = 0
    puissance = len(chiffres) - 1
    for chiffre in chiffres:
        resultat += chiffreShadDec(chiffre) * (4 ** puissance)
        puissance -= 1
    return resultat

def convDecShad(nbre):
    correspondance = ['GA', 'BU', 'ZO', 'MEU']
    resultat = []
    while nbre > 0:
        reste = nbre % 4
        resultat.insert(0, correspondance[reste])
        nbre = nbre // 4
    return resultat