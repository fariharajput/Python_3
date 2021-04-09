# Questions3: Cyber Security: substitution cipher

# Write a function that
# takes a message “m” and numeric offset “o”
# encrypts the messages by shifting all the letters in “m” by the offset “o”.


# For example: With an offset of 3, “Hi” becomes “Kl” and so on. [Hint: use ord() and char() python functions]

def encrypts_func(message, offset):
    enc_message = ''
    for c in message:
        c = ord(c) + offset
        enc_message = enc_message + chr(c)

    return enc_message

message = input("Enter a message: ")
offset = int(input("Enter an offset integer: "))

print("Encrypted message is: ", encrypts_func(message, offset))