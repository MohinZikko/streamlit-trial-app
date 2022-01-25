import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np

st.title('Preventive analysis of Alzheimers disease using Machine learning.')
plot_types = (
    "Scatter",
    "Histogram",
    "Bar",
    "Line",
    "3D Scatter",
)
st.title("Enter Your CSV data:")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

chart_type = st.selectbox("Choose your chart type", plot_types)

