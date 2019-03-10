import numpy as np
import scipy.linalg as alg
import matplotlib.pyplot as plt

def func1(A, f, N):
    for k in range(N):
        for i in range(k + 1, N):
            A[k][i] = A[k][i] / A[k][k]
        f[k] = f[k] / A[k][k]
        A[k][k] = 1
        for i in range(k + 1, N):
            for j in range(k + 1, N):
                A[i][j] = A[i][j] - A[k][j] * A[i][k]
            f[i] = f[i] - f[k] * A[i][k]
            A[i][k] = 0
    return A, f

def func2(A, f, N):
    x = [0] * N
    for i in range(N - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, N):
            x[i] = x[i] - A[i][j] * x[j]
    return np.array(x)

N = int(input())
A = np.random.rand(N, N)
for i in range(N):
    Sum = 0
    for j in range(N):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
f = np.random.rand(N)
#x = np.linalg.solve(A, f)
#print(x)
A, f = func1(A, f, N)
x = func2(A, f, N)
print(x)
