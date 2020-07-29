# Programme message crypté
# permet de crypter un message et de le décrypter
# date : 26/07/2020
# auteur : Julien Violette


# initialisations
cle = "cryptographie" # clé utilisée pour le cryptage
decalage = '-' # valeur de décalage

# saisie du message
message = input("Entrez un message = ")

#---------------------------
#--- cryptage du message ---
#---------------------------

# inversion entre le début et la fin (le message est coupé en 2)
milieu = int(len(message) // 2)
message = message[milieu:] + message[:milieu]

# oux entre chaque lettre du message et une des lettres de la clé
resultat = ""
for k in range(0, len(message)):
    resultat += chr((ord(message[k]) ^ ord(cle[k % len(cle)])) + ord(decalage))

# affichage du message crypté
print("crypté = ", resultat)


#--------------------------------------
#--- opération inverse (décryptage) ---
#--------------------------------------

# à nouveau oux permet de revenir à la valeur d'origine
message = ""
for k in range(0, len(resultat)):
    message += chr((ord(resultat[k]) - ord(decalage)) ^ ord(cle[k % len(cle)]))

# le milieu du message est décalé si la longueur du message est impaire
if len(message) % 2 != 0:
    milieu += 1
message = message[milieu:] + message[:milieu]

# affichage du message décrypté
print("message d'origine = ", message)

