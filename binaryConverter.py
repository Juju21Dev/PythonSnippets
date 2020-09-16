# Program Binary Converter
# converts decimal to binary and binary to decimal
# date : 21/07/2020
# author : Julien Violette

from math import *

# main loop
choice = "A"
while choice != "E" and choice != "e":

    # displays the menu
    print("to convert decimal to binary ........ 1")
    print("to convert binary to decimal ........ 2")
    print("exit ................................ Q")
    choice = input("your choice ................ ")

    # decimal to binary conversion
    if choice == "1":
        binary = ""
        nb = int(input("enter an integer = "))
        while nb != 0:
            binary = str(nb % 2) + binary
            nb = nb // 2
        print("binary conversion = ", binary)
    else:
        # binary to decimal conversion
        if choice == "2":
            nb, k = 0, 0
            binary = input("enter a binary number = ")
            while len(binary) > 0:
                nb += int(binary[len(binary) - 1:]) * pow(2, k)
                binary = binary[: len(binary) - 1]
                k += 1
            print("decimal conversion = ", nb)
