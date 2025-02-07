import numpy as np
import pandas as pd
import streamlit as st 

st.title("Welcome Everyone we are learning python")
st.write("Python Requires practice")

data=pd.DataFrame({
    'player_name':['sachin','virat','dhoni','rohit'],
    'Runs':['100','23','67','56']})
st.write(data)
chart_data=pd.DataFrame(np.random.rand(20,4),columns=['sachin','virat','dhoni','rohit'])
st.area_chart(chart_data)
