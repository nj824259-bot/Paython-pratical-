# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:06:20 2026

@author: nayan jadhav
"""

import datetime

# Take date input from user
date_input = input("Enter date (YYYY-MM-DD): ")

# Convert string to date
date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

# Get weekday (0 = Monday, 6 = Sunday)
day = date_obj.weekday()

# Check weekend
if day == 5 or day == 6:
    print("Weekend - Office Closed")
else:
    print("Working Day - Attendance Required") 