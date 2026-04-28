# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:55:52 2026

@author: nayan jadhav
"""

#taking list input from the user 
n=int(input("enter number of element;"))
numbers=[]
for i in range(n):
    num=int(input(f"enter element {i+1}:"))
    numbers.append(num)
    # Calculating sum and average 
    total = sum(numbers)
    average=total /n if n> 0 else 0
    print("list:",numbers)
    print("sum of element:",total)
    print("Average of element:", average)
    