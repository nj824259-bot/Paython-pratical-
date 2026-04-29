# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:16:37 2026

@author: nayan jadhav
"""

# Program to divide bill safely

def divide_bill():
    try:
        total_bill = float(input("Enter total bill amount: "))
        people = int(input("Enter number of people: "))
        
        if people <= 0:
            print("Invalid input! Number of people must be greater than 0.")
            return
        
        amount_per_person = total_bill / people
        print("Each person should pay:", round(amount_per_person, 2))
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    
    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")

# Run the program
divide_bill()