import streamlit as st
import time
import numpy as np
import pandas as pd

st.title('Test Application')

st.write("Here's our first attempt at using data to create a table:")

st.title('See Dataframe')
df = pd.read_csv("Data/breast-cancer-winsconsin.csv")
st.write(df.head(20))

st.title('Radius and texture plots')
st.line_chart(df[['radius_mean', 'texture_mean']])

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()

st.button("Re-run")