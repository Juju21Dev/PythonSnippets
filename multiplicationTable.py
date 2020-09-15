# Program Multiplication Table
# displays a multiplication table with input control
# date : 19/07/2020
# author : Julien Violette

# keyboarding of the value with input control
val = 0
while val < 1 or val > 9:
    val = int(input("Enter an integer = "))

# displays the multiplication table for this value
for k in range(1, 11):
    print(val, "*", k, "=", (val * k))
