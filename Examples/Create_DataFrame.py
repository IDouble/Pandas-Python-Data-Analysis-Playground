import pandas as pd

# Create data for the Data Frame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

# Create Data Frame
df = pd.DataFrame(data)

# Print out Data Frame & sort by field "year"
print(df.sort_values(["year"]))
