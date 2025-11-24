def moyenne(l):
    '''
    Renvoie la moyenne des entiers de la liste l
    Argument: l est une liste entiers
    '''
    somme=0
    for valeur in l:
        somme= (somme + valeur)
    return somme/len(l)

def complement(t):
    '''
    Renvoie le complément du nombre binaire donné dans le tableau t.
    Argument : t est un tableau d'entiers représentant un nombre binaire,
    dont les éléments sont 0 ou 1 
    '''
    nombre=[]
    for t in t:
        if t==0:
            nombre.append(1)
        else:
            nombre.append(0)
    return nombre
