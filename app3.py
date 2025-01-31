import streamlit as st

# 初始化历史记录
if 'history' not in st.session_state:
    st.session_state.history = []

# 用户输入
user_input = st.text_input("输入内容:")
if st.button("保存"):
    st.session_state.history.append(user_input)  # 将用户输入保存到历史记录

# 显示历史记录
st.write("历史记录:")
for item in st.session_state.history:
    st.write(item)  # 显示所有保存的历史记录
