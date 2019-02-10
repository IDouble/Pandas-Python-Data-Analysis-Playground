import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Print 10 Rows from Dateframe with Integer Index from 10-20

print(df.iloc[10:20])