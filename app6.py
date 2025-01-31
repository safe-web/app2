import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify, Eq, solve, symbols

st.title("Calculator Experiment 1")

mode = st.radio("mode:", ("calculate", "plot", "solve equation"))

if mode == "calculate":
    st.write("Please enter your expression")
    st.write("@ for log, ^ for **, # for sqrt, pi = 3.14……, e = 2.718……")
    expression = st.text_input("Expression:")
    arc = st.radio("'arc'mode",('off','on'))

    if st.button("Calculate"):
        try:
            if arc == 'on':
                expression = expression.replace('asin', 'math.asin')
                expression = expression.replace('acos', 'math.acos')
                expression = expression.replace('atan', 'math.atan')
                expression = expression.replace("'", "/180*math.pi")
                expression = expression.replace('pi', 'math.pi')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('@', 'math.log')
                expression = expression.replace('#', 'math.sqrt')
                expression = expression.replace('^',"**")
            else:
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('e', 'math.e')
                expression = expression.replace("'", "/180*math.pi")
                expression = expression.replace('pi', 'math.pi')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('@', 'math.log')
                expression = expression.replace('#', 'math.sqrt')
                expression = expression.replace('^',"**")
            
            result = eval(expression)
            st.write("Result:", result)

            if "calculator_history" not in st.session_state:
                st.session_state.calculator_history = []
            st.session_state.calculator_history.append((expression, result))

        except Exception as e:
            st.write("Error:", e)


    if 'calculator_history' in st.session_state:
        if st.session_state.calculator_history:
            st.write("History:")
            for expr, res in st.session_state.calculator_history:
                st.write(expr, "=", res)
        else:
                st.write("No history.")
    else:
            st.write("No history")



elif mode == "plot":
    st.write("Please enter your expression")
    expression = st.text_input("Expression:")

    if st.button("plot"):
        try:
            func_expr = sympify(expression)
            x_min = float(st.number_input("Minimum：", value=-10.0))
            x_max = float(st.number_input("Maximum：", value=10.0))
            x = np.linspace(x_min, x_max, 1000)

            func = lambdify('x', func_expr, 'numpy')
            y = func(x)

            plt.figure(figsize=(10, 5))
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Graph of the function')
            plt.grid(True)
            st.pyplot(plt)
            if "mapping_history" not in st.session_state:
                st.session_state.mapping_history = []
                st.session_state.mapping_history.append(expression)
        except Exception as e:
            st.write("Error:", e)

    if 'mapping_history' in st.session_state:
        if st.session_state.mapping_history:
            st.write("History:")
            for items in st.session_state.mapping_history:
                st.write(items)
        else:
            st.write("No history.")
    else:
        st.write("No history.")

        

elif mode == "solve equation":
    st.write("enter equation（e.g ：x^2 - 4 = 0）")
    equation_input = st.text_input("Equation:")

    if st.button("solve"):
        try:
            if "equation_history" not in st.session_state:
                st.session_state.equation_history = []
            left_expr, right_expr = equation_input.split('=')
            x = symbols('x')
            left_expr = sympify(left_expr)
            right_expr = sympify(right_expr)
            equation = Eq(left_expr, right_expr)
            solutions = solve(equation, x)

            for i in range(0,len(solutions)):
                st.write("x",i+1, solutions[i])
                st.session_state.equation_history.append((equation_input,solutions[i]))
        

        except Exception as e:
            st.write("Error:", e)
    if 'equation_history' in st.session_state:
        if st.session_state.equation_history:
            st.write("History:")
            for expr, rel in st.session_state.equation_history:
                st.write(expr,rel)
        else:
            st.write("No history.")
    else:
        st.write("No history.")

        


