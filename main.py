import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd

# Read Data
df = pd.read_csv("Data/housing.csv")
column_selector = df.drop('ocean_proximity', axis=1)

# Add Sidebar to the application
sidebar_selectbox_value = st.sidebar.selectbox(
    'Please Choose column to plot in the second graph',
    column_selector.columns
)

st.title('Example service created to showcase some of the features of the application')

st.write("We will use a housing dataset used in book Hands On Machine Learning with Scikit Learn and Tensorflow for "
         "regression tasks")

st.subheader('First 20 rows of the dataset')
st.write(df.head(20))

st.subheader('Histogram of %s column from dataset' % sidebar_selectbox_value)
histogram_data, bins = np.histogram(df[sidebar_selectbox_value], bins=45)
st.bar_chart(histogram_data)

st.subheader('Plot House points from dataset on map')
map_data = df[['latitude', 'longitude']]
st.map(map_data)

st.subheader('Filter ocean proximity using selectbox')
option = st.selectbox(
    'Which Ocean Proximity you want to see',
    np.unique(df['ocean_proximity']))

'You selected: ', option
st.write(df[df['ocean_proximity'] == option].head(20))

st.subheader("See different ocean proximity points on map")
left_column, right_column = st.columns(2)
with left_column:
    chosen = st.radio(
        'Choose Ocean Proximity Here', np.unique(df['ocean_proximity'])
    )

with right_column:
    len_data = len(df[df['ocean_proximity'] == chosen]['median_income'])
    st.write("Number of Houses in this range is : %s" % (len_data))
    map_data = df[df['ocean_proximity'] == chosen][['latitude', 'longitude']]
    st.map(map_data)

st.subheader("Control House price and see on map and datase")
x = st.sidebar.slider('Choose minimal price of houses', min(df['median_house_value']), max(df['median_house_value']))
left_column, right_column = st.columns(2)
with left_column:
    st.write("Number of rooms and bedrooms in houses with price over selected")
    st.write(df[df['median_house_value'] > x][['total_rooms', 'total_bedrooms']])

with right_column:
    len_data = len(df[df['ocean_proximity'] == chosen]['median_income'])
    st.write("Number of Houses in this range is : %s" % (len_data))
    map_data = df[df['median_house_value'] > x][['latitude', 'longitude']]
    st.map(map_data)


st.subheader("Latex can also be added to the page")
st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)''')


st.subheader('Use checkbox to show or hide the chart')
if st.checkbox('Show Chart'):
    # Draw the histogram
    histogram_data, bins = np.histogram(df[sidebar_selectbox_value], bins=45)
    st.bar_chart(histogram_data)

st.button("Restart the page")