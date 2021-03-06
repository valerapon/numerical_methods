import numpy as np

def func(a, b, c, f, N):
    alpha = np.array([0.0] * (N + 1))
    beta = np.array([0.0] * (N + 1))
    for i in range(N):
        alpha[i + 1] = -c[i] / (a[i] * alpha[i] + b[i])
        beta[i + 1] = (f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + b[i])
    x = np.array([0.0] * N)
    x[N - 1] = beta[N]
    for i in range(N - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x
   
N = int(input())
A = np.ones((N,N)) * 0.0
a = np.random.sample(N)
b = np.random.sample(N)
c = np.random.sample(N)
f = np.random.sample(N)
a[0], c[N - 1] = 0, 0
for i in range(N):
    b[i] = abs(a[i]) + abs(b[i]) + abs(c[i]) + 1
    A[i][i] = b[i]
    if i > 0:
        A[i][i - 1] = a[i]
    if i < N - 1:
        A[i][i + 1] = c[i]
x = func(a, b, c, f, N)
#print(a)
#print(b)
#print(c)
#print(f)
print(x)
