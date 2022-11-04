import random
import numpy as np
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
def func():
    i=np.sort(random.sample(range(len(diamonds)), 20))
    return diamonds.iloc[i]
print(func())