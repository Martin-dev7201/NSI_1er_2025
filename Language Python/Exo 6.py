def temps_en_secondes(h, m, s, ms):
    """
    h : heures
    m : minutes
    s : secondes
    ms : millisecondes
    Retourne l'équivalent en secondes (float)
    """
    temps_total=h * 3600 + m * 60 + s + ms / 1000
    return temps_total

def distance(arrivee, emission):
    """
    arrivee : instant de réception (en secondes)
    emission : instant d’émission (en secondes)
    Retourne la distance parcourue en km
    """
    c = 300000  # vitesse de la lumière en km/s
    return (arrivee - emission) * c

def dms_a_decimale(deg, minute, seconde):
    """
    Convertit une coordonnée en DMS (degré, minute, seconde)
    en degré décimal
    """
    return deg + minute / 60 + seconde / 3600

def decimale_a_dms(val):
    """
    Convertit une coordonnée en degré décimal
    en DMS (degré, minute, seconde)
    """
    deg = int(val)
    minute = int((val - deg) * 60)
    seconde = (val - deg - minute / 60) * 3600
    return deg, minute, round(seconde)