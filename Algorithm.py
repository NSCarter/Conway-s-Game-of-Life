import random

grid = []
tempGrid = []

#Create a random patern in a grid
for row in range(10):
    grid.append([])
    for column in range(10):
        cell = random.randint(0,1)
        if cell == 0:
            grid[row].append(' ')
        else:
            grid[row].append('*')
print grid

def run(grid, tempGrid):
    for i in range(2):
##        print grid
        #Deleted the contents of the temporary grid
        del tempGrid[:]
        #Create a blank temporary grid
        for row in range(10):
            tempGrid.append([])
            for column in range(10):
                tempGrid[row].append(' ')
        #Go through each cell in the grid
        for row in range(10):
            for column in range(10):
                count = 0
                #If the cell is alive
                if grid[row][column] == '*':
                    #Check the cells surrounding it
                    if row+1 < 10:
                        if grid[row+1][column] == '*':
                            #Add 1 to the count if a cell surrounding it is alive
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

                    #If the cell is surrounded by 2 or 3 live cells
                    if count == 2 or count == 3:
                        #The cell remains alive
                        tempGrid[row][column] = '*'
                    else:
                        #Otherwise the cell dies
                        tempGrid[row][column] = ' '

                #If the cell is dead
                elif grid[row][column] == ' ':
                    #Check the cells surrounding it
                    if row+1 < 10:
                        if grid[row+1][column] == '*':
                            #Add 1 to the count is a cell surrounding it is alive
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

                    #If the cell is surrounded by 3 live cells
                    if count == 3:
                        #The cell becomes alive
                        tempGrid[row][column] = '*'
                    else:
                        #Otherwise the cell remains dead
                        tempGrid[row][column] = ' '

        #Delete the contents of the grid
        del grid [:]
        #Add the contents of the temporary grid to the main grid
        grid = tempGrid
##        print grid
        #Print the grid
        printGrid(grid)

def printGrid(grid):
    for row in grid:
        #Remove the brackets, spaces and apostrophes
        print ''.join(row)
    print 'Done'

printGrid(grid)

run(grid,tempGrid)

##for i in range(2):
##    run(grid, tempGrid)
