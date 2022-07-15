df = df.drop(df.columns[[0, 1, 3]], axis=1) # Drop Columns 0, 1 and 3

df = df.drop(df.columns[[0, 1, 3]], axis=0) # Drop Rows 0, 1 and 3

df = df.drop('column_name', axis=1) # Drop column 'column_name'