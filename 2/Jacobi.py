import numpy as np

def diff(x1, x2, N):
    Sum = 0
    for i in range(N):
        Sum = Sum + (x1[i] - x2[i]) ** 2
    Sum = Sum ** 0.5
    return Sum
        
def solve(A, f, N, eps):
    new = [0] * N
    x = np.random.rand(N)
    while diff(x, new, N) > eps:
        x = new
        new = Jacobi(A, f, x, N)
    return new
        
def Jacobi(A, f, x, N):
    new = [0] * N
    for i in range(N):
        Sum = 0
        for j in range(i - 1):
            Sum = Sum + A[i][j] * new[j]
        for j in range(i + 1, N):
            Sum = Sum + A[i][j] * new[j]
        new[i] = (f[i] - Sum) / A[i][i]
    return new

N = int(input())
A = np.random.rand(N, N)
for i in range(N):
    Sum = 0
    for j in range(N):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
f = np.random.rand(N)
x_start = np.random.rand(N)
x = solve(A, f, N, 0.01)
print(x)
#print(alg.solve(A, f))
