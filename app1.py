import numpy as np
import pandas as pd
import streamlit as st 

st.title("Welcome Everyone we are learning python")
st.write("Python Requires practice")

data=pd.DataFrame({
    'c1':[10,20,30,40],
    'c2':['A','B','C','D']})
st.write(data)
chart_data=pd.DataFrame(np.random.rand(20,4),columns=['A','B','C','D'])
st.area_chart(chart_data)
