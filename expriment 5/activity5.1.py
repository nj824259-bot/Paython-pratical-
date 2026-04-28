# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:01:38 2026

@author: nayan jadhav
"""



# Sample list of purchased items
purchases = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'orange', 'apple']

# Count frequency
item_counts = count(purchases)

# Display results
print(item_counts)
# Output: Counter({'apple': 4, 'banana': 2, 'orange': 2})

# Iterate through results
for item, count in item_counts.items():
    print(f"{item}: {count}")