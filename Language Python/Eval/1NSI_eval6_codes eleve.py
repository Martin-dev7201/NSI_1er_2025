def conversion(nb, lg):
    '''Conversion decimal -> binaire de nb. Renvoie une chaine de caractere constituée de
    1 et de 0 et de longueur lg si lg est superieur à la longueur de la representation
    binaire de nb.
    >>> conversion(13, 8)
    '00001101'
    >>> conversion(6, 4)
    '0110'
    >>> conversion(6, 2)
    '110'
    '''
    nb_bin = ''
    # Conversion decimale -> binaire par la méthode des divisions successives par 2
    while nb // 2 != 0:
        nb_bin = str(nb % 2) + nb_bin
        nb = nb // 2
    nb_bin = str(nb % 2) + nb_bin
    # Mise à la longueur lg (ajout de 0 à gauche du nombre)
    while lg > len(nb_bin) :
        nb_bin = '0' + nb_bin
    return nb_bin



def booleen(bit) :
    '''Converti le caractère bit en un booléen : TRUE si bit = '1' et FALSE sinon
    '''
    if bit == '1':
        return True
    else:
        return False
    
    
def caractere(bool) :
    '''Converti le booleen bool en un caractère : '1' si bool = TRUE et FALSE sinon
    '''
    if bool == True:
        return '1'
    else:
        return '0'
    
def addition(nb1, nb2):
    '''Additionne nb1 et nb2 (chaines de caracteres). nb1 et nb2 doivent être de même longueur.
    >>> addition("0101", "0011")
    '1000'
    >>> addition("1101", "0010")
    '1111'
    >>> addition("1001", "1000")
    '0001'
    '''
    res = ""
    retenue = "0"
    lg = len(nb1)
    while lg > 0 :
        lg = lg - 1
        b1 = booleen(nb1[lg])
        b2 = booleen(nb2[lg])
        r1 = booleen(retenue)
        b= (b1^b2)^r1
        r = (b1 and b2) or (b1 and r1) or (b2 and r1)
        retenue = caractere(r)
        res = caractere(b) + res
    return res
