import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(10, 100)
k=-x*np.sin(x)
y =np.exp(k)
print(x)
print(k)
print(y)
plt.plot(x,y)
#plt.grid('visible', which='major', axis='both', alpha=1)
#plt.grid('visible', which='minor', axis='both', alpha=0.5)
plt.ylabel("Y")
plt.xlabel("X")

plt.show()