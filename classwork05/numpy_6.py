import numpy as np
np.random.seed(2)
print(np.linspace(0,120,120).reshape(12, 10), "\n")
print("max в столбце: ", np.linspace(0,120,120).reshape(12, 10).max(axis=1), "\n"  )
print("min в столбце: ", np.linspace(0,120,120).reshape(12, 10).min(axis=1), "\n"  )