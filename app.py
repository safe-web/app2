import math
import streamlit as st
import random

st.title("my first experiment")

st.write("Enter text")
expression=st.text_input("expression:)

result=None


if st.button("Calculate"):
    try:
        result=eval(expression)
        st.write("result:",result)
    except exception as e:
        st.write("we find error in", e)

if st. button("guess"):
    correct=False
    guess=None
    answer=random.randint(1,100)
    if 'answer' not in st.session_state:
        st.session_state.answer = answer
    else:
        st.session_state.answer = random.randint(1, 100)

    while correct==False:
        guess = st.number_input("PLEASE GUESS (1-100)", min_value=1, max_value=100, key=f"guess_input_{st.session_state.answer}")
        if st.session_state.answer==guess:
            correct=True
            st.write("Correct")
        if st.session_state.answer>guess:
           st.write("too small")
        if st.session_state.answer<guess:
            st.write("too big")

    
    
    









