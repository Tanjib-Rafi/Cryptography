import re

def decrypt(text,s) :
   
    plain = ""

    for i in range(len(text)) :

      char = text[i]   

      if (char.isupper()) :

         plain += chr((ord(char) - s - 65) % 26 + 65)

      elif (char.islower()):

         plain += chr((ord(char) - s - 97) % 26 + 97)

      else :

         plain +=char


    return plain


text = input("Enter the cipher text: ")

s = int(input("Enter the shift pattern: "))

print ("Plain Text: " + decrypt(text,s))
