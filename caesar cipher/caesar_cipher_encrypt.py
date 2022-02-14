import re

def encrypt(text,s) :
   
    cipher = ""

    regex = "|^&+-%*/=!>#@$£€"

    for i in range(len(text)) :

      char = text[i]   

      if (char.isupper()) :

         cipher += chr((ord(char) + s - 65) % 26 + 65)
         '''ord function convert char to ascii value'''
         '''changing char to numbers by subtracting 65'''
         '''make sure that our values don't fall away from 0-25 range, so we need modulo 26 operation'''
         '''by adding 65 at last we are now converting numbers to char'''

      elif (char.islower()) :

         cipher += chr((ord(char) + s - 97) % 26 + 97)

      elif (char.isnumeric()) :

         cipher += str(char)

      elif (re.match(regex, char)):

         cipher += str(char)
      
      elif " " in char:

         cipher += char

      else :
         
         cipher += char

    return cipher


text = input("Enter the plain text: ")

s = int(input("Enter the shift pattern: "))

print ("Cipher: " + encrypt(text,s))
