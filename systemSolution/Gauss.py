import numpy as np

def backward(A, f, N):
    x = [0] * N
    for i in range(N - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, N):
            x[i] = x[i] - A[i][j] * x[j]
    return np.array(x)

def forward(A, f, N):
    for k in range(N):
        tmp = A[k][k]
        A[k] = A[k] / tmp
        f[k] = f[k] / tmp
        for i in range(k + 1, N):
            A[i] = A[i] - A[k] * A[i][k]
            f[i] = f[i] - f[k] * A[i][k]
            A[i][k] = 0
    return A, f

N = int(input())
A = np.random.rand(N, N)
for i in range(N):
    Sum = 0
    for j in range(N):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
f = np.random.rand(N)
A, f = forward(A, f, N)
x = backward(A, f, N)
print(x)
