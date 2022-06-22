import numpy as np

grid = [
    [0, 8, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [6, 0, 0, 9, 2, 0, 3, 0, 0],
    [1, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 5, 0, 0],
    [0, 0, 7, 1, 5, 0, 0, 0, 3],
    [0, 0, 6, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [9, 0, 0, 3, 1, 0, 2, 0, 0],
    
]


def possible(row, col, num):
    global grid
    for i in range(0, 9):
        if grid[row][i] == num:
            return False

    for i in range(0, 9):
        if grid[i][col] == num:
            return False

    x0 = (col // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == num:
                return False
    return True


def solve():
    global grid
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if possible(row, col, num):
                        grid[row][col] = num
                        solve()
                        grid[row][col] = 0
                return
    print(np.matrix(grid))
    input("More")


solve()
