# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:09:44 2026

@author: nayan jadhav
"""

import math

# Take input from user
P = float(input("Enter Principal amount (loan amount): "))
R = float(input("Enter Annual Interest Rate (in %): "))
N = int(input("Enter Loan Tenure (in months): "))

# Convert annual rate to monthly rate
r = R / (12 * 100)

# EMI formula
EMI = P * r * math.pow((1 + r), N) / (math.pow((1 + r), N) - 1)

# Display result
print(f"Monthly EMI is: {EMI:.2f}")