import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')

def hello(name):
    return 'Hello ' + name
first_variable = st.text_input('What's your name?')
if first_variable:
    st.write(hello(first_variable))
