# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:14:44 2026

@author: nayan jadhav
"""

# ATM Withdrawal System

# Initial balance
balance = 10000  

# Take withdrawal amount from user
amount = float(input("Enter amount to withdraw: "))

# Check conditions
if amount <= 0:
    print("Invalid amount! Please enter a positive value.")

elif amount > balance:
    print("Insufficient balance! Transaction failed.")

else:
    balance -= amount
    print("Withdrawal successful!")
    print("Remaining balance:", balance)