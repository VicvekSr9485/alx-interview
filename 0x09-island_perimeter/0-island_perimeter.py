#!/usr/bin/python3
""" Island Perimeter Module """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check bottom neighbor
                if i == rows - 1 and grid[i + 1][j] == 0:
                    perimeter += 1
                # check left neighbor
                if j == 0 or grid[i][j + 1] == 0:
                    perimeter += 1
                # check right neighbor
                if j == cols - 1 and grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
