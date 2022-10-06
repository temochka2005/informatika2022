#в ноутбуке задачки нет, поэтому пусть будет здесь
vvod = input()
new = ''
for i in vvod:
    if not(ord(i) == 32 or (ord(i) >=48 and ord(i) <=57) ):
        new += i
d = dict()
for i in new:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    d[i] = d[i]/len(new)
print(d)