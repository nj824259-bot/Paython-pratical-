# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:28:17 2026

@author: nayan jadhav
"""

import streamlit as st

# Title
st.title("Student Result Calculator App")

# Student Name
name = st.text_input("Enter Student Name")

# Subject Marks
mark1 = st.number_input("Enter Marks of Subject 1", min_value=0, max_value=100)
mark2 = st.number_input("Enter Marks of Subject 2", min_value=0, max_value=100)
mark3 = st.number_input("Enter Marks of Subject 3", min_value=0, max_value=100)
mark4 = st.number_input("Enter Marks of Subject 4", min_value=0, max_value=100)
mark5 = st.number_input("Enter Marks of Subject 5", min_value=0, max_value=100)

# Button
if st.button("Calculate Result"):

    # Total and Percentage
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5

    # Grade Calculation
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Display Result
    st.subheader("Student Result")

    st.write("Student Name:", name)
    st.write("Total Marks:", total)
    st.write("Percentage:", percentage, "%")
    st.write("Grade:", grade)