import numpy as np
import scipy.linalg as sl

N = int(input())
a = np.random.rand(N)
b = np.random.sample(N)
c = np.random.sample(N)
f = np.random.sample(N)
a[0], c[N - 1] = 0, 0
for i in range(N):
    b[i] = abs(a[i]) + abs(b[i]) + abs(c[i]) + 1
A = np.random.rand(3, N)
for i in range(N):
    A[0][i] = a[i]
    A[1][i] = b[i]
    A[2][i] = c[i]
x = sl.solve_banded((1, 1), A, f)
print(x)
