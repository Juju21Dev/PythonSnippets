# Program Prime Numbers below 100
# prime numbers below 100
# date : 20/09/2020
# author : Julien Violette

from math import *

# initializations
prime = []  # array that stores the prime numbers
nb = 3  # variable that will be tested

# initialization of the first cell
prime.append(2)

# loop for searching prime numbers
while nb < 100:
    # tests if the number in nb is a prime number
    k = 0
    while pow(prime[k], 2) < nb and nb % prime[k] != 0:
        k += 1
    # if nb is a prime number, nb is stored
    if nb % prime[k] != 0:
        prime.append(nb)
    # tests the next number
    nb += 1

# displays the prime numbers
for k in range(0, len(prime)):
    print(prime[k])
