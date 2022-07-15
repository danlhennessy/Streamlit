import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import matplotlib.pyplot as plt

st.title("Test Page")

#Test dataframe

#Test dataframe with lists

#Test Simple Graph

testindex = ["23rd", "24rd", "25rd", "26rd", "27rd", "28rd", "29rd", "30rd"]

nums = [11,22,34,4,5,6,7,8]
Date = ["23", "24", "25", "26", "27", "28", "29", "30"]
date1 = []

for v in Date:
    date1.append(float(v))

df = pd.DataFrame({"nom" : nums, "Date" : date1}, index=testindex)
df

# Area plot
st.area_chart(df["Date"])