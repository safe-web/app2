import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify


st.title("calculator experiment 1")

st.write("Please enter your expression below")
st.write("@ -> log, ** -> ^, # -> sqrt, pi = 3.14……, e = 2.718……")
expression = st.text_input("Expression:")

if 'arc' not in st.session_state:
    st.session_state.arc = False

if st.button("Open 'arc' mode"):
    st.session_state.arc = True

if st.button("Close 'arc' mode"):
    st.session_state.arc = False

st.write("Arc mode is:",st.session_state.arc)

if st.button("Calculate"):
    try:
        if st.session_state.arc == True:
            expression = expression.replace('asin','math.asin')
            expression = expression.replace('acos','math.acos')
            expression = expression.replace('atan','math.atan')
            expression = expression.replace("'","/180*pi")
            expression = expression.replace('pi','math.pi')
            expression = expression.replace('log','math.log')
            expression = expression.replace('@','math.log')
            expression = expression.replace('#','math.sqrt')
        else:   
            expression = expression.replace('sin','math.sin')
            expression = expression.replace('cos','math.cos')
            expression = expression.replace('tan','math.tan')
            expression = expression.replace('e','math.e')
            expression = expression.replace("'","/180*pi")
            expression = expression.replace('pi','math.pi')
            expression = expression.replace('log','math.log')
            expression = expression.replace('@','math.log')
            expression = expression.replace('#','math.sqrt')
        result = eval(expression)
        st.write("Result:",result)
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append((expression,result))
    except Exception as e:
        st.write("Error found in:",e)
if 'history' in st.session_state:  
    if st.session_state.history:
        st.write("History:")
        for expression, result in st.session_state.history:
            st.write(expression, "=", result)
    else:
        st.write("No history.")
else:
    st.write("No history.")
