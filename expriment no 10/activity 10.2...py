# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:20:05 2026

@author:nayan jadhav
"""

import streamlit as st

# Title
st.title("Grocery Bill Calculator")

st.write("Enter grocery item details below")

# Input fields
item1 = st.text_input("Enter first item name")
price1 = st.number_input("Enter price of first item", min_value=0.0)

item2 = st.text_input("Enter second item name")
price2 = st.number_input("Enter price of second item", min_value=0.0)

item3 = st.text_input("Enter third item name")
price3 = st.number_input("Enter price of third item", min_value=0.0)

# Calculate button
if st.button("Calculate Bill"):

    total = price1 + price2 + price3

    st.subheader("Bill Summary")
    st.write(f"{item1}: ₹{price1}")
    st.write(f"{item2}: ₹{price2}")
    st.write(f"{item3}: ₹{price3}")

    st.success(f"Total Grocery Bill = ₹{total}")