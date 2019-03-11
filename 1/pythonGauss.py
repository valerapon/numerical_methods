import numpy as np

N = int(input())
A = np.random.rand(N, N)
for i in range(N):
    Sum = 0
    for j in range(N):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
f = np.random.rand(N)
x = np.linalg.solve(A, f)
print(x)
