import numpy as np
np.random.seed(2)
print(np.linspace(0,120,120).reshape(12, 10), "\n")
print("среднеквадратичное отклонение вдоль направления 0: ",np.linspace(0,120,120).reshape(12, 10).std(axis=0), "\n")
print("сумма вдоль направления 0: ",np.linspace(0,120,120).reshape(12, 10).sum(axis=0), "\n")
print("среднее вдоль направления 0: ",np.linspace(0,120,120).reshape(12, 10).mean(axis=0), "\n")

print("среднеквадратичное отклонение вдоль направления 1: ",np.linspace(0,120,120).reshape(12, 10).std(axis=1), "\n")
print("сумма вдоль направления 1: ",np.linspace(0,120,120).reshape(12, 10).sum(axis=1), "\n")
print("среднее вдоль направления 1: ",np.linspace(0,120,120).reshape(12, 10).mean(axis=1), "\n")