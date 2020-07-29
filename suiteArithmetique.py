# Programme suite arithmétique
# termes d'une suite arithmétique
# date : 19/07/2020
# auteur : Julien Violette

# saisie du premier terme, de la raison et du nombre de termes
u0 = int(input("Entrez le premier terme de la suite = "))
raison = int(input("Entrez la raison de la suite = "))
nombreTermes = int(input("Entrez le nombre de termes = "))

# initialisation de terme (qui démarre à u0)
terme = u0

# initialisation de la somme des termes
somme = 0

# boucle pour afficher les nb premiers termes de la suite
for k in range(0, nombreTermes):
    print(f"u{k} = {terme}")
    somme += terme
    terme += raison

# affichage de la somme des termes
print(f"la somme des premiers termes de la suite = {somme}")