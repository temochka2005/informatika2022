import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

titanicNOnulls=titanic.dropna(subset=['age'],how='all')


def group(pclass, sex):
    group0 = titanicNOnulls[(titanicNOnulls['pclass']==pclass)&(titanicNOnulls['sex']==sex)].sort_values(by="age", ascending = False)
    group1 = group0[:len(group0)//2]
    group2 = group0[len(group0)//2:]
    return group1, group2


for pclass in range(1, 4):
    for sex in ['male', 'female']:
        print(group(pclass, sex))