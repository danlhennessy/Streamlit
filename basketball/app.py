import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np

st.title('NBA Player Stats')

chosenyear = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))

st.markdown("""
* **Python Libraries:** base64, pandas, streamlit            
* **Data Source:** [Basketball-reference.com](https://www.basketball-reference.com)            
            """)

st.subheader("Player Stats Per Game")

# Web Scraping:
@st.cache
def loadtable(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0] #  Selects first table from html data
    raw = df.drop(df[df.Age == "Age"].index) # Remove any row where Age column = "Age" (Useless Data)
    raw = raw.fillna('0.0')
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

stats = loadtable(chosenyear)
st.dataframe(stats)