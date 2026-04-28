# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:02:44 2026

@author: nayan jadhav
"""

# Roll numbers of students present in Class A
attendance_class_a = {101, 102, 103, 104, 105}

# Roll numbers of students present in Class B
attendance_class_b = {104, 105, 106, 107, 108}

# Method 1: Using the intersection() method
present_in_both_method = attendance_class_a.intersection(attendance_class_b)

# Method 2: Using the & operator (a shortcut for intersection)
present_in_both_operator = attendance_class_a & attendance_class_b

# Print the results
print(f"Students present in Class A: {attendance_class_a}")
print(f"Students present in Class B: {attendance_class_b}")
print(f"Students present in both classes (using .intersection()): {present_in_both_method}")
print(f"Students present in both classes (using & operator): {present_in_both_operator}")