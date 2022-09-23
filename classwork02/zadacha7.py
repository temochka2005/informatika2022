f = open('input7.txt', 'r', encoding='utf-8')
lines = f.readlines()
lines = filter(None, (line.rstrip() for line in lines))
d = {'9': 0, '10': 0, '11': 0}
for line in lines:
    a, b, c, k = map(str, line.split())
    if d[c] < int(k):
        d[c] = int(k)
for i in d:
    if d[i]>=80:
        print(d[i],end=' ')