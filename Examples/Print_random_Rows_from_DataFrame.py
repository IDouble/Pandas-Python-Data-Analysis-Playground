import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Print 10 random Rows from a Dateframe

print(df.sample(10))