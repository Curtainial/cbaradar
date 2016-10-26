import string
alpha = "ABCDEFGHIJKLHMNOPQRSTUVWXYZ"
#still idk what to do with this
def encrypt(message,key):
    print(message)
    while len(key) < len(message):
        key += key
#Gets the key lined up with the message.
    print(key[:len(message)])

#assign values to letters, then use those values to add for encryption
#subtract for decryption and use modulo 26 if greater than 26



message = input("What is your message? ")
key = input("What is your key? ")


message = message.upper()
key = key.upper()

print(encrypt(message,key))

































