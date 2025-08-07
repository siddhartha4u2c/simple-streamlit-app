import streamlit as st

st.title("Simple Greeting App 😊")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, **{name}**! 👋 Welcome to the Streamlit app.")p