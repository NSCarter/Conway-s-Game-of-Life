import random

grid = []
tempGrid = []

for row in range(10):
    grid.append([])
    for column in range(10):
        cell = random.randint(0,1)
        if cell == 0:
            grid[row].append(' ')
        else:
            grid[row].append('*')

for row in range(10):
    tempGrid.append([])
    for column in range(10):
        cell = random.randint(0,1)
        if cell == 0:
            tempGrid[row].append(' ')
        else:
            tempGrid[row].append('*')

def run(grid, tempGrid):
    del tempGrid[:]
##    for row in range(10):
##        tempGrid.append([])
##        for column in range(10):
##            cell = random.randint(0,1)
##            if cell == 0:
##                tempGrid[row].append(' ')
##            else:
##                tempGrid[row].append('*')
    for row in range(10):
        tempGrid.append([])
        for column in range(10):
            tempGrid[row].append(' ')
    for row in range(10):
        for column in range(10):
            count = 0
            if grid[row][column] == '*':
                if row+1 < 10:
                    if grid[row+1][column] == '*':
                        count += 1
                if row-1 > -1:
                    if grid[row-1][column] == '*':
                        count += 1
                if column+1 < 10:
                    if grid[row][column+1] == '*':
                        count += 1
                if column-1 > -1:
                    if grid[row][column-1] == '*':
                        count += 1
                if column+1 < 10 and row+1 < 10:
                    if grid[row+1][column+1] == '*':
                        count += 1
                if row-1 > -1 and column-1 > -1:
                    if grid[row-1][column-1] == '*':
                        count += 1
                if row+1 < 10 and column-1 > -1:
                    if grid[row+1][column-1] == '*':
                        count += 1
                if row-1 > -1 and column+1 < 10:
                    if grid[row-1][column+1] == '*':
                        count += 1

                if count == 2 or count == 3:
                    tempGrid[row][column] = '*'
                    print '1', count, '1', tempGrid[row][column]
                else:
                    tempGrid[row][column] = ' '
                    print '1', count, '0', tempGrid[row][column]

            elif grid[row][column] == ' ':
                if row+1 < 10:
                    if grid[row+1][column] == '*':
                        count += 1
                if row-1 > -1:
                    if grid[row-1][column] == '*':
                        count += 1
                if column+1 < 10:
                    if grid[row][column+1] == '*':
                        count += 1
                if column-1 > -1:
                    if grid[row][column-1] == '*':
                        count += 1
                if column+1 < 10 and row+1 < 10:
                    if grid[row+1][column+1] == '*':
                        count += 1
                if row-1 > -1 and column-1 > -1:
                    if grid[row-1][column-1] == '*':
                        count += 1
                if row+1 < 10 and column-1 > -1:
                    if grid[row+1][column-1] == '*':
                        count += 1
                if row-1 > -1 and column+1 < 10:
                    if grid[row-1][column+1] == '*':
                        count += 1

                if count == 3:
                    tempGrid[row][column] = '*'
                    print '0', count, '1', tempGrid[row][column]
                else:
                    tempGrid[row][column] = ' '
                    print '0', count, '0', tempGrid[row][column]

    del grid [:]
    grid = tempGrid
    printGrid(grid)

def printGrid(grid):
    for row in grid:
        print ''.join(row)
    print 'Done'

printGrid(grid)

run(grid, tempGrid)
