# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:17:32 2026

@author: nayan jadhav 
"""

# Number Guessing Game in Python

import random

# Generate Random Number
secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:

    # User Input
    guess = int(input("Enter your guess: "))

    # Check Guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")