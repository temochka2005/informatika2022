import numpy as np
from matplotlib import pyplot as plt

np.random.seed(42)
data = np.random.normal(5, size=(10000,))
x = data[:5000]
y = data[5000:]

xedges = np.linspace(-0.5, 10, 190)
yedges = np.linspace(-0.5, 10, 190)
distribution, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))

cs = plt.matshow(distribution)
plt.colorbar(cs)
plt.show()