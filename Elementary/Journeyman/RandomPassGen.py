# Write a program that generates a basic, random password
#- Define a function that takes two parameters: a string and an integer and returns a string
   # - The string parameter is the possible characters to be used in a password;
   #   the integer parameter is the length of the password.
   # - The function should generate the password one character at a time by randomly
   #   selecting a character from the first parameter and then return the password
#- Ask the user for how long the password should be 
#- Call the function makePassword using the string charChoice and the above input
 # as the arguments and then print the return value of the function. 

charChoice = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import random

def makePassword(aString, anInt):
    password = ""
    for i in range(anInt):
        index = random.randint(0, len(aString)-1)
        new = aString[index]
        password += new
    return password

length = int(input("How long do you want your password to be: "))


print(makePassword(charChoice,length))
