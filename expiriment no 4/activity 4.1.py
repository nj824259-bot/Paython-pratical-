

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:42:24 2026

@author nayan jadhav
"""

def calculate_total_bill(cart):
    """
    Calculates the total bill from a shopping cart dictionary.
    
    Args:
        cart (dict): A dictionary where keys are product names 
                     and values are their prices.
                     
    Returns:
        float: The grand total of all items in the cart.
    """
    total = 0
    # Iterate over each item and its price in the dictionary
    for item, price in cart.items():
        total += price
        print(f"* {item:<15} : ${price:>.2f}") # Print each item and its price in the list
        
    return total

# The shopping cart with product prices
shopping_cart = {
    "Laptop": 1200.00,
    "Mouse": 25.50,
    "Keyboard": 75.00,
    "Monitor": 300.00,
}

# Calculate the total bill
grand_total = calculate_total_bill(shopping_cart)

# Print the final bill
print("-" * 30)
print(f"Total Bill Amount : ${grand_total:>.2f}")
print("-" * 30)  