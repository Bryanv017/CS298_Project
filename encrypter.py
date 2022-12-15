import string
import random

#get all characters including numbers and punctuations
chars = string.digits + string.ascii_letters

#Casting our chars string into a list with all characters
chars = list(chars)
keys = chars.copy()
 #Shuffle every character in our list so they have different order
random.shuffle(keys)
#print keys to console to verify each equivalence
print(f"chars:{chars}")
print(f"keys:{keys}")

def encrypt(message):
    cipher_text = ""

    for character in message:
        index = chars.index(character)
        cipher_text += keys[index]

    return cipher_text