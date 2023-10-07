import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matrix_size = 100
# matrix = np.random.randint(2, size=(matrix_size, matrix_size))
matrix = np.zeros((matrix_size,matrix_size))
matrix[matrix_size//2,matrix_size//2] = 1 #Ant position
x,y = matrix_size//2,matrix_size//2
direction = 0

def move_Ant(direction):
    global x, y
    direction %= 4
    if direction == 1:
        x += 1
    elif direction == 3:
        x -= 1
    elif direction == 2:
        y -= 1
    elif direction == 0:
        y += 1
    return x, y

def step_color(i,j):
    global direction
    if(matrix[i,j]==0):
        direction +=1
        x, y = move_Ant(direction)
    elif(matrix[i,j]==1):
        direction +=3
        x, y = move_Ant(direction)
    matrix[i,j] = not matrix[i,j]
    return matrix, x, y
def update_Pos():
    global x, y
    global matrix
    matrix, x, y = step_color(x, y)
    return matrix

def update_matrix():
    global matrix
    matrix = update_Pos()

def animate(i):
    plt.clf()
    update_matrix()
    plt.imshow(matrix, cmap='binary')
    plt.title(f'Frame {i}')

fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
