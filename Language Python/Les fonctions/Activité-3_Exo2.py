def diviseurs(n):
    """Affiche les diviseurs du nombre n"""
    print(f"Les diviseurs de {f} sont :")
    for i in range(1, n + 1):   # On teste tous les nombres de 1 à n
        if n % i == 0:          # Si la division tombe juste (pas de reste)
            print(i)
