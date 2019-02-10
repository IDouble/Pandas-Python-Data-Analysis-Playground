# 🐍 Pandas-Python-Data-Analysis-Playground 📊📈
🐍 Python Data Analysis with the Pandas Library 📊📈

## Installation Pandas ⬇️ 
The easiest way to install Pandas is with pip. Type in your console:
```
pip install pandas
```

## Print Rows from Dateframe with Integer Index 🗃
Print 10 Rows from Dateframe with Integer Index from 10-20. (Method .iloc[from:to])
```
import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Print 10 Rows from Dateframe with Integer Index from 10-20

print(df.iloc[10:20])
```
