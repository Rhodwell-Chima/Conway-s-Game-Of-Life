"""Simulation of Conway's Game of Life."""

import os
import time
import numpy
from range import Range



def make_grid(rows, cols, live_cells):
    """Construct a rows x cols grid with the given live cells.

    The grid is represented as a (rows+2) x (cols+2) numpy array of
    8-bit integers, representing cell locations from (-1, -1) to
    (row+1, col+1). Live cells contain a 1, while dead cells contain a
    0.

    >>> make_grid(3, 4, [])
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    >>> make_grid(3, 4, [(0, 1), (1, 2), (2, 2), (2, 3)])
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    """
    # your code here
    grid = numpy.zeros((rows + 2, cols + 2), dtype=numpy.int8)
    for r, c in live_cells:
        grid[r + 1, c + 1] = 1
    return grid


def print_grid(grid, interactive=False):
    """Print a grid.

    If interactive is true, then inserts a slight delay between
    printing each timestep.
    """
    if interactive:
        time.sleep(0.05)
        os.system('clear')
    rows, cols = grid.shape
    print('-' * cols)
    for i in Range(1, rows - 1):
        print('|', end='')
        for j in Range(1, cols - 1):
            print('*' if grid[i, j] else ' ', end='')
        print('|')
    print('-' * cols)
    print()


def timestep(current_grid, next_grid):
    """Simulate a single timestep of the Game of Life.

    current_grid is the input grid, next_grid is the output.

    >>> grid1 = make_grid(3, 4, [(0, 1), (1, 2), (2, 2), (2, 3)])
    >>> grid2 = make_grid(3, 4, [])
    >>> timestep(grid1, grid2)
    >>> grid1
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    >>> grid2
    array([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]], dtype=int8)
    """
    interior_rows = Range(1, current_grid.shape[0] - 1)
    interior_cols = Range(1, current_grid.shape[1] - 1)
    # your code here
    for i in interior_rows:
        for j in interior_cols:
            neighbors = numpy.sum(current_grid[i-1:i+2, j-1:j+2])-current_grid[i, j]
            if current_grid[i, j] == 1:
                next_grid[i, j] = 1 if neighbors in [2, 3] else 0
            else:
                next_grid[i, j] = 1 if neighbors == 3 else 0



def simulate(rows, cols, steps, live_cells, interactive=False):
    """Simulate full Game of Life.

    Simulates on a rows x cols grid for the given number of steps, with
    the given sequence of initial live cells.
    """
    # your code here
    grid1 = make_grid(rows, cols, live_cells)
    grid2 = make_grid(rows, cols, [])

    for _ in range(steps):
        print_grid(grid1, interactive)
        timestep(grid1, grid2)
        grid1, grid2 = grid2, grid1

print("Running simulation with 5 rows, 5 cols, 10 steps, and live cells at (1,2), (2,2), (3,2)")
simulate(5, 5, 10, [(1, 2), (2, 2), (3, 2),(0, 3), (3,3)], interactive=True)
print("Simulation complete.")

