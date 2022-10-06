import numpy as np

import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y

student=18

plt.figure(figsize=(7,7))
plt.title(r"$DATA$")
plt.ylabel(r"$\rho, mm^{-3}$")
plt.xlabel(r"$\xi, cm$")
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)


x, y = fake_data_generator(student)
plt.plot(x, y)
deltaX = [(x[i+1]-x[i])/2 if i!=len(x)-1 else (x[i]-x[i-1])/2 for i in range(len(x))]
deltaY = np.abs(y)**0.5
plt.errorbar(x, y, xerr=deltaX, yerr=deltaY, fmt='.', ecolor='green', linestyle="None",)

y1 = y
x1 = [np.mean(x)]*len(y1)
plt.plot(x1,y1,"b--", label=("mean x = ",np.mean(x)))

x2 = x
y2 = [np.mean(y)]*len(x2)
plt.plot(x2,y2,"r--", label=("mean y = ",np.mean(y)))

p, v = np.polyfit(x, y, deg=1, cov=True)


x3 = x
y3 = [sum([p[j] * i ** (len(p) - j - 1) for j in range(1 + 1)]) for i in x]
plt.plot(x3, y3, "k-", label = "fit")






plt.legend(loc = 4)
plt.show()
