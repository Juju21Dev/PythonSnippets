# Program Network Adress Calculation
# calculates a network adress with an adress and a mask
# date : 26/07/2020
# author : Julien Violette

from math import *

# keyboarding of the adress and mask
adressB2 = input("Enter a base 2 adress : ")
maskB2 = input("Enter a base 2 mask : ")

# converts the base 2 adress to a base 10 adress
adressB10 = 0
k = 0
while len(adressB2) > 0:
    adressB10 += int(adressB2[-1:]) * pow(2, k)
    adressB2 = adressB2[:len(adressB2) - 1]
    k += 1

# converts the base 2 mask to a base 10 mask
maskB10 = 0
k = 0
while len(maskB2) > 0:
    maskB10 += int(maskB2[-1:]) * pow(2, k)
    maskB2 = maskB2[:len(maskB2) - 1]
    k += 1

# calculates and displays the base 10 network adress
networkAdressB10 = int(adressB10) & int(maskB10)
print("base 10 network adress : ", networkAdressB10)

# calculates and displays the base 2 network adress
networkAdressB2 = ""
while networkAdressB10 != 0:
    networkAdressB2 = str(networkAdressB10 % 2) + networkAdressB2
    networkAdressB10 = networkAdressB10 // 2
print("base 2 network adress : ", networkAdressB2)