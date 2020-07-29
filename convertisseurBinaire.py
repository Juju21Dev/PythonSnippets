# Programme convertisseur d'entiers en binaires et vice-versa
# conversions d'entiers en binaires et vice-versa
# date : 21/07/2020
# auteur : Julien Violette

from math import *

# boucle sur le menu
choix = "Z"
while choix != "Q" and choix != "q":

    # afficher le menu
    print("conversion entier vers binaire ........ 1")
    print("conversion binaire vers entier ........ 2")
    print("quitter ............................... Q")
    choix = input("votre choix ............ ")

    # conversion entier vers binaire
    if choix == "1":
        binaire = ""
        nb = int(input("entrez un entier = "))
        while nb != 0:
            binaire = str(nb % 2) + binaire
            nb = nb // 2
        print("conversion en binaire = ", binaire)
    else:
        # conversion binaire vers entier
        if choix == "2":
            nb, k = 0, 0
            binaire = input("entrez un nombre binaire = ")
            while len(binaire) > 0:
                nb += int(binaire[len(binaire) - 1:]) * pow(2, k)
                binaire = binaire[: len(binaire) - 1]
                k += 1
            print("conversion en base 10 = ", nb)




