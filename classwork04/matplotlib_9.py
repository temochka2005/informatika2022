import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(50, 100)
y = x * np.sin(x)**2

plt.plot(x,y, label="grahp")
plt.plot(x,y,'o', label="dots")
plt.grid('visible', which='major', axis='both', alpha=1)
plt.grid('visible', which='minor', axis='both', alpha=0.5)
plt.yscale('log')
plt.ylabel("$y = xsin^2(x) (log scale)$")
plt.xlabel("x")
plt.minorticks_on()
plt.title("Хороший график")
plt.legend(loc=4)

plt.show()
