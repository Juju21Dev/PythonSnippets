# Program Polynomial
# polynomial
# date : 10/08/2020
# author : Julien Violette

from math import *

# general loop for testing multiple polynomials
choice = "O"
while choice == "O":
    # loop on entering the degree of the polynomial (a maximum of 6)
    n = 7
    while n > 6:
        n = int(input("Enter the degree of the polynomial (a maximum of 6) = "))

    # loop on entering the constant terms of the polynomial
    a = []
    for k in range(0, n + 1):
        a.append(float(input("a" + str(k) + " = ")))

    # displays the polynomial
    print("f(x) = ", a[0])  # displays the first constant term

    # loop through the display of the following terms of the polynomial
    for k in range(1, n + 1):
        # displays only the terms where the constant is different from zero
        if a[k] != 0:
            print("+", a[k], "* x^", k)

    # loop on the possibility of entering several x
    choice = "O"
    while choice == "O":

        # entering x
        x = float(input("x = "))

        # loop for calculating the polynomial
        result = 0
        for k in range(0, n + 1):
            result += a[k] * pow(x, k)

        # displays the result
        print("f(x) = ", result)

        # asks the user if he wants to do a new test
        choice = input("Do you want to test this polynomial with a new value ? (Y/N) ")

    # asks the user if he wants to test a new polynomial
    choice = input("Do you want to test a new polynomial ? (Y/N) ")
