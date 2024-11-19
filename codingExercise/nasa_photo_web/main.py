import streamlit as st
import requests

# Prepare API key and API url
api_key = "VJhPaQFypOfztTPabcAuTZjHsgxkOc9w4fZxdd5r"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
response = requests.get(url)
content = response.json()

# Extract the image title, url and explanation
title = content["title"]
urlImage = content["url"]
explanation = content["explanation"]


st.set_page_config(layout="wide")

enpty_col, col1, enpty_col1 = st.columns([1, 1.5, 1])
with col1:
    st.title(title)
    st.image(urlImage)
    st.text(explanation)



