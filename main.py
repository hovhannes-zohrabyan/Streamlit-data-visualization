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

st.title('Use checkbox to show or hide the chart')
if st.checkbox('Show Chart'):
    st.line_chart(df['median_house_value'])

st.title('Filter Dataset using Selectbox')
option = st.selectbox(
    'Which Ocean Proximity you want to see',
     np.unique(df['ocean_proximity']))

'You selected: ', option
st.write(df[df['ocean_proximity'] == option].head(20))


st.button("Restart the page")