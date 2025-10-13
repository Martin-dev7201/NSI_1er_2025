import math   # pour utiliser la racine carrée

def equation_2nd_degre(a, b, c):
    """Résout une équation du second degré : a*x² + b*x + c = 0"""
    delta = b**2 - 4*a*c
    print(f"Le discriminant Δ ={delta}")

    if delta < 0:
        print("Il n’y a pas de solution réelle.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Une seule solution :{x}")
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Deux solutions :")
        print(f"x1 ={x1}")
        print(f"x2 ={x2}")
