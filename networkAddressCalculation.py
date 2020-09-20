# Program Network Address Calculation
# calculates a network address with an address and a mask
# date : 26/07/2020
# author : Julien Violette

from math import *

# entering the address and mask
addressB2 = input("Enter a base 2 address : ")
maskB2 = input("Enter a base 2 mask : ")

# converts the base 2 address to a base 10 address
addressB10 = 0
k = 0
while len(addressB2) > 0:
    addressB10 += int(addressB2[-1:]) * pow(2, k)
    addressB2 = addressB2[:len(addressB2) - 1]
    k += 1

# converts the base 2 mask to a base 10 mask
maskB10 = 0
k = 0
while len(maskB2) > 0:
    maskB10 += int(maskB2[-1:]) * pow(2, k)
    maskB2 = maskB2[:len(maskB2) - 1]
    k += 1

# calculates and displays the base 10 network address
networkAddressB10 = int(addressB10) & int(maskB10)
print("base 10 network address : ", networkAddressB10)

# calculates and displays the base 2 network address
networkAddressB2 = ""
while networkAddressB10 != 0:
    networkAddressB2 = str(networkAddressB10 % 2) + networkAddressB2
    networkAddressB10 = networkAddressB10 // 2
print("base 2 network address : ", networkAddressB2)
