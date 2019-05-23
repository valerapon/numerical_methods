import numpy as np

#O(m * n ^ 2)
def Lagrange(x, y, valueX):
    valueY = 0.0
    N = len(x)
    for i in range(N):
        if valueX == x[i]:
            return y[i]
    for i in range(N):
        tmp = 1.0
        for j in range(N):
            if i != j:
                tmp = tmp * (valueX - x[j]) / (x[i] - x[j])
        valueY = valueY + y[i] * tmp     
    return valueY

#O(n ^ 2 + m * n)
#См. прикрепленное фото
def fastLagrange(x, y, valueX):
    N = len(x)
    for i in range(N):
        if (valueX == x[i]):
            return y[i]
    A = [0] * N
    for i in range(N):
        tmp = 1.0
        for j in range(N):
            if i != j:
                tmp = tmp * (x[i] - x[j])
        A[i] = y[i] / tmp
    alpha = 1.0
    for i in range(N):
        alpha = alpha * (valueX - x[i])
    beta = 0.0
    for i in range(N):
        beta = beta + A[i] / (valueX - x[i])
    return alpha * beta

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


outputY.write(str(N) + '\n')
'''
for i in range(M):
    valueY = Lagrange(x, y, newX[i])
    outputY.write(str(valueY) + ' ')
'''
for i in range(M):
    valueY = fastLagrange(x, y, newX[i])
    outputY.write(str(valueY) + ' ')
inputX.close()
inputY.close()
inputFindX.close()
outputY.close()

    

