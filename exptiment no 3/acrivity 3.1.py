
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:14:31 2026

@author:  nayan jadhav
"""

# Define the items for a single receipt (can be a list or dictionary)
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
# Define the number of copies to print
num_copies = 3

# Outer loop iterates for the number of copies
for copy_num in range(1, num_copies + 1):
    print(f"--- Receipt Copy #{copy_num} ---")
    
    # Inner loop iterates through the items of the receipt
    for item_num, item_name in enumerate(items, 1):
        print(f"  Item {item_num}: {item_name}")
        
    # Print a separator and an extra newline for clarity between receipts
    print("-" * 25)
    print("\n")