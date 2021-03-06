# Program Geometric Sequence
# terms of a geometric sequence
# date : 19/07/2020
# author : Julien Violette

# first term entry, common ratio and number of terms
a = int(input("Enter the first term of the sequence = "))
r = int(input("Enter the common ratio of the sequence = "))
nb = int(input("Enter the number of terms = "))

# initializations
term = a
sumTerms = 0

# loop that displays the nb first terms of the sequence
for k in range(0, nb):
    print(f"u{k} = {term}")
    sumTerms += term
    term *= r

# displays the sum
print(f"the sum of the sequence's first terms = {sumTerms}")
