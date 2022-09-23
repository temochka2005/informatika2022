n = int(input())
d = dict()
for i in range(n):
    s = input().split()
    d[i+1] = s[0]
    d[-i-1] = s[1]
word = input()
print(d)
for k in range(-len(d)-1, len(d)+2):
    if word == d[k]:
        print(d[-k])