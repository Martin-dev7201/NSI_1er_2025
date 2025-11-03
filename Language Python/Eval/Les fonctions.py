def cotisation(age):
    ''' Savoir le tarif d'une personne
Arguments:
          age=nombre entier
    '''
    if age<12:
        print("Votre tarif est de 50.0")
    elif 12<=age<=18:
        print("Votre tarif est de 100.0")
    elif 19<=age<=64:
        print("Votre tarif est de 150.0")
    elif age>=65:
        print("Votre tarif est de 75.0")

def avec_reductions(montant, etudiant, famille, senior):
    ''' Savoir si les personnes benifficent d'une reduction
Arguments:
    montant= cotisation de base
    étudiant: True si l'adhérent est etudient, False dans le cas contraire
    famille: True si l'adhérent sont en familles nombreuse, False dans le cas contraire
    senior_residents: True si l'adhérent est sénior et résident de" la commune, False dans le cas contraire
    '''
    if montant==100 and etudiant==True and famille==False and senior==False:
        resultat= montant-(1-(15/100))
        print(f"Votre nouveau tarif est de {resultat}")
    elif montant==150 and etudiant==False and famille==True and senior==False:
        resultat=montant-(1-(20/100))
        print(f"Votre nouveau tarif est de {resultat}")
    elif montant==75 and etudiant==False and famille==False and senior==True:
        resultat=montant-(1-(25/100))
        print(f"Votre nouveau tarif est de {resultat}")
    else:
        print("Vous n'avez accés aux reduction proposé")
