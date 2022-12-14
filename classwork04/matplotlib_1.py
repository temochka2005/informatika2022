import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)
y = (x**(-2))*np.sin(x*np.pi/180)
plt.plot(x, y, 'bs')
plt.plot(x,y)
plt.show()