with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.rstrip().split(), a))
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])
print(a)
b = [[a[i][j] ** 2 for j in range(len(a[i]))] for i in range(len(a))]
print(b)
b = [[str(x) for x in b[i]] for i in range(len(b))]
with open("output.txt", "w") as f:
    f.writelines([" ".join(x) + "\n" for x in b])