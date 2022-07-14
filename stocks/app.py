import streamlit as st
import pandas as pd
import yfinance as yf
import base64
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.title("Stocks Price Web App")

st.markdown("""
            This app retrieves data from Wikipedia of the top 500 S&P, and displays the closing price in a Pandas dataframe
            * **Data Source:** [Wikipedia](https://www.Wikipedia.org)
            """)


url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
html = pd.read_html(url, header = 0)
df = html[0]
df
    

# yfinance data
data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = list(df.Symbol),

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "5d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

choice = st.selectbox("Choose a company to show close prices for this year to date", list(df.Symbol))

closedf = pd.DataFrame(data[choice].Close)
closedf

st.area_chart(closedf)