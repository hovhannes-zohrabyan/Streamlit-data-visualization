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
st.line_chart(df[['median_income']])

st.title('Map Plot of points from dataset')
map_data = df[['latitude', 'longitude']]
st.map(map_data)

st.title('Use checkbox to show or hide the chart')
if st.checkbox('Show Chart'):
    # Draw the histogram
    hist_values = np.histogram(
        df['median_house_value'], bins=24, range=(0, 24))[0]
    st.bar_chart(df['median_house_value'])

st.title('Filter Dataset using Selectbox')
option = st.selectbox(
    'Which Ocean Proximity you want to see',
     np.unique(df['ocean_proximity']))

'You selected: ', option
st.write(df[df['ocean_proximity'] == option].head(20))

st.title("Example of Latex in webpage")
st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)''')

st.title("Slider Control Example")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.button("Restart the page")