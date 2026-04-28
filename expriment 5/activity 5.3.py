# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:03:33 2026

@author: nayan jadhav
"""

# The initial shop inventory dictionary (item name: quantity)
inventory = {
    'apple': 50,
    'banana': 100,
    'orange': 75
}

def add_stock(item_name, quantity_to_add):
    """
    Adds new stock to the inventory dictionary.

    If the item already exists, its quantity is increased.
    If the item does not exist, it is added as a new item.
    """
    if item_name in inventory:
        inventory[item_name] += quantity_to_add # Update existing quantity
        print(f"Updated stock for '{item_name}'. New quantity: {inventory[item_name]}")
    else:
        inventory[item_name] = quantity_to_add # Add new item
        print(f"Added new item '{item_name}' with quantity: {inventory[item_name]}")

# Example Usage:

# 1. Add stock for an existing item
add_stock('apple', 25)

# 2. Add a new item to the inventory
add_stock('grape', 60)

# Print the updated inventory
print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(f"- {item}: {quantity}") 