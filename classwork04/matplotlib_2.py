import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)
y = (x**(-2))*np.sin(x*np.pi/180)
plt.plot(x, y, 'bs')
plt.plot(x,y)
plt.grid('visible', which='major', axis='both', alpha=1)
plt.grid('visible', which='minor', axis='both', alpha=0.5)
plt.ylabel("Y")
plt.xlabel(r"X")

plt.show()