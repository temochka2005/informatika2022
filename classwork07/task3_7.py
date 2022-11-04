import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanicNOnulls=titanic.dropna(subset=['age'],how='all')

xmale=[]
ymale=[]
for i in range(20):
    ymale.append(titanicNOnulls[(titanicNOnulls['age']>=5*i)&(titanicNOnulls['age']<5*(i+1))&(titanicNOnulls['sex']=='male')].agg({'survived': 'mean'})[0])
    xmale.append(i*5)

xfemale=[]
yfemale=[]
for i in range(20):
    yfemale.append(titanicNOnulls[(titanicNOnulls['age']>=5*i)&(titanicNOnulls['age']<5*(i+1))&(titanicNOnulls['sex']=='female')].agg({'survived': 'mean'})[0])
    xfemale.append(i*5)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(xmale, ymale)
ax1.set_title('male')
ax2.plot(xfemale, yfemale)
ax2.set_title('female')
plt.show()