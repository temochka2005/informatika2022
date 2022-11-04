import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanicNOnulls=titanic.dropna(subset=['age'],how='all')

def group(pclass, sex):
    group0 = titanicNOnulls[(titanicNOnulls['pclass']==pclass)&(titanicNOnulls['sex']==sex)].sort_values(by="age", ascending = False)
    group1 = group0[:len(group0)//2]
    group2 = group0[len(group0)//2:]
    return group1, group2


cl1mo, cl1my = group(1, 'male')
cl2mo, cl2my = group(2, 'male')
cl3mo, cl3my = group(3, 'male')
cl1fo, cl1fy = group(1, 'female')
cl2fo, cl2fy = group(2, 'female')
cl3fo, cl3fy = group(3, 'female')

f = pd.DataFrame({"male younger": [cl1my['survived'].mean(), cl2my['survived'].mean() , cl3my['survived'].mean()],
"male older": [cl1mo['survived'].mean(), cl2mo['survived'].mean() , cl3mo['survived'].mean()],
"female younger": [cl1fy['survived'].mean(), cl2fy['survived'].mean() , cl3fy['survived'].mean()],
"female older": [cl1fo['survived'].mean(), cl2fo['survived'].mean() , cl3fo['survived'].mean()]}, index = ["1", "2", "3"])
print(f)