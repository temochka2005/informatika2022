import numpy as np
b=np.array(range(1,100)).reshape(33, 3)
summa = [sum(x) for x in b]
##for i in range(33):
    ##if i <= 97:
      ##  k = np.append(k, b[i]+b[i+1]+b[i+2])
        ##i += 3
    ##print(b[3*i-2],b[3*i-1],b[3*i])
    ##k = np.append(k, b[3*i-2]+b[3*i-1]+b[3*i])
print(summa)