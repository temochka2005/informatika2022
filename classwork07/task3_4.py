import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanicNOnulls=titanic.dropna(subset=['age'],how='all')

males = titanicNOnulls[(titanicNOnulls['sex']=='male')&(titanicNOnulls['survived']==1)].agg({'age': 'mean'})[0]
females = titanicNOnulls[(titanicNOnulls['sex']=='female')&(titanicNOnulls['survived']==1)].agg({'age': 'mean'})[0]

print("males: ", males, "females: ", females)