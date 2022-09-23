import numpy as np
b=np.array(range(1,100)).reshape(33, 3)
summa = np.array([sum(x) for x in b]).reshape(11,3).T
v=np.array(range(-9,2))
proizv=summa*v
print(proizv)