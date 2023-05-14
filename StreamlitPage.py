import streamlit as st
from PIL import Image

st.header("StreamlitPage Header")
st.title("StreamlitPage Title")
st.write("Hello StreamlitPage !")

st.subheader('This is a subheader')
st.markdown('_Markdown_')
st.text('This is sample text')
st.latex(r''' e^{i\pi} + 1 = 10 ''')
st.caption('This is a caption')
