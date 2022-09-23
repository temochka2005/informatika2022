import numpy as np
b=np.array(range(1,100)).reshape(33, 3)
summa = np.array([sum(x) for x in b]).reshape(11,3).T
print(summa)