import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd

# Read Data
df = pd.read_csv("Data/housing.csv")

# Add Sidebar to the application
sidebar_selectbox_value = st.sidebar.selectbox(
    'Please Choose column to plot in the second graph',
    df.columns
)

st.title('Example service created to showcase some of the features of the application')

st.write("We will use a housing dataset used in book Hands On Machine Learning with Scikit Learn and Tensorflow for "
         "regression tasks")

st.subheader('First 20 rows of the dataset')
st.write(df.head(20))

st.subheader('Median Income and House Value Histograms')
histogram_data, bins = np.histogram(df['median_income'], bins=45)
st.bar_chart(histogram_data)

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


st.title("Widgets can also be placed Side-by-Side for better view")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:

# Or even better, call Streamlit functions inside a "with" block:
with left_column:
    chosen = st.radio(
        'Choose Ocean Proximity Here', np.unique(df['ocean_proximity'])
    )

with right_column:
    len = len(df[df['ocean_proximity'] == chosen]['median_income'])
    st.write("Number of Houses in this range is : %s" % (len))
    map_data = df[df['ocean_proximity'] == chosen][['latitude', 'longitude']]
    st.map(map_data)



st.button("Restart the page")