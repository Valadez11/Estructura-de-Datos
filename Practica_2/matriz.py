A = [[5, 6, 13], [3, 10, 1], [2, 11, 3]]
B = [[1, 2, 17], [6, 5, 15], [3, 11, 12]]
AB =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(len(A)):
    for j in range(len(B[0])):   
        for k in range(len(B)):
            AB[i][j] += A[i][k] * B[k][j]

print(AB)
#PRUEBAAA