f1 = open('test.dat', 'r')
f2 = open('test.ans', 'r')
f3 = open('plot.txt', 'w')
f1.readline()
x = [float(i) for i in f1.readline().split()]
f2.readline()
y = [float(i) for i in f2.readline().split()]
for i in range(len(x)):
    f3.write(str(x[i]) + ' ' + str(y[i]) + '\n')
f1.close()
f2.close()
f3.close()
