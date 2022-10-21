def task1():
    # TODO: первое задание
    a = int(input())
    b = int(input())
    print(a ** 2 - b ** 2)
def task2():
    # TODO: второе задание
    a = list(input())
    k = 0
    print(a)
    for a in a:
        if (ord(a) >= 65 and ord(a) <= 90):
            k += 1
    print(k)
def task3():
    # TODO: третье задание
    a = input().split()
    k = 0
    for a in a:
        for i in range(len(list(a))):
            if a[i] == "s" and a[i + 1] == "u" and a[i + 2] == "s":
                k += 1
                break
    print(k)
def task4(generator):
    # TODO: четвертое задание
    def foo(generator):
        return list(filter(lambda x: (x % 2 == 0), generator))

    print(foo(generator))
def task5(list_of_smth):
    # TODO: пятое задание
    def kkk(list_of_smth):
        return list_of_smth[5:-1:2]
    print(*kkk(list_of_smth))


def task6(list1, list2, list3, list4):
#TODO: шестое задание
    def union(list1, list2, list3, list4):
        return ((list1 & list2) | (list3 & list4))

    print(union(list1, list2, list3, list4))

def task7():
    # TODO: ...
    import numpy as np
    def matrixFUNC():
        np.random.seed(16)
        matrix = np.random.randint(37, size=36).reshape(6, 6)
        removed = matrix[:-1:, 1::]
        minor = np.linalg.det(removed)
        return (removed, minor)

    print(*matrixFUNC())
def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...
    def otrisovka(f, min_x, max_x, N, min_y, max_y):
        from scipy import misc
        import numpy as np
        import matplotlib.pyplot as plt
        # Логарифмический масштаб по оси x (аналогично для y)
        plt.xscale('log')
        plt.yscale('log')
        # Сетка
        plt.grid(True)
        # Добавляем данные
        k = (max_x - min_x) / N
        x = np.arange(min_x, max_x, k)
        # График синий, штрихованный
        plt.ylim(min_y, max_y)
        plt.plot(x, f(x), 'b--')

        # proizvodnaya_y = misc.derivative(f, x, dx=1e-2)
        # plt.plot(x, proizvodnaya_y)

        def proizvodnaya(x):
            for i in range(len(x)):
                dx = x[i + 1] - x[i]
                dydx = np.gradient(f(x), dx)
                return dydx

        plt.plot(x, proizvodnaya(x))
        plt.savefig('function.pdf')

        plt.show()
def task9(data, x_array, y_array, threshold):
    # TODO: ...
    def histogramma(data, x_array, y_array, threshold):
        import numpy as np
        from matplotlib import pyplot as plt
        x1, y1, data1 = ([], [], [])
        for k in data:
            x1.append(k[0])
            y1.append(k[1])
            data1.append(sum(o))

        plt.hist(x1)
        plt.savefig(' histograms_0.png')
        plt.show()
def task10(list_of_smth, n):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
