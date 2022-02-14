import re

def encrypt(text,s) :
   
    cipher = ""

    regex = "|^&+-%*/=!>#@$£€"

    for i in range(len(text)) :

      char = text[i]   

      if (char.isupper()) :

         cipher += chr((ord(char) - s - 65) % 26 + 65)

      elif (char.islower()):

         cipher += chr((ord(char) - s - 97) % 26 + 97)

      else :

         cipher +=char


    return cipher


text = input("Enter the cipher text: ")

s = int(input("Enter the shift pattern: "))

print ("Cipher: " + encrypt(text,s))