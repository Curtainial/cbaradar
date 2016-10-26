import string
alpha = "ABCDEFGHIJKLHMNOPQRSTUVWXYZ"

def encrypt(message,key):
    print(message)
    while len(key) < len(message):
        key += key

    return key[:len(message)]









message = input("What is your message? ")
key = input("What is your key? ")


message = message.upper()
key = key.upper()

print(encrypt(message,key))

































