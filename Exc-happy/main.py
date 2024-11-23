import streamlit as st
import plotly.express as px
import pandas as pd

# Add a title widget
st.title("In Search for Happiness")

#Add two selectboxes
option_x = st.selectbox("Select the data for the X axis",
                        ("GDP", "Happiness", "Generosity"))

option_y = st.selectbox("Select the data for the Y axis",
                        ("GDP", "Happiness", "Generosity"))

# Load the dataframe
df = pd.read_csv("happy.csv")
opt_x_lower = str(option_x).lower()
opt_y_lower = str(option_y).lower()

st.subheader("GDP and Happiness")


def get_data(opt_x, opt_y):
    option_x = df[opt_x]
    option_y = df[opt_y]
    return option_x, option_y

x, y = get_data(opt_x_lower,opt_y_lower)

figure = px.strip(df, x={opt_x_lower}, y={opt_y_lower})
st.plotly_chart(figure)
