import numpy as np
import pygame

def sweep(a, b, c, f, N):
    alpha = np.array([0.0] * (N + 1))
    beta = np.array([0.0] * (N + 1))
    for i in range(N):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i] / d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x = np.array([0.0] * N)
    x[N - 1] = beta[N]
    for i in range(N - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x

def generateSpline(x, y):
    N = len(x) - 1 #N splines, N + 1 points
    h = (x[N] - x[0]) / N
    a = np.array([0] + [1] * (N - 1) + [0])
    b = np.array([1] + [4] * (N - 1) + [1])
    c = np.array([0] + [1] * (N - 1) + [0])
    f = np.zeros(N + 1)
    for i in range(1, N):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
    s = sweep(a, b, c, f, N + 1)
    A = np.array([0.0] * (N + 1))
    B = np.array([0.0] * (N + 1))
    C = np.array([0.0] * (N + 1))
    D = np.array([0.0] * (N + 1))
    for i in range(N):
        B[i] = s[i]
    for i in range(N):
        A[i] = (B[i + 1] - B[i]) / (3.0 * h)
        C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        D[i] = y[i]
    return A[:N], B[:N], C[:N], D[:N]

def draw(xFactors, yFactors, tStart, tEnd):
    for i in range(tStart, tEnd + 1):
        x = xFactors[0] * ((i - tStart) ** 3) + xFactors[1] * ((i - tStart) ** 2) + xFactors[2] * (i - tStart) + xFactors[3]
        y = yFactors[0] * ((i - tStart) ** 3) + yFactors[1] * ((i - tStart) ** 2) + yFactors[2] * (i - tStart) + yFactors[3]
        pygame.draw.line(sc, RED, (x, y), (x, y), 2)

x = []
y = []
t = []

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
 
pygame.init()
sc = pygame.display.set_mode((600, 600))
sc.fill(WHITE)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            x += [i.pos[0]]
            y += [i.pos[1]]
            t += [len(t) * 1000]
            if i.button == 1:
                sc.fill(WHITE)
                for j in range(len(x)):
                    pygame.draw.circle(sc, GREEN, (x[j], y[j]), 5)
                if len(x) > 1: 
                    xA, xB, xC, xD = generateSpline(t, x)
                    yA, yB, yC, yD = generateSpline(t, y)
                    for j in range(len(xA)):
                        draw([xA[j], xB[j], xC[j], xD[j]], [yA[j], yB[j], yC[j], yD[j]], t[j], t[j + 1])
                pygame.display.update() 
    pygame.time.delay(20)
