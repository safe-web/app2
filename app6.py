import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify, Eq, solve, symbols, diff, integrate, latex


def login():
    st.title("Login: ")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
        elif username == "Jeremy" and password == "24034":
            st.session_state.logged_in = True
        elif username == "David" and password == "24077":
            st.session_state.logged_in = True
        elif username == "Tony" and password == "24326":
            st.session_state.logged_in = True
        elif username == "Ben" and password == "24250":
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")
        
        if st.session_state.logged_in:
            st.rerun()
    
def main_app():
    st.title("The math helper")
    st.write("Jeremy - 24034 Tony-24326 Ben-24250 David-24077")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    mode = st.radio("mode:", ("calculate", "plot", "solve equation","calculus","unit converter"))

    if mode == "calculate":
        calculate_mode()
    elif mode == "plot":
        plot_mode()
    elif mode == "solve equation":
        equation_mode()
    elif mode == "calculus":
        calculus_mode()
    elif mode == "unit converter":
        unit_converter()
        

def calculate_mode():
    st.write("Please enter your expression")
    st.write("@() for log(), ^ / ** for square, #() for sqrt(), pi = 3.14……, e = 2.718……")
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
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('#', 'math.sqrt')
            expression = expression.replace('^', '**')
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
    else:
        st.write("No history.")

def plot_mode():
    st.write("Please enter your expression")
    expression = st.text_input("Expression:")
    x_min = st.number_input("Minimum：", value=-10)
    x_max = st.number_input("Maximum：", value=10)
    
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

def equation_mode():
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


def calculus_mode():
    st.write("Calculus Operations")
    operation = st.radio("Operation:", ("Differentiate", "Integrate"))
    expr_input = st.text_input("Enter expression (use 'x' as variable):")
    
    # 初始化 lower 和 upper 为默认值
    lower = ""
    upper = ""
    
    if operation == "Integrate":
        lower = st.text_input("Lower limit (leave empty for indefinite):")
        upper = st.text_input("Upper limit (leave empty for indefinite):")

    if st.button("Compute"):
        try:
            x = symbols('x')
            expr = sympify(expr_input)
            
            if operation == "Differentiate":
                result = diff(expr, x)
                st.latex(fr"\frac{{d}}{{dx}}({latex(expr)}) = {latex(result)}")
                
            elif operation == "Integrate":
                if lower or upper:
                    # 处理空字符串的情况（视为不定积分）
                    lower_val = sympify(lower) if lower.strip() else x
                    upper_val = sympify(upper) if upper.strip() else x
                    result = integrate(expr, (x, lower_val, upper_val))
                    limits = f"_{{{lower}}}^{{{upper}}}" if (lower or upper) else ""
                else:
                    result = integrate(expr, x)
                    limits = ""
                st.latex(fr"\int{limits} {latex(expr)}\,dx = {latex(result)}")

            # 保存历史记录（包含默认值）
            if "calculus_history" not in st.session_state:
                st.session_state.calculus_history = []
            st.session_state.calculus_history.append((operation, expr_input, lower, upper, result))

        except Exception as e:
            st.error(f"Error: {str(e)}")

    # 显示历史记录（适配不同操作）
    if 'calculus_history' in st.session_state and st.session_state.calculus_history:
        st.write("History:")
        for item in reversed(st.session_state.calculus_history):
            op, expr, l, u, res = item
            if op == "Differentiate":
                st.latex(fr"\frac{{d}}{{dx}}({latex(expr)}) = {latex(res)}")
            elif op == "Integrate":
                limits = f" from {l} to {u}" if (l or u) else ""
                st.latex(fr"\int{limits} {latex(expr)}\,dx = {latex(res)}")




if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    
if st.session_state.logged_in:
    main_app()
