

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 13:11:44 2026

@author:  nayan jadhav
"""

def simple_interest(principal,rate,time):
    si=(principal * rate * time)/100
    return si
# Taking input from the user 
p=float(input("Enter principle amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("enter time(in years):"))
# funcation call
interst=simple_interest(p,r,t)
print("simple interest is:", interest)