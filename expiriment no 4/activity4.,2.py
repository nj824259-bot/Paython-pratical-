

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:04:23 2026

@author: nayan jadhav
"""

def calculate_total_bill_with_loop(price_list):
    """
    Calculates the total bill using a for loop.
    """
    total = 0
    for price in price_list:
        total += price
    return total

# Example Usage:
product_prices_loop = [10.50, 20.00, 5.25, 15.00]
total_bill_loop = calculate_total_bill_with_loop(product_prices_loop)
print(f"The total bill calculated with a loop is: ${total_bill_loop:.2f}")