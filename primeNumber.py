# Program Prime Number
# Prime Number
# date : 19/07/2020
# author : Julien Violette

# first entry of the number to test
val = int(input("Enter an integer > 1 (or 0 to quit) : "))

# general loop for several tests
while val != 0:

    # initializations
    divisor = 2
    prime = True

    # loop on finding a divisor
    while prime and divisor * divisor <= val:
        if val % divisor == 0:
            prime = False
        divisor += 1

    # displays the message corresponding to the number
    if prime:
        print(val, "is prime")
    else:
        print(val, "is not prime")

    # keyboarding of a new number to test
    val = int(input("Enter an integer > 1 (or 0 to quit) : "))
