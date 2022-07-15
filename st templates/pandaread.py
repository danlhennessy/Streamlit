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
    
