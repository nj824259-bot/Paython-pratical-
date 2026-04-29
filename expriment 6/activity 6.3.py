

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:59:13 2026

@author: nayan jadhav
"""

file = open("complaints.txt", "w")
file.write("Late service\nPoor quality\nDelay in response")
file.close()

file = open("complaints.txt", "r")
data = file.read()
print("Complaints:\n", data)
file.close()