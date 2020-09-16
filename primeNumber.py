# Program Prime Number
# Prime Number
# date : 19/07/2020
# author : Julien Violette

# first keyboarding of the number to test
val = int(input("Enter an integer > 1 (or 0 to quit) : "))

# general loop for several tests
while val != 0:

    # initializations
    divider = 2
    prime = True

    # loop on finding a divider
    while prime and divider * divider <= val:
        if val % divider == 0:
            prime = False
        divider += 1

    # displays the message corresponding to the number
    if prime:
        print(val, "is prime")
    else:
        print(val, "is not prime")

    # keyboarding of a new number to test
    val = int(input("Enter an integer > 1 (or 0 to quit) : "))
