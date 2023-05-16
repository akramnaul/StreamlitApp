import streamlit as st
import subprocess
import sys

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')

def hello(name):
    return 'Hello ' + name
first_variable = st.text_input("What's your name ? ")
if first_variable:
    st.write(hello(first_variable))

subprocess.run([f"{sys.executable} ", "pypy.py"])
