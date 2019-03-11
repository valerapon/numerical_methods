import subprocess
import time
import matplotlib.pyplot as plt
#
path = input()
pathFast = input()
jump = int(input())
start = 0.0
finish = 0.0
parametr = 0
X = []
Y = []
while finish - start <= 1:
    parametr = parametr + jump
    cmd = 'echo ' + str(parametr) + ' | ' + 'python3 ' + path
    start = time.time()
    subprocess.call(cmd, shell=True)
    finish = time.time()
    X = X + [parametr]
    Y = Y + [int(1000.0 * (finish - start))]
oldParametr = parametr
plt.scatter(X, Y, s=10, c='red')
plt.plot(X, Y)
#
path = pathFast
start = 0.0
finish = 0.0
parametr = 0
X = []
Y = []
while finish - start <= 1 and parametr <= oldParametr:
    parametr = parametr + jump
    cmd = 'echo ' + str(parametr) + ' | ' + 'python3 ' + path
    start = time.time()
    subprocess.call(cmd, shell=True)
    finish = time.time()
    X = X + [parametr]
    Y = Y + [int(1000.0 * (finish - start))]
plt.scatter(X, Y, s=10, c='green')
plt.plot(X, Y)
plt.show()

