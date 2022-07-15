import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np

st.title("Crypto Dashboard")

url = "https://crypto.com/price"

# Requests Module gets HTML data
header = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
r = requests.get(url, headers=header)

html = pd.read_html(r.text)
df = html[0] # Set dataframe to be the first table if multiple on page
df = df.drop(df.columns[[0,1,2,3,7,8]], axis=1)

# BS Scraping:
soup = bs(r.content, "html.parser")
coinnames = []
mydivs = soup.find_all("a", {"class": "chakra-text css-o2rp9n"})
for v in mydivs:
    coinnames.append(v.text)
prices = []
initprices = soup.find_all("div", {"class": "css-b1ilzc"})
for v in initprices:
    prices.append(v.text)

df.insert(0, "Name", coinnames)
df.insert(1, "Price", prices)

df

# ToDo: Fix Sorting on each column
# Add more visuals in streamlit,new tools

    

