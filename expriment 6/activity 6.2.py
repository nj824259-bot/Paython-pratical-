

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:55:37 2026

@author: nayan jadhav
"""

# Create and write file
file = open("attendance.txt", "w")
file.write("Rahul - Present\n")
file.write("Sneha - Absent\n")
file.close()

# Append new record
file = open("attendance.txt", "a")
file.write("Amit - Present\n")
file.close()

# Read file
file = open("attendance.txt", "r")
print(file.read())
file.close() 