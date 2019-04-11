import numpy as np

def runing(a, b, c, f, N):
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

def findIndex(array, value):
    L, R = 0, len(array) - 1
    while R - L > 1:
        m = (L + R) // 2
        if array[m] >= value:
            R = m
        else:
            L = m
    return L

def evaluateValueY(x, A, B, C, D, xValue):
    index = findIndex(x, xValue)
    tmp = xValue - x[index]
    return A[index] * (tmp ** 3) + B[index] * (tmp ** 2) + C[index] * tmp + D[index]

def generateSplineSmoothGrid(x, y):
    N = len(x) - 1 #N splines, N + 1 points
    h = (x[N] - x[0]) / N
    a = np.array([0] + [1] * (N - 1) + [0])
    b = np.array([1] + [4] * (N - 1) + [1])
    c = np.array([0] + [1] * (N - 1) + [0])
    f = np.zeros(N + 1)
    for i in range(1, N):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
    s = runing(a, b, c, f, N + 1)
    A = np.array([0] * (N + 1))
    B = np.array([0] * (N + 1))
    C = np.array([0] * (N + 1))
    D = np.array([0] * (N + 1))
    for i in range(N):
        D[i] = y[i]
        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        if i != N - 1:
            C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        else:
            C[i] = (y[i + 1] - y[i]) / h - (2 * B[i]) * h / 3
    return A, B, C, D

def generateSplineRandomGrid(x, y):
    N = len(x) - 1 #N splines, N + 1 points
    h = [0] * N
    for i in range(N):
        h[i] = x[i + 1] - x[i]
    a = np.array([0] * (N + 1))
    b = np.array([1] + [0] * (N - 1) + [1])
    c = np.array([0] * (N + 1))
    f = np.array([0] * (N + 1))
    for i in range(1, N):
        a[i] = h[i - 1]
        b[i] = 2 * (h[i - 1] + h[i])
        c[i] = h[i - 1]
        f[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
    s = runing(a, b, c, f, N + 1)
    A = np.array([0] * (N + 1))
    B = np.array([0] * (N + 1))
    C = np.array([0] * (N + 1))
    D = np.array([0] * (N + 1))
    for i in range(N):
        D[i] = y[i]
        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h[i])
        if i != N - 1:
            C[i] = (y[i + 1] - y[i]) / h[i] - (B[i + 1] + 2 * B[i]) * h[i] / 3
        else:
            C[i] = (y[i + 1] - y[i]) / h[i] - (2 * B[i]) * h[i] / 3
    return A, B, C, D
    return



inputX = open('train.dat', 'r')
inputY = open('train.ans', 'r')
inputFindX = open('test.dat', 'r')
outputY = open('test.ans', 'w')

N = int(inputX.readline())
inputY.readline()
M = int(inputFindX.readline())

x = np.array([float(i) for i in inputX.readline().split()])
y = np.array([float(i) for i in inputY.readline().split()])
newX = np.array([float(i) for i in inputFindX.readline().split()])

#A, B, C, D = generateSplineSmoothGrid(x, y)
A, B, C, D = generateSplineRandomGrid(x, y)

outputY.write(str(N) + '\n')
for i in range(M):
    valueY = evaluateValueY(x, A, B, C, D, newX[i]);
    outputY.write(str(valueY) + ' ')
inputX.close()
inputY.close()
inputFindX.close()
outputY.close()
