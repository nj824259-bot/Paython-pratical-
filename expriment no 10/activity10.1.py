# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:11:58 2026

@author:nayan jadhav
"""

import streamlit as st
import random

# Title
st.title("🎯 Number Guessing Game")

# Initialize session state
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0

# Instructions
st.write("Guess a number between 1 and 100")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check button
if st.button("Check Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.random_number:
        st.warning("📉 Too low! Try again.")
    elif guess > st.session_state.random_number:
        st.warning("📈 Too high! Try again.")
    else:
        st.success(
            f"🎉 Correct! The number was {st.session_state.random_number}."
        )
        st.info(f"You guessed it in {st.session_state.attempts} attempts.")

# Restart button
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("🔄 Game restarted! Guess the new number.")