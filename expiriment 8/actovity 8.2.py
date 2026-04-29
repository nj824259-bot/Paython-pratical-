# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:15:43 2026

@author: nayan jadhav
"""

# Registration Form - Age Validation

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            
            if age <= 0:
                print("Invalid age! Age must be greater than 0.")
            elif age < 18:
                print("You must be at least 18 years old to register.")
            else:
                return age
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def register_user():
    name = input("Enter your name: ")
    age = get_age()
    
    print("\nRegistration Successful!")
    print("Name:", name)
    print("Age:", age)

# Run the program
register_user()