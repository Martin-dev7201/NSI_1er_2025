def est_premier(n):
    """Vérifie si un nombre est premier"""
    if n <= 1:
        print(n, "n’est pas un nombre premier")
        return False
    
    for i in range(2, n):       # On teste tous les nombres entre 2 et n-1
        if n % i == 0:          # Si un diviseur existe, ce n’est pas premier
            print(n, "n’est pas un nombre premier (divisible par", i, ")")
            return False
    
    print(n, "est un nombre premier !")
    return True
