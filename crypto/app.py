import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

st.title("Crypto Dashboard")

toggle = st.sidebar.checkbox("Hide Historical Data")


st.markdown("""Data from https://crypto.com and https://uk.investing.com  
    Modules used: **Streamlit, Requests, Pandas, BS4**
            """)

st.subheader("Data for top 50 Crypto Currencies")



# Data Request and Parsing for 1st site
url = "https://crypto.com/price"
header = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
r = requests.get(url, headers=header)
html = pd.read_html(r.text)
df = html[0] # Set dataframe to be the first table if multiple on page
df = df.drop(df.columns[[0,1,2,3,4,7,8]], axis=1)
soup = bs(r.content, "html.parser")

# Creating main DataFrame
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

# Data Request and Parsing for 2nd site:

coin =  st.selectbox("Choose a coin to see historical data", coinnames, index=0)
newurl = f"https://uk.investing.com/crypto/{coin.lower()}/historical-data"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
r2 = requests.get(newurl)
soup2 = bs(r2.content, "html.parser")
html = pd.read_html(r2.text)
testdf = html[0]

# Image retrieval
imgdiv = soup2.select_one('.left.cryptoCurrentData')
st.image(imgdiv.find('img').attrs['src'])


# Creating 2nd DataFrame and formatting to display correctly as a graph
histdate = []
histopen = []
for v in testdf["Date"]:
    histdate.append(v)
for v in testdf["Open"]:
    histopen.append(v)
df2 = pd.DataFrame({"Date" : histdate, "Open Price ($)" : histopen})
df2.Date = pd.to_datetime(df2.Date) # Convert Date Column to datetime from string
df2.set_index("Date", inplace=True) # Set Date to be index

#Display Data
if not toggle:
    tab1, tab2 = st.tabs(["Area Chart", "Raw data"])
    with tab1:
        st.area_chart(df2["Open Price ($)"])
    with tab2:
        df2



