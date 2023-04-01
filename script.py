"""
.) Pandas is a high level data manipulation tool developed by Wes McKinney built on 
Numpy package.
.) We store tabular data in DataFrame.

DataFrame from dictionary:
.) Keys are the column lables.
.) Values(data, column by column)
"""
import pandas as pd

world = {
    "country": ["Brazil", "Russia", "India", "China", "South Afria"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.read_csv("brics.csv", index_col=0)
# read_csv contains many argument's to customize your data import.
# index_col = 0 means first column contains the row indexes.
print(brics)

# brics = pd.DataFrame(world)
# brics.index = ["BR", "RU", "IN", "CH", "SA"]
# print(brics)
