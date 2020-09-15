# Program Encrypted Message
# allows you to encrypt a message and decrypt it
# date : 26/07/2020
# author : Julien Violette


# initializations
key = "cryptography" # key used for encryption
offsetting = '-' # offset value

# keyboarding of the message
message = input("Enter a message = ")

#---------------------------
#--- message encryption ---
#---------------------------

# reversal between the beginning and the end (the message is cut in half)
middle = int(len(message) // 2)
message = message[middle:] + message[:middle]

# exclusive or between each letter of the message and one of the letters of the key
result = ""
for k in range(0, len(message)):
    result += chr((ord(message[k]) ^ ord(key[k % len(key)])) + ord(offsetting))

# displays the encrypted message
print("encrypted = ", result)