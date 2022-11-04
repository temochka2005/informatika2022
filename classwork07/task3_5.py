import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanicNOnulls=titanic.dropna(subset=['age'],how='all')

print( titanicNOnulls[titanicNOnulls['survived']==1]['age'].std() )