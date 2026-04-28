# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:19:22 2026

@author: nayan jadhav
"""

# Program to print multiplication tables from 1 to 10

# Outer loop to iterate through each table (1 to 10)
for i in range(1, 11):
    print(f"--- Multiplication Table of {i} ---")
    
    # Inner loop to calculate and print multiplication (1 to 10)
    for j in range(1, 11):
        product = i * j
        # Display in formatted manner: i x j = product
        print(f"{i} x {j} = {product}")
        
    # Print a blank line to separate tables for better readability
    print()

