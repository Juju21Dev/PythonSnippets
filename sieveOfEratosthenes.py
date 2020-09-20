# Program Sieve of Eratosthenes
# prime numbers before n with the sieve of Eratosthenes
# date : 20/09/2020
# author : Julien Violette

from math import *

# entering the maximum number
n = int(input("maximum value = "))

# initializations
arr = [1] * n  # array initialized to 1

# finds the prime numbers through the array
for k in range(2, int(sqrt(n))):
    # if the cell contains 1, it is a prime number
    if arr[k] == 1:
        # searches the following cells where the index is divided by k
        for i in range(k + 1, n):
            # if k divides i, then i is not a prime number
            if i % k == 0:
                arr[i] = 0

# displays the prime numbers
for k in range(2, n):
    if arr[k] == 1:
        print(k)
