N,M = map(int, input().split())
chisla=input().split()

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
shift(chisla,-M)
print(*chisla)
