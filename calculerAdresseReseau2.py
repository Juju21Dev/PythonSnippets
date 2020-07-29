# Programme calcul d'un adresse réseau en base 10 et en base 2
# calcul d'une adresse réseau à partir d'une adresse et d'un masque
# date : 26/07/2020
# auteur : Julien Violette

from math import *

# saisie de l'adresse et du masque
adresseB2 = input("Entrez une adresse en base 2 : ")
masqueB2 = input("Entrez un masque en base 2 : ")

# conversion adresseB2 en base 10
adresseB10 = 0
k = 0
while len(adresseB2) > 0:
    adresseB10 += int(adresseB2[-1:]) * pow(2, k)
    adresseB2 = adresseB2[:len(adresseB2) - 1]
    k += 1

# conversion masqueB2 en base 10
masqueB10 = 0
k = 0
while len(masqueB2) > 0:
    masqueB10 += int(masqueB2[-1:]) * pow(2, k)
    masqueB2 = masqueB2[:len(masqueB2) - 1]
    k += 1

# calcul et affichage de l'adresse réseau en base 10
reseauB10 = int(adresseB10) & int(masqueB10)
print("adresse réseau en base 10 : ", reseauB10)

# calcul et affichage de l'adresse réseau en base 2
reseauB2 = ""
while reseauB10 != 0:
    reseauB2 = str(reseauB10 % 2) + reseauB2
    reseauB10 = reseauB10 // 2
print("adresse réseau en base 2 : ", reseauB2)