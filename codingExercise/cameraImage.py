import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Add image browser
upload_image = st.file_uploader("Upload Image")

if upload_image:
    upload_img = Image.open(upload_image)
    gray_upload_image = upload_img.convert("L")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

# Render the grayscale image on the webpage
if camera_image:
    st.image(gray_img)
elif upload_image:
    st.image(gray_upload_image)
