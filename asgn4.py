#Assignment 4
#Due Wednesday @ 2 pm
#Finish tonight. VERY IMPORTANT!!!!!!!!!

import string
from itertools import cycle

alphabet = string.ascii_uppercase

def remove_nonalphabetic(input_string):
    output = ''
    for char in input_string:
        if char.isalpha():
            output += char

    return output

def eightspace(input_string):
    output = ''
    for i, char in enumerate(input_string):
        output += char
        if (i + 1) % 8 == 0:
            output += ' '

    return output


def encrypt(input_string, key):
    output = '' # this is what will be our encrypted string, begins empty
    input_string = remove_nonalphabetic(input_string)

    zipped = zip(input_string.upper(), cycle(key.upper()))
    print(input_string)
    while len(key) < len(input_string):
            key = key*10000
            newkey = print(key[:len(input_string)])
    for pair in zipped:
#Pairs each letter of the message with the corresponding key letter
        input_idx = alphabet.index(pair[0])
#Finds the index of the first letter of the message
        key_idx = alphabet.index(pair[1])
#Finds the index of the first lettter of the key
        encrypted_idx = (input_idx + key_idx) % len(alphabet)
#Finds the new shifted cipher text mod 26 to wrap around.
        output += alphabet[encrypted_idx]

    output = eightspace(output)

    return output




def decrypt(input_string,key):
    output = ''
    zipped = zip(input_string.upper(), cycle(key.upper()))
    while len(key) < len(input_string):
        key = key*100
        newkey = print(key[:len(input_string)])
    for pair in zipped:
        input_idx = alphabet.index(pair[0])
#Finds index of first letter of coded message
        key_idx = alphabet.index(pair[1])
#Finds index of first letter of the key
        decrypted_idx = (input_idx - key_idx) % len(alphabet)
#The message decrypted is equal to the coded message - the key at each location mod 26 to wrap around.
        output += alphabet[decrypted_idx]
    return output



input_string = input("What is your message? ")
key = input("What is your key? ")
choice = input("(E)ncrypt or (D)ecrypt? ")
if choice == "E" or choice == "e" or choice.index[0:1] == 'e':
    encrypt(input_string,key)
elif choice.index[0:1] == 'd' or choice == 'd' or choice == 'D':
    decrypt(input_string,key)































