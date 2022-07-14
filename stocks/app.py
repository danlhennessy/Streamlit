import streamlit as st
import pandas as pd

st.title("Stocks Price Web App")

st.markdown("""
            This app retrieves data from Wikipedia of the top 500 S&P, and displays the closing price in a Pandas dataframe
            * **Data Source:** [Wikipedia](https://www.Wikipedia.org)
            """)