# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:02:49 2026

@author: nayan
"""

import random

def generate_otp():
    otp = ""
    for i in range(6):  # 6-digit OTP
        otp += str(random.randint(0, 9))
    return otp

# Generate and display OTP
otp = generate_otp()
print("Your OTP is:", otp)