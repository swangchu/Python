"""
The program to generate a random number and compares with user input number.
The user continues to guess for the number till random number is gussed.
"""

import random

randNum = random.randint(0,100)
ans = "yes"

while ans == "yes":
    guess = int(input("Enter a number"))
    if guess == randNum :
        print("You guess it right")
        break
    elif guess > randNum:
        print("Your guess is high")
        ans = input("Type yes to continue:")
    else:
        print("Your guess is low")
        ans = input("Type yes to continue:")
    
