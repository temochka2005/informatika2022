import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

pclass = titanic.groupby('pclass').agg({'pclass': 'count'})

age = titanic.groupby('age').agg({'age': 'count'})

print(pclass,'\n')
print(age)