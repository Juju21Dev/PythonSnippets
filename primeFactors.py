# Program Prime Factors
# displays an integer's prime factors
# date : 20/09/2020
# author : Julien Violette

# entering the first value
value = int(input("enter a value (0 to quit) = "))

# loop on the treatment of several values
while value != 0:
    # finds and displays the prime factors
    vecDiv = []
    divisor = 2
    while divisor <= value:
        # if you find a prime factor
        if value % divisor == 0:
            print(divisor)
            value = value // divisor
            # the divisor is stored in the array
            vecDiv.append(divisor)
        else:
            # otherwise go to the next divisor
            divisor += 1

    # displays each divisor, just once
    print("divisors : ")
    print(vecDiv[0])
    for k in range(1, len(vecDiv)):
        if vecDiv[k] != vecDiv[k - 1]:
            print(vecDiv[k])

    # entering a new value
    value = int(input("enter a value (à to quit) = "))
