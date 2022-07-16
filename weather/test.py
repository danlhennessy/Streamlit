import pandas as pd

date=["2022-07-16T15:00Z", "2022-07-16T18:00Z", "2022-07-16T21:00Z", "2022-07-17T15:00Z", "2022-07-16T18:00Z", "2022-07-16T21:00Z"]
temp = [24,27,24,21,32,45]

df = pd.DataFrame({"Temperature  °C" : temp}, index=date)

df.index = pd.to_datetime(df.index) # Convert Date Column to datetime from string

print(df)