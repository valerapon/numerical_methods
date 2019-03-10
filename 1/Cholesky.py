import numpy as np
import scipy.linalg as alg
import matplotlib.pyplot as plt

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
L = np.ones((N, N)) * 0.0
for i in range(N):
    for j in range(i + 1):
        if i == j:
            Sum = 0
            for k in range(i):
                Sum = Sum + L[i][k] ** 2
            L[i][i] = (A[i][i] - Sum) ** 0.5
        else:
            Sum = 0
            for k in range(j):
                Sum = Sum + L[i][k] * L[j][k]
            L[i][j] = (A[i][j] - Sum) / L[j][j]
y = func(L, f, N)
L.transpose()
x = func(L, y, N)
print(A)
print(f)
print(x)
