#Assignment 4
import string
alphabet = string.ascii_uppercase

def filter_nonletters(message):
    output = ''
    for c in message:
        if c.isalpha():
            output += c
    return output
#This function removes every character that isn't in the 26 letter alphabet.

def ask():
    choice = input("(E)ncrypt or (D)ecrypt?")
    if choice.index[0:1] == 'e' or choice.index[0:1] == 'E':
        print(encrypt(message,key))
        print("Message Encrypted")
    if choice.index[0:1] == 'd' or choice.index[0:1] == 'D':
        print(decrypt(message,key))
        print("Message Decrypted")
    else:
        choice = input("(E)ncrypt or (D)ecrypt?")
        ask()
#This function iterates if the incorrect inputs are provided, while also providing the means for encryption and decryption.

def join_input_and_key(message,key):
    pairs = []
    for i, c in enumerate(message):
	    key_idx = i % len(key)
	    pairs.append((c, key[key_idx]))
    return pairs
#This function finds the new cipher shifted letter.

def eightspace(message):
    output = ''
    for i, c in enumerate(message):
        output += c
        if (i + 1) % 8 == 0:
            output += ' '
    return output
#This function creates agap every 8 spaces, as per Assignment guidelines.

def encrypt(message,key):
    output = ''
    message = filter_nonletters(message.upper())
    key = filter_nonletters(key.upper())
    print(message)
    for c in range(len(message)):
        if len(message) > len(key):
            key +=key
        c +=1
    pairs = join_input_and_key(message.upper(),key.upper())

    for pair in pairs:
#Pairs each letter of the message with the corresponding key letter
        mess_idx = alphabet.index(pair[0])
#Finds the index of the first letter of the message
        key_idx = alphabet.index(pair[1])
#Finds the index of the first lettter of the key
        encrypted_idx = (mess_idx + key_idx) % len(alphabet)
#Finds the new shifted cipher text mod 26 to wrap around.
        output += alphabet[encrypted_idx]

    output = eightspace(output)
    return output

def decrypt(message,key):
    output = ''
    pairs = join_input_and_key(message,key)
    for pair in pairs:
        mess_idx = alphabet.index(pair[0])
#Finds index of first letter of coded message
        key_idx = alphabet.index(pair[1])
#Finds index of first letter of the key
        decrypted_idx = (mess_idx - key_idx) % len(alphabet)
#The message decrypted is equal to the coded message - the key at each location mod 26 to wrap around.
        output += alphabet[decrypted_idx]
    return output

message = input("What is your message? ")
key = input("What is your key? ")
eightspace(filter_nonletters(message))
ask()




















