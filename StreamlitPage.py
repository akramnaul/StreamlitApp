import streamlit as st
from PIL import Image

st.header("StreamlitPage Header")
st.title("StreamlitPage Title")
st.write("Hello StreamlitPage !")

# opening the image
image = Image.open('A.jpg')

#displaying the image on streamlit app
st.image(image, caption='Enter any caption here')
