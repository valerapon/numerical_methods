import numpy as np
import scipy.linalg as sl

def func(A, f, N):
    x = [0] * N
    for i in range(N):
        x[i] = f[i]
        for j in range(i):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return np.array(x)
 
N = int(input())
A = np.random.rand(N, N)
for i in range(N):
    for j in range(i, N):
        A[i][j] = A[j][i]
for i in range(N):
    Sum = 0
    for j in range(N):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
f = np.random.rand(N)
L = sl.cholesky(A, lower=True)
y = func(L, f, N)
L.transpose()
x = func(L, y, N)
#print(A)
#print(f)
print(x)
