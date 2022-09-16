def dot_product(N,vector1,vector2):
    proizvedenie=0
    for i in range(N):
        proizvedenie+=vector1[i]*vector2[i]
    return(proizvedenie)
dot_product(3,[1,2,3],[4,5,6])
