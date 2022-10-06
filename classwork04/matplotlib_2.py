import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 10,float)
y = (x**(-2))*np.sin(x)
plt.plot(x, y, 'bs')
plt.plot(x,y)
plt.grid('visible', which='major', axis='both', alpha=1)
plt.grid('visible', which='minor', axis='both', alpha=0.5)
plt.ylabel("$y=sin(x)x^2 $ ")
plt.xlabel(r"X")

plt.show()