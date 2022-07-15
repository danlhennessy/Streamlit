import requests
import pandas as pd


def webtoDF(url):
    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=header)
    html = pd.read_html(r.text)
    df = html[0] # Set dataframe to be the first table if multiple on page
    df
    
df = df.drop(df.columns[[0, 1, 3]], axis=1) # Drop Columns 0, 1 and 3

df = df.drop(df.columns[[0, 1, 3]], axis=0) # Drop Rows 0, 1 and 3

df = df.drop('column_name', axis=1) # Drop column 'column_name'