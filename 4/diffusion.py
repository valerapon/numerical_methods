import numpy as np
import pygame

def f():
    newMatrix = np.ones((N,N)) * 0.0
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                newMatrix[i][j] = 0.0
            else:
                newMatrix[i][j] = matrix[i][j] + mu * tau / (h ** 2) * \
                                  (matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1] - 4 * matrix[i][j])
                if (newMatrix[i][j] < 1):
                    newMatrix[i][j] = 0.0
    return newMatrix

def draw():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 0.0 and matrix[i][j] < 1024.0:
                pygame.draw.line(window, (255, 255 - int(matrix[i][j]) % 256, 255 - int(matrix[i][j]) % 256), (i, j), (i, j), 1)
            elif matrix[i][j] > 1024.0:
                pygame.draw.line(window, (255, 0, 0), (i, j), (i, j), 1)
            else:
                pygame.draw.line(window, (255, 255, 255), (i, j), (i, j), 1)

mu = 0.25
tau = 1.0
h = 1.0

N = 100
matrix = np.ones((N, N)) * 0.0

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
 
pygame.init()
window = pygame.display.set_mode((N, N))
window.fill(WHITE)
pygame.display.update()

x, y, t = [], [], []

while True:
    matrix = f()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        matrix[pos[0]][pos[1]] = 255.0
    draw()
    pygame.display.update()
