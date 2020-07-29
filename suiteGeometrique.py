# Programme suite géométrique
# termes d'une suite géométrique
# date : 19/07/2020
# auteur : Julien Violette

# saisie du premier terme, de la raison et du nombre de termes
u0 = int(input("Entrez le premier terme de la suite = "))
q = int(input("Entrez la raison de la suite = "))
nb = int(input("Entrez le nombre de termes = "))

# initialisation de terme (qui démarre à u0)
terme = u0

# initialisation de la somme des termes
somme = 0

# boucle pour afficher les nb premiers termes de la suite
for k in range(0, nb):
    print(f"u{k} = {terme}")
    somme += terme
    terme *= q

# affichage de la somme des termes
print(f"la somme des premiers termes de la suite = {somme}")