import numpy as np
np.random.seed(2)
print(np.linspace(0,120,120).reshape(12, 10), "\n")
print("max в столбце: ", np.linspace(0,120,120).reshape(12, 10).argmax(axis=0), "\n"  )
print("min в столбце: ", np.linspace(0,120,120).reshape(12, 10).argmin(axis=0), "\n"  )