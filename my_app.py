import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st
#print("hello")

st.title(":blue[Test Data]")
st.write("This is a test file")

url="test_a_b.csv"
df=pd.read_csv(url)
#print(df)
st.dataframe(df)
st.write(df.shape[0])
n=(df.shape[0]-1)
st.write(n)











