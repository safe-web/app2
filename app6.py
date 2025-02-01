import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify, Eq, solve, symbols

# 登录验证
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # 简单验证（生产环境请使用安全验证方式）
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
    st.stop()

# 主程序
st.title("Calculator Experiment 1")

# 添加注销按钮
if st.button("Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

mode = st.radio("mode:", ("calculate", "plot", "solve equation"))

if mode == "calculate":
    st.write("Please enter your expression")
    st.write("@ for log, ^ for **, # for sqrt, pi = 3.14……, e = 2.718……")
    expression = st.text_input("Expression:")
    arc = st.radio("'arc'mode", ('off', 'on'))

    if st.button("Calculate"):
        try:
            if arc == 'on':
                expression = expression.replace('asin', 'math.asin')
                expression = expression.replace('acos', 'math.acos')
                expression = expression.replace('atan', 'math.atan')
            else:
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')

            expression = expression.replace("'", "/180*math.pi")
            expression = expression.replace('pi', 'math.pi')
            expression = expression.replace('e', 'math.e')
            expression = expression.replace('log', 'math.log')
            expression = expression.replace('@', 'math.log')
            expression = expression.replace('#', 'math.sqrt')
            expression = expression.replace('^', "**")

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
            for expr, res in reversed(st.session_state.calculator_history):
                st.write(f"{expr} = {res}")
        else:
            st.write("No history.")

elif mode == "plot":
    st.write("Please enter your expression")
    expression = st.text_input("Expression:")
    
    x_min = st.number_input("Minimum：", value=-10.0)
    x_max = st.number_input("Maximum：", value=10.0)
    
    if st.button("Plot"):
        try:
            if x_min >= x_max:
                raise ValueError("Maximum must be greater than Minimum")
                
            func_expr = sympify(expression)
            x = np.linspace(x_min, x_max, 1000)

            func = lambdify('x', func_expr, 'numpy')
            y = func(x)

            plt.figure(figsize=(10, 5))
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f'Graph of {expression}')
            plt.grid(True)
            st.pyplot(plt.gcf())
            
            if "mapping_history" not in st.session_state:
                st.session_state.mapping_history = []
            st.session_state.mapping_history.append(expression)      
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.write("History")
    if 'mapping_history' in st.session_state:
        if st.session_state.mapping_history:
            for item in reversed(st.session_state.mapping_history):
                st.code(item)
        else:
            st.write("No history")
    else:
        st.write("No history")

elif mode == "solve equation":
    st.write("Enter equation (e.g.: x^2 - 4 = 0)")
    equation_input = st.text_input("Equation:")

    if st.button("Solve"):
        try:
            left_expr, right_expr = equation_input.split('=')
            x = symbols('x')
            equation = Eq(sympify(left_expr), sympify(right_expr))
            solutions = solve(equation, x)

            st.write("Solutions:")
            for i, sol in enumerate(solutions):
                st.write(f"x{i+1}: {sol}")

            if "equation_history" not in st.session_state:
                st.session_state.equation_history = []
            st.session_state.equation_history.append((equation_input, solutions))

        except Exception as e:
            st.write("Error:", e)

    if 'equation_history' in st.session_state:
        if st.session_state.equation_history:
            st.write("History:")
            for expr, sols in reversed(st.session_state.equation_history):
                st.write(f"Equation: {expr}")
                for i, sol in enumerate(sols):
                    st.write(f"x{i+1}: {sol}")
        else:
            st.write("No history.")
    else:
        st.write("No history.")
