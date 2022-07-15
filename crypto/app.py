from soupsieve import select_one
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

st.title("Crypto Dashboard")

st.markdown("""Data from https://crypto.com/price  
    Modules used: **Streamlit, Requests, Pandas, BS4**
            """)

url = "https://crypto.com/price"

# Requests Module gets HTML data
header = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
r = requests.get(url, headers=header)

html = pd.read_html(r.text)
df = html[0] # Set dataframe to be the first table if multiple on page
df = df.drop(df.columns[[0,1,2,3,4,7,8]], axis=1)

# BS Scraping:
soup = bs(r.content, "html.parser")
coinnames = [] # Coinname column
mydivs = soup.find_all("a", {"class": "chakra-text css-o2rp9n"})
for v in mydivs: 
    coinnames.append(v.text)
prices = [] # Price column
initprices = soup.find_all("div", {"class": "css-b1ilzc"})
for v in initprices: 
    temp = v.text 
    vall = float(temp.replace(',','').replace('$', '')) # Convert str price to float
    prices.append(vall)

df.insert(0, "Name", coinnames)
df.insert(1, "Price ($)", prices)
df = df.astype(str)
df

# Add more visuals in streamlit,new tools

#Chart showing coin price history for selected coin

coin = "bitcoin"
newurl = f"https://uk.investing.com/crypto/{coin}/historical-data"
# Request
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
r2 = requests.get(newurl)
soup2 = bs(r2.content, "html.parser")
html = pd.read_html(r2.text)
testdf = html[0]
histdate = []
histopen = []
for v in testdf["Date"]:
    histdate.append(v)
for v in testdf["Open"]:
    histopen.append(v)
df2 = pd.DataFrame(histopen, histdate)
tab1, tab2 = st.tabs(["Dataframe", "Area Chart"])
with tab1:
    df2
with tab2:
    st.area_chart(df2)