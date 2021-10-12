import streamlit as st
import time
import numpy as np
import pandas as pd

st.title('Test Application')

st.write("Here's our first attempt at using data to create a table:")

st.title('First 20 Rows of housing dataset')
df = pd.read_csv("Data/housing.csv")
st.write(df.head(20))

st.title('Median Income and House Value Plots')
st.line_chart(df[['median_income', 'median_house_value']])

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()

st.button("Re-run")