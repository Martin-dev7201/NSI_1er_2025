''' Convertisseur d'entiers relatifs en binaire signe avec lecomplement a 2
convertir_dec_binaire(5) renvoie [0, 1, 0, 1]
convertir_dec_binaire(-5) renvoie [1, 0, 1, 1]
'''



def additionBinaire(b1,b2) :
    ''' Additionne b1 à b2
    Arg ->  b1 : bit (entier 1 /0)
            b2 : bit (entier 1 /0)
    retour -> retenue et resultat (entiers 1 /0)
    Ex : additionBinaire(1,1) renvoie (1,0)
    '''
    pass


def ajout1(nbreBin) :
    ''' Ajoute 1 au nombre binaire nbreBin
    Arg -> nbreBin : nombre binaire. Liste d'entiers 1 / 0
    retour ->  Liste d'entiers 1 / 0
    Ex : ajout1([1,0,0,1,1]) renvoie [1,0,1,0,0]
    '''
    pass

def convertir_dec_binNaturel(nbreDecimal) :
    ''' Convertir en binaire naturel nbreDecimal
    Arg -> nbreDecimal : nombre entier naturel
    retour ->  Liste d'entiers 1 / 0
    '''
    nbreBin = []
    res = nbreDecimal
    while res > 0 :
        nbreBin.append(res%2)
        res = res//2
    nbreBin.append(0)
    nbreBin.reverse()
    return nbreBin

def absolute(val) :
    if val < 0 :
        return -val
    else :
        return val




def convertir_dec_binaire_7bits(nbreDecimal) :
    ''' Convertir en binaire signe complement a 2 sur 7 bits nbreDecimal
    Arg -> nbreDecimal : nombre entier relatif (-64 à 63)
    retour ->  Liste d'entiers 1 / 0 (complement a 2) de taille 7
    '''
    TAILLE_BITS = 7
    
    # Vérification de la plage pour 7 bits (de -64 à 63)
    if not (-(2**(TAILLE_BITS-1)) <= nbreDecimal <= (2**(TAILLE_BITS-1) - 1)):
        # Gérer le débordement (optional)
        print(f"Attention : {nbreDecimal} est hors de la plage représentable sur {TAILLE_BITS} bits ([-{2**(TAILLE_BITS-1)}, {2**(TAILLE_BITS-1) - 1}])")
        # On peut choisir de tronquer, lever une erreur, ou utiliser le comportement standard
        # Pour rester simple, nous allons continuer mais l'utilisateur doit être conscient.
    
    # --- Cas du nombre positif (ou zéro) ---
    if nbreDecimal >= 0:
        n = nbreDecimal
        binaire = []
        if n == 0:
            binaire = [0]
        else:
            # Conversion standard en binaire
            while n > 0:
                binaire.insert(0, n % 2)
                n //= 2
        
        # Ajout des zéros devant (padding) pour atteindre 7 bits
        # Un nombre positif commence toujours par 0.
        while len(binaire) < TAILLE_BITS:
            binaire.insert(0, 0)
            
        return binaire

    # --- Cas du nombre négatif (Complément à deux) ---
    else:
        # Étape 1 : Obtenir la représentation binaire du nombre positif correspondant (sur N-1 bits)
        n = abs(nbreDecimal)
        binaire_abs = []
        if n == 0: # Ne devrait pas arriver ici si nbreDecimal < 0
            binaire_abs = [0]
        else:
            while n > 0:
                binaire_abs.insert(0, n % 2)
                n //= 2
        
        # Padding pour atteindre N-1 bits
        while len(binaire_abs) < TAILLE_BITS - 1:
            binaire_abs.insert(0, 0)
        
        # Le nombre négatif final aura 7 bits, y compris le bit de signe (1)
        binaire_positif_signe = [0] + binaire_abs
        
        # Étape 2 : Inversion (Complément à un)
        # On inverse les 7 bits
        binaire_ca1 = [1 - bit for bit in binaire_positif_signe]
        
        # Étape 3 : Addition de 1 (Complément à deux)
        binaire_ca2 = list(binaire_ca1)
        retenue = 1
        i = len(binaire_ca2) - 1
        
        while i >= 0 and retenue == 1:
            if binaire_ca2[i] == 0:
                binaire_ca2[i] = 1
                retenue = 0
            else:
                binaire_ca2[i] = 0
            i -= 1
            
        # Si une retenue reste (débordement potentiel pour -64 qui est 1000000)
        # Le bit de poids fort est déjà géré par la taille fixe de 7.
        
        return binaire_ca2
