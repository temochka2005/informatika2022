def invert_array(arr, N):
    res = arr[:N]
    return list(reversed(res))
massiv=input().split()
N = int(input())
print(invert_array(massiv, N))

