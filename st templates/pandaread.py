import pandas as pd

url = "https://en.wikipedia.org/wiki/Forbes%27_list_of_the_world%27s_highest-paid_athletes"

html = pd.read_html(url)
df = html[0] # Set dataframe to be the first table if multiple on page
print(df)