import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds)

mask = (diamonds['x'] > 5) | (diamonds['y'] > 5) | (diamonds['z'] > 5)
print(diamonds[mask][["x","y","z"]])d