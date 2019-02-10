import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Prints the first 10 Rows, sorted by Start Time

print(df.iloc[0:10].sort_values(["Start Time"]))