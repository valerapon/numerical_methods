import numpy as np
import scipy.linalg as alg
import matplotlib.pyplot as plt

def findIndex(array, value):
    L, R = 0, len(array) - 1
    while R - L > 1:
        m = (L + R) // 2
        if array[m] >= value:
            R = m
        else:
            L = m
    return L

def segmentBuild(x, y):
    #y = k * x + b
    N = len(x)
    k, b = [0.0] * (N - 1), [0.0] * (N - 1)
    for i in range(N - 1):
        tmp = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        k[i] = tmp
        b[i] = y[i] - x[i] * tmp
    return k, b

inputX = open('train.dat', 'r')
inputY = open('train.ans', 'r')
inputFindX = open('test.dat', 'r')
outputY = open('test.ans', 'w')

N = int(inputX.readline())
inputY.readline()
M = int(inputFindX.readline())

x = [float(i) for i in inputX.readline().split()]
y = [float(i) for i in inputY.readline().split()]
newX = [float(i) for i in inputFindX.readline().split()]

k, b = segmentBuild(x, y)
print('Input X:')
print(*x)
print('Input Y:')
print(*y)
print('Find X:')
print(*newX)
print('Output:')
outputY.write(str(N) + '\n')
for i in range(M):
    index = findIndex(x, newX[i])
    valueY = k[index] * newX[i] + b[index]
    outputY.write(str(valueY) + ' ')
    print(valueY, end=' ')
    
inputX.close()
inputY.close()
inputFindX.close()
outputY.close()

    

