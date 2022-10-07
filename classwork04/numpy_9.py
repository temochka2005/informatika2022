import numpy as np


def check_prime_number(m):
    if m == 1:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            return False
    else:
        return True


def prime_number(x):
    if x == 1:
        return 2
    if x == 2:
        return 3
    k = prime_number(x - 1) + 1
    while True:
        if check_prime_number(k):
            return k
        else:
            k += 1


def fibonacci_number(r):
    if r == 1:
        return 1
    if r == 2:
        return 1
    return fibonacci_number(r - 1) + fibonacci_number(r - 2)


vector1 = np.array([-prime_number(i) for i in range(1, 11)])
vector2 = np.array([fibonacci_number(i) for i in range(1, 11)])
print(vector1.dot(vector2))
