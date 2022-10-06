import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(10, 100)
k= x ** 0.5 * np.sin(x)
y =np.exp(k)

plt.plot(x,y, 'o')
plt.grid('visible', which='major', axis='both', alpha=1)
plt.grid('visible', which='minor', axis='both', alpha=0.5)
plt.ylabel("$y = e^{\\sqrt{x}sin(x)}$")
plt.xlabel("x")
plt.minorticks_on()
plt.show()