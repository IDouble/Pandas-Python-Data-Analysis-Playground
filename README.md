# 🐍 Pandas Python Data Analysis Playground 📊📈
🐍 Python Data Analysis with the Pandas Library 📊📈

## Installation Pandas ⬇️ 
The easiest way to install Pandas is with pip. Type in your console:
```
pip install pandas
```

## Print Rows from a Dateframe using an Integer Index 🗃
Print 10 Rows from a Dateframe using an Integer Index from 10-20. (Method .iloc[from:to])
```
import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Print 10 Rows from Dateframe using an Integer Index from 10-20

print(df.iloc[10:20])
```

## Print the first Rows from a Dateframe 🗃
Print the first 10 Rows from a Dateframe. (Method .head(10))
```
import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Print the first 10 Rows from the Dateframe

print(df.head(10))
```


## Print Rows from a Dateframe and sort them with an attribute 🗃
Print 10 Rows from a Dateframe using an Integer Index from 0-10 and sort them with an attribute. (Method .sort_values(["Start Time"]))
```
import pandas as pd

df = pd.read_csv("new_york_city.csv")

# Prints the first 10 Rows, sorted by Start Time

print(df.iloc[0:10].sort_values(["Start Time"]))
```
