import streamlit as st
import math

st.title("Calculator Experiment 1")

st.write("Please enter your expression below")
st.write("@ -> log, ** -> ^, # -> sqrt, pi = 3.14……, e = 2.718……")
expression = st.text_input("Expression:")

# 初始化 arc 模式
if 'arc' not in st.session_state:
    st.session_state.arc = False

if st.button("Open 'arc' mode"):
    st.session_state.arc = True

if st.button("Close 'arc' mode"):
    st.session_state.arc = False

st.write("Arc mode is:", st.session_state.arc)

# 计算按钮
if st.button("Calculate"):
    try:
        # 替换表达式
        if st.session_state.arc:
            expression = expression.replace('asin', 'math.asin')
            expression = expression.replace('acos', 'math.acos')
            expression = expression.replace('atan', 'math.atan')
            expression = expression.replace("'", "/180*math.pi")
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

        # 计算结果
        result = eval(expression)
        st.write("Result:", result)

        # 初始化历史记录
        if "history" not in st.session_state:
            st.session_state.history = []  # 确保初始化为列表

        # 添加到历史记录
        st.session_state.history.append((expression, result))

    except Exception as e:
        st.write("Error found in:", e)

# 显示历史记录
if 'history' in st.session_state:
    if st.session_state.history:  # 检查历史记录是否非空
        st.write("History:")
        for exp, res in st.session_state.history:
            st.write(f"Expression: {exp} => Result: {res}")
    else:
        st.write("No history.")
else:
    st.write("No history.")
