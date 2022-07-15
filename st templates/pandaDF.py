df = df.drop(df.columns[[0, 1, 3]], axis=1) # Drop Columns 0, 1 and 3

df = df.drop(df.columns[[0, 1, 3]], axis=0) # Drop Rows 0, 1 and 3

df = df.drop('column_name', axis=1) # Drop column 'column_name'

df.insert(0, "Name", coinnames) # Insert column at position 0

df.columns.values[0] = "b" # Rename column at position 0

df2 = pd.DataFrame({"Date" : histdate, "Open Price" : histopen}, index=["Whatever", "I", "Choose"]) # New df with list variables as columns

df2.Date = pd.to_datetime(df2.Date) # Convert Date Column to datetime from string

df2.set_index("Date", inplace=True) # Set Date to be index