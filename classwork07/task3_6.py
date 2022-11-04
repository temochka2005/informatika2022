import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanicNOnulls=titanic.dropna(subset=['age'],how='all')

x=[]
y=[]
for i in range(20):
    y.append(titanicNOnulls[(titanicNOnulls['age']>=5*i)&(titanicNOnulls['age']<5*(i+1))].agg({'survived': 'mean'})[0])
    x.append(i*5)
plt.plot(x,y)
plt.show()