import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Rules 
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

matrix_size = 100 # Size of the game grid
matrix = np.random.randint(2, size=(matrix_size, matrix_size)) # Starting with a random seed
# matrix = np.zeros((matrix_size,matrix_size))
def glider(): #Makes a glider inside the field
    global matrix
    matrix[3, 4] = 1
    matrix[4, 5] = 1
    matrix[5, 3] = 1
    matrix[5, 4] = 1
    matrix[5, 5] = 1
# glider()
def sum_of_neigh(i, j):
    """Counts the sum of the coordinates neighbours"""
    value = 0
    global matrix
    for a in range(-1,2 ):
        for b in range(-1,2):
            if(a==0 and b==0):continue
            if (0 <= i+a < matrix_size and 0 <= j+b < matrix_size):
                if(matrix[i+a, j+b]):
                    value+=1
    return value

def naive_way():
    """Function for progressing the game - checks every single coordinate."""
    global matrix
    tobe_matrix = np.zeros((matrix_size,matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            tobe_matrix[i,j] =  sum_of_neigh(i,j)
    for i in range(matrix_size):
        for j in range(matrix_size):
            match tobe_matrix[i,j]:
                case 3:
                    matrix[i,j] = 1
                case 2: 
                    continue
                case _:
                    matrix[i,j] = 0
    return matrix

def get_neigh(i,j):
    """Returns the coordinates of neighbour cells. """
    global matrix
    x,y = [],[]
    for a in range(-1,2):
        for b in range(-1,2):
            if (a==0 and b ==0 ):continue
            if (0 <= i+a < matrix_size and 0 <= j+b < matrix_size):
                x.append(i+a)
                y.append(j+b)
    return x,y

def remove_duplicates(input_list):
    """Removes duplicates from a list of lists."""
    seen = set()
    result = []
    for sublist in input_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            result.append(list(sublist_tuple))
            seen.add(sublist_tuple)
    return result
def better_way():
    """A faster way of progressing the game - only checking the relevant coordinates."""
    tobe_matrix = np.zeros((matrix_size,matrix_size))
    all_list_to_check = []
    global matrix
    for i in range(matrix_size):
        for j in range(matrix_size):
            if(matrix[i,j]):
                x,y = get_neigh(i,j)
                if(x != []):
                    zipped_points = [list(point) for point in zip(x, y)]
                    for el in zipped_points:
                        all_list_to_check.append(el)
                all_list_to_check.append([i,j])
    all_list_to_check = remove_duplicates(all_list_to_check)
    for el in all_list_to_check:
        tobe_matrix[el[0],el[1]] = sum_of_neigh(el[0],el[1])
    for i in range(matrix_size):
        for j in range(matrix_size):
            match tobe_matrix[i,j]:
                case 3:
                    matrix[i,j] = 1
                case 2: 
                    continue
                case _:
                    matrix[i,j] = 0
    return matrix

def update_matrix():
    global matrix
    # matrix = naive_way()
    matrix = better_way()

def animate(i):
    plt.clf()
    plt.imshow(matrix, cmap='binary')
    plt.title(f'Frame {i}')
    update_matrix()

fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()