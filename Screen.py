'''
~~~~~To Do~~~~~
Help - rules
Help - How to use
Grid lines maybe
More patterns
'''

#Import the pygame and time modules
import pygame
import time

#Initialise pygame
pygame.init()

#Size of the screen
displayWidth = 800
displayHeight = 600

#Colours
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
red = (255,0,0)

#Fonts used for displaying text
font = pygame.font.Font('freesansbold.ttf', 16)
speedFont = pygame.font.Font('freesansbold.ttf', 32)
sizeFont = pygame.font.Font('freesansbold.ttf', 32)
#Start value for speed, size of the grid and the square size
speedValue = 9
sizeOfGridValue = 10
#The amount of the screen used for the grid
gridWidth = 600
#Grids used for running through the algorithm
grid = []
tempGrid = []
startGrid = []
#The number of generations is initially set to 0
generations = 0
stable = False

#Set the size of the screen, the name of the screen and define the clock
screenDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Conway\'s game of life')
clock = pygame.time.Clock()

#Create all the squares in the grid
class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        super(Square, self).__init__()
        #Width of the square
        self.width = width
        #Height of the square
        self.height = height
        #Overall size of the square
        self.image = pygame.Surface((width,height))
        #Colour of the square
        self.colour = colour
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        #X and Y coordinates of where the square is positioned
        self.rect.x = x
        self.rect.y = y
        self.animate = False
    def update(self):
        #Add the square to the screen
        self.image = pygame.Surface((self.height/2,self.width/2))

#List of all the squares in the grid
squareList = []

def menuBackground():
    pygame.draw.rect(screenDisplay, grey, (0,0,200,600))
    pygame.draw.line(screenDisplay, black,(200,0),(200,600),3)
    pygame.draw.line(screenDisplay, black,(0,90),(200,90),3)
    pygame.draw.line(screenDisplay, black,(0,260),(200,260),3)

#The boxes in the menu
def menuBoxes():
    #Name of pattern
    nameOfPattern = pygame.draw.rect(screenDisplay, white,(50,20,100,50))
    pygame.draw.rect(screenDisplay, black,(50,20,100,50),3)
    #Speed
    pygame.draw.rect(screenDisplay, white,(25,110,75,25))
    pygame.draw.rect(screenDisplay, black,(25,110,75,25),3)
    speed = pygame.draw.rect(screenDisplay, white,(125,110,25,25))
    pygame.draw.rect(screenDisplay, black,(125,110,25,25),3)
    #Size of grid
    pygame.draw.rect(screenDisplay, white,(25,160,150,25))
    pygame.draw.rect(screenDisplay, black,(25,160,150,25),3)
    sizeOfGrid = pygame.draw.rect(screenDisplay, white,(62,210,90,25))
    pygame.draw.rect(screenDisplay, black,(62,210,90,25),3)
    #Start
    start = pygame.draw.rect(screenDisplay, white,(62,285,75,25))
    pygame.draw.rect(screenDisplay, black,(62,285,75,25),3)
    #Stop
    stop = pygame.draw.rect(screenDisplay, white,(62,335,75,25))
    pygame.draw.rect(screenDisplay, black,(62,335,75,25),3)
    #Step
    step = pygame.draw.rect(screenDisplay, white,(62,385,75,25))
    pygame.draw.rect(screenDisplay, black,(62,385,75,25),3)
    #Clear
    clear = pygame.draw.rect(screenDisplay, white,(62,435,75,25))
    pygame.draw.rect(screenDisplay, black,(62,435,75,25),3)
    return nameOfPattern, speed, sizeOfGrid, start, stop, step, clear

#The text in the menu boxes
def menuText():
    #Name of pattern
    text = font.render("Select a", 1, black)
    textpos = (65,25)
    screenDisplay.blit(text, textpos)
    text = font.render("pattern", 1, (black))
    textpos = (70,45)
    screenDisplay.blit(text, textpos)
    #Speed
    text = font.render("Speed:", 1, (black))
    textpos = (32,115)
    screenDisplay.blit(text, textpos)
    text = font.render(str(speedValue), 1, (black))
    textpos = (132,115)
    screenDisplay.blit(text, textpos)
    #Size of grid
    text = font.render("Size of the grid:", 1, (black))
    textpos = (35,165)
    screenDisplay.blit(text, textpos)
    text = font.render("%d x %d" % tuple([sizeOfGridValue]*2), 1, (black))
    textpos = (70,215)
    screenDisplay.blit(text, textpos)
    #Start
    text = font.render("Start", 1, (black))
    textpos = (77,290)
    screenDisplay.blit(text, textpos)
    #Stop
    text = font.render("Stop", 1, (black))
    textpos = (80,340)
    screenDisplay.blit(text, textpos)
    #Step
    text = font.render("Step", 1, (black))
    textpos = (80,390)
    screenDisplay.blit(text, textpos)
    #Clear
    text = font.render("Clear", 1, (black))
    textpos = (77,440)
    screenDisplay.blit(text, textpos)
    #Generations
    text = font.render("Generations:", 1, (black))
    textpos = (5,490)
    screenDisplay.blit(text, textpos)
    text = font.render(str(generations), 1, (black))
    textpos = (125,490)
    screenDisplay.blit(text, textpos)
    #Stable
    text = font.render('Stable:', 1, (black))
    textpos = (5,515)
    screenDisplay.blit(text, textpos)
    #Check if the pattern is stable
    global stableGen
    #If it isn't display no
    if stable == False:
        text = font.render('No', 1, (black))
        textpos = (75,515)
        screenDisplay.blit(text, textpos)
    #Otherwise display yes
    else:
        pygame.draw.rect(screenDisplay, grey,(75,515,74,25))
        text = font.render('Yes', 1, (black))
        textpos = (75,515)
        screenDisplay.blit(text, textpos)

#Function deciding which button has been clicked and what to do next
def button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos):
    global squareList, speedValue, sizeOfGridValue
    #If the nameOfPattern button was clicked
    if nameOfPattern.collidepoint(pos):
        chosen = False
        #While the user hasn't chosen a pattern
        while chosen == False:
            #Display the pattern menu
            chosen = patternMenu()
    #If the speed button was clicked
    elif speed.collidepoint(pos):
        chosen = False
        #While the user hasn't chosen a speed
        while chosen == False:
            #Display the speed menu
            chosen, speedValue = speedMenu(speedValue, pos)
    #If the user clicked the size of grid button
    elif sizeOfGrid.collidepoint(pos):
        chosen = False
        #While the user hasn't chosen a size
        while chosen == False:
            #Display the size of grid menu
            chosen, sizeOfGridValue, squareList = sizeOfGridMenu(sizeOfGridValue, pos)
        #Run the grid setup again the the new size of grid value to change the number
        #of squares on the grid
        gridSetup(sizeOfGridValue, squareList)
    #If the user clicked the start button
    elif start.collidepoint(pos):
        stopped = False
        #Check if  the grid is empty
        empty = emptyValidate()
        #If the grid isn't empty
        if empty == False:
            #While the user hasn't clicked the stop button
            while not stopped:
                    #Run the pattern on the grid through the rules
                    stopped = startRun(grid, stop, sizeOfGridValue)
        #If the grid is empty
        else:
            closed = False
            while not closed:
                #Display an error message
                closed = emptyMessage()
    #If the user clicked the step button
    elif step.collidepoint(pos):
        stopped = False
        #Check if the grid is empty
        empty = emptyValidate()
        #If the grid isn't empty
        if empty == False:
            #Step through the pattern once
            stepRun(grid, sizeOfGridValue)
        #If the grid is empty
        else:
            closed = False
            while not closed:
                #Display an error message
                closed = emptyMessage()
    #If the user clicked the clear button
    elif clear.collidepoint(pos):
        #Clear the grid
        clearGrid()
    #Return the speed value, the size of grid value and the squarelist
    return speedValue, sizeOfGridValue, squareList

#The menu displayed when the clicks the speed button
def speedMenu(speedValue, pos):
    time.sleep(0.1)
    end = False

    #While the user hasn't closed the program
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            #Find the position of the mouse
            pos = pygame.mouse.get_pos()
            #If the left mouse button was clicked
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #If the user clicked the 1 button
                if speed1.collidepoint(pos):
                    #Change the speed value to one
                    speedValue = 1
                    #Set chosen to true
                    chosen = True
                    #Return chosen and the new speed value
                    return chosen, speedValue
                elif speed2.collidepoint(pos):
                    speedValue = 2
                    chosen = True
                    return chosen, speedValue
                elif speed3.collidepoint(pos):
                    speedValue = 3
                    chosen = True
                    return chosen, speedValue
                elif speed4.collidepoint(pos):
                    speedValue = 4
                    chosen = True
                    return chosen, speedValue
                elif speed5.collidepoint(pos):
                    speedValue = 5
                    chosen = True
                    return chosen, speedValue
                elif speed6.collidepoint(pos):
                    speedValue = 6
                    chosen = True
                    return chosen, speedValue
                elif speed7.collidepoint(pos):
                    speedValue = 7
                    chosen = True
                    return chosen, speedValue
                elif speed8.collidepoint(pos):
                    speedValue = 8
                    chosen = True
                    return chosen, speedValue
                elif speed9.collidepoint(pos):
                    speedValue = 9
                    chosen = True
                    return chosen, speedValue

        #Boxes
        pygame.draw.rect(screenDisplay, white,(405,205,190,190))
        pygame.draw.rect(screenDisplay, black,(405,205,190,190),3)
        speed1 = pygame.draw.rect(screenDisplay, white,(415,215,50,50))
        pygame.draw.rect(screenDisplay, black,(415,215,50,50),3)
        speed2 = pygame.draw.rect(screenDisplay, white,(475,215,50,50))
        pygame.draw.rect(screenDisplay, black,(475,215,50,50),3)
        speed3 = pygame.draw.rect(screenDisplay, white,(535,215,50,50))
        pygame.draw.rect(screenDisplay, black,(535,215,50,50),3)
        speed4 = pygame.draw.rect(screenDisplay, white,(415,275,50,50))
        pygame.draw.rect(screenDisplay, black,(415,275,50,50),3)
        speed5 = pygame.draw.rect(screenDisplay, white,(475,275,50,50))
        pygame.draw.rect(screenDisplay, black,(475,275,50,50),3)
        speed6 = pygame.draw.rect(screenDisplay, white,(535,275,50,50))
        pygame.draw.rect(screenDisplay, black,(535,275,50,50),3)
        speed7 = pygame.draw.rect(screenDisplay, white,(415,335,50,50))
        pygame.draw.rect(screenDisplay, black,(415,335,50,50),3)
        speed8 = pygame.draw.rect(screenDisplay, white,(475,335,50,50))
        pygame.draw.rect(screenDisplay, black,(475,335,50,50),3)
        speed9 = pygame.draw.rect(screenDisplay, white,(535,335,50,50))
        pygame.draw.rect(screenDisplay, black,(535,335,50,50),3)

        #Text
        text = speedFont.render("1", 1, (black))
        textpos = (430,225)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("2", 1, (black))
        textpos = (490,225)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("3", 1, (black))
        textpos = (550,225)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("4", 1, (black))
        textpos = (430,285)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("5", 1, (black))
        textpos = (490,285)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("6", 1, (black))
        textpos = (550,285)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("7", 1, (black))
        textpos = (430,345)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("8", 1, (black))
        textpos = (490,345)
        screenDisplay.blit(text, textpos)
        text = speedFont.render("9", 1, (black))
        textpos = (550,345)
        screenDisplay.blit(text, textpos)

        #Update the screen
        pygame.display.update()
        clock.tick(11)

#Function to setup the grid to create the white squares
def gridSetup(sizeOfGridValue, squareList):
    xPos = 0
    yPos = 0
    row = 0
    column = 0
    for i in range (sizeOfGridValue):
        #Create an empty array
        squareList.append([])
        for j in range (sizeOfGridValue):
            #If you have reached the end of the row
            if column * (gridWidth/sizeOfGridValue) > gridWidth - (gridWidth/sizeOfGridValue):
                #Move onto the next row
                row += 1
                #And start again at the first column
                column = 0
            #Find the x position of the square
            xPos = 202 + (column * (gridWidth/sizeOfGridValue))
            #Find the y position of the square
            yPos = row * (displayHeight/sizeOfGridValue)
            #Move onto the next column
            column += 1
            #Add a new square to the list of squares at the postion we have just calculated
            squareList[i].append(Square(xPos,yPos,gridWidth/sizeOfGridValue,displayHeight/sizeOfGridValue,white))
    return squareList

#Function that changes the colour of a square when a user clicks on it
def squareChange(pos):
    #Find the square the user clicked on
    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            if squareList[row][col].rect.collidepoint(pos):
                squareList[row][col].animate = True
                #If the square white
                if squareList[row][col].colour == white:
                    #Turn it red
                    squareList[row][col].colour = red
                    squareList[row][col].image.fill(red)
                #If the square is red
                elif squareList[row][col].colour == red:
                    #Turn it white
                    squareList[row][col].colour = white
                    squareList[row][col].image.fill(white)

#Function that runs the pattern on the grid through the game of life rules
def startRun(grid, stop, sizeOfGridValue):
    end = False

    #While the user hasn't closed the program
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #If the user clicked the stop button
                if stop.collidepoint(pos):
                    #Stop running through the pattern
                    stopped = True
                    return stopped

        #Clear the grid
        grid = []

        #Create an empty array
        for i in range(sizeOfGridValue):
            grid.append([])

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                #For each cell in the square list that is red
                if squareList[row][col].colour == red:
                    #Add an asterix at the corresponding position in the grid
                    grid[row].append('*')
                else:
                    #Otherwise add a space at the corresponding position in the grid
                    grid[row].append(' ')

        startGrid = grid

        #Clear the temporary grid
        tempGrid = []

        #Turn the temporary grid into a blank two dimensional array
        for row in range(sizeOfGridValue):
            tempGrid.append([])
            for column in range(sizeOfGridValue):
                tempGrid[row].append(' ')

        #Go through each cell in the grid
        for row in range(sizeOfGridValue):
            for column in range(sizeOfGridValue):
                count = 0
                #If the cell is alive
                if grid[row][column] == '*':
                    #Check the cells surrounding it
                    if row+1 < sizeOfGridValue:
                        if grid[row+1][column] == '*':
                            #Add one to the count if the cell is alive
                            count += 1
                    if row-1 > -1:
                        if grid[row-1][column] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue:
                        if grid[row][column+1] == '*':
                            count += 1
                    if column-1 > -1:
                        if grid[row][column-1] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue and row+1 < sizeOfGridValue:
                        if grid[row+1][column+1] == '*':
                            count += 1
                    if row-1 > -1 and column-1 > -1:
                        if grid[row-1][column-1] == '*':
                           count += 1
                    if row+1 < sizeOfGridValue and column-1 > -1:
                        if grid[row+1][column-1] == '*':
                            count += 1
                    if row-1 > -1 and column+1 < sizeOfGridValue:
                        if grid[row-1][column+1] == '*':
                            count += 1

                    #If the cell is surrounded by 2 or 3 live cells
                    if count == 2 or count == 3:
                        #It remains alive
                        tempGrid[row][column] = '*'
                    else:
                        #Otherwise it dies
                        tempGrid[row][column] = ' '

                #If the cell is dead
                elif grid[row][column] == ' ':
                    #Check the cells surrounding it
                    if row+1 < sizeOfGridValue:
                        if grid[row+1][column] == '*':
                            #If the cell is alive add one to the count
                            count += 1
                    if row-1 > -1:
                        if grid[row-1][column] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue:
                        if grid[row][column+1] == '*':
                            count += 1
                    if column-1 > -1:
                        if grid[row][column-1] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue and row+1 < sizeOfGridValue:
                        if grid[row+1][column+1] == '*':
                            count += 1
                    if row-1 > -1 and column-1 > -1:
                        if grid[row-1][column-1] == '*':
                            count += 1
                    if row+1 < sizeOfGridValue and column-1 > -1:
                        if grid[row+1][column-1] == '*':
                            count += 1
                    if row-1 > -1 and column+1 < sizeOfGridValue:
                        if grid[row-1][column+1] == '*':
                            count += 1

                    #If the cell is surrounded by 3 live cells
                    if count == 3:
                        #The cell becomes alive
                        tempGrid[row][column] = '*'
                    else:
                        #Otherwise the cell dies
                        tempGrid[row][column] = ' '

        #Empty the grid
        grid = []

        #Make the grid equal to the temporary  grid
        grid = tempGrid

        #Run through each square in the squareList
        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                #If the cell in the grid at the same position of the square is
                #alive
                if grid[row][col] == '*':
                    #The square becomes red
                    squareList[row][col].colour = red
                    squareList[row][col].image.fill(red)
                #If the cell is dead
                else:
                    #The square becomes white
                    squareList[row][col].colour = white
                    squareList[row][col].image.fill(white)

        #For each square in the squareList
        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                #Display it on the screen
                screenDisplay.blit(squareList[row][col].image, squareList[row][col].rect)

        global generations

        #Add 1 to the generations
        generations += 1

        #Display the number of generations onto the screen
        pygame.draw.rect(screenDisplay, grey,(125,490,74,25))
        text = font.render(str(generations), 1, (black))
        textpos = (125,490)
        screenDisplay.blit(text, textpos)

        global stable
        #If the pattern is not already stable
        if stable == False:
            #Check if the pattern on the grid is the same as it was before
            #running through the algorithm
            if grid == startGrid:
                stable = True
                pygame.draw.rect(screenDisplay, grey,(75,515,74,25))
                text = font.render('Yes', 1, (black))
                textpos = (75,515)
                screenDisplay.blit(text, textpos)
                text = font.render(str(generations), 1, (black))
                textpos = (110,515)
                screenDisplay.blit(text, textpos)
##            menuText()

        time.sleep(9-speedValue)

        pygame.display.update()
        clock.tick(11)

def clearGrid():
    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            squareList[row][col].colour = white
            squareList[row][col].image.fill(white)
    global generations, stable
    generations = 0
    stable = False


def sizeOfGridMenu(sizeOfGridValue, pos):
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if size5.collidepoint(pos):
                    sizeOfGridValue = 5
                    chosen  = True
                    squareList = []
                    return chosen, sizeOfGridValue, squareList
                elif size10.collidepoint(pos):
                    sizeOfGridValue = 10
                    chosen  = True
                    squareList = []
                    return chosen, sizeOfGridValue, squareList
                elif size25.collidepoint(pos):
                    sizeOfGridValue = 25
                    chosen  = True
                    squareList = []
                    return chosen, sizeOfGridValue, squareList
                elif size50.collidepoint(pos):
                    sizeOfGridValue = 50
                    chosen  = True
                    squareList= []
                    return chosen, sizeOfGridValue, squareList
                elif size75.collidepoint(pos):
                    sizeOfGridValue = 75
                    chosen  = True
                    squareList = []
                    return chosen, sizeOfGridValue, squareList
                elif size100.collidepoint(pos):
                    sizeOfGridValue = 100
                    chosen  = True
                    squareList = []
                    return chosen, sizeOfGridValue, squareList

        #Boxes
        pygame.draw.rect(screenDisplay, white,(325,205,330,190))
        pygame.draw.rect(screenDisplay, black,(325,205,330,190),3)
        size5 = pygame.draw.rect(screenDisplay, white,(335,215,150,50))
        pygame.draw.rect(screenDisplay, black,(335,215,150,50),3)
        size10 = pygame.draw.rect(screenDisplay, white,(495,215,150,50))
        pygame.draw.rect(screenDisplay, black,(495,215,150,50),3)
        size25 = pygame.draw.rect(screenDisplay, white,(335,275,150,50))
        pygame.draw.rect(screenDisplay, black,(335,275,150,50),3)
        size50 = pygame.draw.rect(screenDisplay, white,(495,275,150,50))
        pygame.draw.rect(screenDisplay, black,(495,275,150,50),3)
        size75 = pygame.draw.rect(screenDisplay, white,(335,335,150,50))
        pygame.draw.rect(screenDisplay, black,(335,335,150,50),3)
        size100 = pygame.draw.rect(screenDisplay, white,(495,335,150,50))
        pygame.draw.rect(screenDisplay, black,(495,335,150,50),3)

        #Text
        text = sizeFont.render('5 x 5',1, (black))
        textpos = (373,225)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('10 x 10',1, (black))
        textpos = (515,225)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('25 x 25',1, (black))
        textpos = (355,285)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('50 x 50',1, (black))
        textpos = (515,285)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('75 x 75',1, (black))
        textpos = (355,345)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('100 x 100',1, (black))
        textpos = (496,345)
        screenDisplay.blit(text, textpos)

        pygame.display.update()
        clock.tick(11)

def stepRun(grid, sizeOfGridValue):
        grid = []

        for i in range(sizeOfGridValue):
            grid.append([])

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                if squareList[row][col].colour == red:
                    grid[row].append('*')
                else:
                    grid[row].append(' ')

        tempGrid = []

        for row in range(sizeOfGridValue):
            tempGrid.append([])
            for column in range(sizeOfGridValue):
                tempGrid[row].append(' ')

        for row in range(sizeOfGridValue):
            for column in range(sizeOfGridValue):
                count = 0
                if grid[row][column] == '*':
                    if row+1 < sizeOfGridValue:
                        if grid[row+1][column] == '*':
                            count += 1
                    if row-1 > -1:
                        if grid[row-1][column] == '*':
                            count += 1
                    if column+1 <sizeOfGridValue:
                        if grid[row][column+1] == '*':
                            count += 1
                    if column-1 > -1:
                        if grid[row][column-1] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue and row+1 < sizeOfGridValue:
                        if grid[row+1][column+1] == '*':
                            count += 1
                    if row-1 > -1 and column-1 > -1:
                        if grid[row-1][column-1] == '*':
                            count += 1
                    if row+1 < sizeOfGridValue and column-1 > -1:
                        if grid[row+1][column-1] == '*':
                            count += 1
                    if row-1 > -1 and column+1 < sizeOfGridValue:
                        if grid[row-1][column+1] == '*':
                            count += 1

                    if count == 2 or count == 3:
                        tempGrid[row][column] = '*'
                    else:
                        tempGrid[row][column] = ' '

                elif grid[row][column] == ' ':
                    if row+1 < sizeOfGridValue:
                        if grid[row+1][column] == '*':
                            count += 1
                    if row-1 > -1:
                        if grid[row-1][column] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue:
                        if grid[row][column+1] == '*':
                            count += 1
                    if column-1 > -1:
                        if grid[row][column-1] == '*':
                            count += 1
                    if column+1 < sizeOfGridValue and row+1 < sizeOfGridValue:
                        if grid[row+1][column+1] == '*':
                            count += 1
                    if row-1 > -1 and column-1 > -1:
                        if grid[row-1][column-1] == '*':
                            count += 1
                    if row+1 < sizeOfGridValue and column-1 > -1:
                        if grid[row+1][column-1] == '*':
                            count += 1
                    if row-1 > -1 and column+1 < sizeOfGridValue:
                        if grid[row-1][column+1] == '*':
                            count += 1

                    if count == 3:
                        tempGrid[row][column] = '*'
                    else:
                        tempGrid[row][column] = ' '

        grid = []
        grid = tempGrid

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                if grid[row][col] == '*':
                    squareList[row][col].colour = red
                    squareList[row][col].image.fill(red)
                else:
                    squareList[row][col].colour = white
                    squareList[row][col].image.fill(white)

        global generations
        generations += 1

def patternMenu():
    global squareList
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if blinker.collidepoint(pos):
                    chosen  = True
                    x = 'blinker'
                    patterns(x)
                    return chosen
                elif toad.collidepoint(pos):
                    chosen = True
                    x = 'toad'
                    patterns(x)
                    return chosen
                elif beacon.collidepoint(pos):
                    chosen = True
                    x = 'beacon'
                    patterns(x)
                    return chosen
                elif pulsar.collidepoint(pos):
                    chosen = True
                    x = 'pulsar'
                    squareList, sizeOfGridValue = patterns(x)
                    return chosen
                elif pentadecathalon.collidepoint(pos):
                    chosen = True
                    x = 'pentadecathalon'
                    patterns(x)
                    return chosen
                elif glider.collidepoint(pos):
                    chosen = True
                    x = 'glider'
                    patterns(x)
                    return chosen
                elif lightweightSpaceship.collidepoint(pos):
                    chosen = True
                    x = 'lightweight spaceship'
                    patterns(x)
                    return chosen
                elif theRPentomino.collidepoint(pos):
                    chosen = True
                    x = 'the r pentomino'
                    patterns(x)
                    return chosen
                elif dieHard.collidepoint(pos):
                    chosen = True
                    x = 'die hard'
                    patterns(x)
                    return chosen

        #Boxes
        pygame.draw.rect(screenDisplay, grey,(225,15,550,570))
        pygame.draw.rect(screenDisplay, black,(225,15,550,570),3)
        pygame.draw.rect(screenDisplay, white,(355,25,270,45))
        pygame.draw.rect(screenDisplay, black,(355,25,270,45),3)
        blinker = pygame.draw.rect(screenDisplay, white,(240,90,125,40))
        pygame.draw.rect(screenDisplay, black,(240,90,125,40),3)
        toad = pygame.draw.rect(screenDisplay, white,(378,90,85,40))
        pygame.draw.rect(screenDisplay, black,(378,90,85,40),3)
        beacon = pygame.draw.rect(screenDisplay, white,(475,90,125,40))
        pygame.draw.rect(screenDisplay, black,(475,90,125,40),3)
        pulsar = pygame.draw.rect(screenDisplay, white,(615,90,115,40))
        pygame.draw.rect(screenDisplay, black,(615,90,115,40),3)
        pentadecathalon = pygame.draw.rect(screenDisplay, white,(240,140,280,40))
        pygame.draw.rect(screenDisplay, black,(240,140,280,40),3)
        glider = pygame.draw.rect(screenDisplay, white,(535,140,110,40))
        pygame.draw.rect(screenDisplay, black,(535,140,110,40),3)
        lightweightSpaceship = pygame.draw.rect(screenDisplay, white,(240,190,375,40))
        pygame.draw.rect(screenDisplay, black,(240,191,375,40),3)
        theRPentomino = pygame.draw.rect(screenDisplay, white,(240,241,282,40))
        pygame.draw.rect(screenDisplay, black,(240,241,282,40),3)
        dieHard = pygame.draw.rect(screenDisplay, white,(535,240,145,40))
        pygame.draw.rect(screenDisplay, black,(535,240,145,40),3)

        #Text
        text = sizeFont.render('Select a pattern',1, (black))
        textpos = (365,30)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Blinker',1, (black))
        textpos = (245,95)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Toad',1, (black))
        textpos = (383,95)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Beacon',1, (black))
        textpos = (480,95)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Pulsar',1, (black))
        textpos = (620,95)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Pentadecathalon',1, (black))
        textpos = (245,145)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Glider',1, (black))
        textpos = (540,145)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Lightweight Spaceship',1, (black))
        textpos = (245,195)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('The R-pentomino',1, (black))
        textpos = (245,245)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Die hard',1, (black))
        textpos = (540,245)
        screenDisplay.blit(text, textpos)

        pygame.display.update()
        clock.tick(11)

def patterns(x):
    clearGrid()
    global sizeOfGridValue, squareList
    if x == 'blinker':
        pattern = blinker()
    elif x == 'toad':
        pattern = toad()
    elif x == 'beacon':
        pattern = beacon()
    elif x == 'pulsar':
        while sizeOfGridValue < 15:
            sizeOfGridValue = grid25()
            squareList = gridSetup(sizeOfGridValue, [])
        pattern = pulsar()
    elif x == 'pentadecathalon':
        while sizeOfGridValue < 15:
            sizeOfGridValue = grid25()
            squareList = gridSetup(sizeOfGridValue, [])
        pattern = pentadecathalon()
    elif x == 'glider':
        pattern = glider()
    elif x == 'lightweight spaceship':
        while sizeOfGridValue < 6:
            sizeOfGridValue = grid10()
            squareList = gridSetup(sizeOfGridValue, [])
        pattern = lightweightSpaceship()
    elif x == 'the r pentomino':
        pattern = theRPentomino()
    elif x == 'die hard':
        while sizeOfGridValue < 6:
            sizeOfGridValue = grid10()
            squareList = gridSetup(sizeOfGridValue, [])
        pattern = dieHard()

    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            if pattern[row][col] == '*':
                squareList[row][col].colour = red
                squareList[row][col].image.fill(red)
            else:
                squareList[row][col].colour = white
                squareList[row][col].image.fill(white)

    return squareList, sizeOfGridValue

def blinker():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Blinker/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def toad():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Toad/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def beacon():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Beacon/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def pulsar():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Pulsar/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def pentadecathalon():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Pentadecathalon/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def glider():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Glider/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def lightweightSpaceship():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Lightweight Spaceship/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def theRPentomino():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/The R-pentomino/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def dieHard():
    pattern = []
    for i in range(sizeOfGridValue):
        pattern.append([])
    f = open('Patterns/Die Hard/%d.txt' % tuple([sizeOfGridValue]),'r')
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                pattern[count].append(char)
        count += 1
    f.close()
    return pattern

def emptyValidate():
    empty = True

    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            if squareList[row][col].colour == red:
                empty = False

    return empty

def emptyMessage():
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if close.collidepoint(pos):
                    stopped = True
                    return stopped

        pygame.draw.rect(screenDisplay, white,(290,190,425,100))
        close = pygame.draw.rect(screenDisplay, red,(690,191,25,25))
        pygame.draw.line(screenDisplay, black,(691,214),(714,190),3)
        pygame.draw.line(screenDisplay, black,(689,190),(714,214),3)
        pygame.draw.rect(screenDisplay, black,(290,190,425,100),3)

        text = sizeFont.render('The grid is empty.',1, (black))
        textpos = (300,200)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Put something in the grid.',1, (black))
        textpos = (300,250)
        screenDisplay.blit(text, textpos)

        pygame.display.update()
        clock.tick(11)

def grid25():
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if size25.collidepoint(pos):
                    sizeOfGridValue = 25
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size50.collidepoint(pos):
                    sizeOfGridValue = 50
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size75.collidepoint(pos):
                    sizeOfGridValue = 75
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size100.collidepoint(pos):
                    sizeOfGridValue = 100
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue

        pygame.draw.rect(screenDisplay, white,(265,170,475,240))
        pygame.draw.rect(screenDisplay, black,(265,170,475,240),3)
        size25 = pygame.draw.rect(screenDisplay, white,(335,275,150,50))
        pygame.draw.rect(screenDisplay, black,(335,275,150,50),3)
        size50 = pygame.draw.rect(screenDisplay, white,(495,275,150,50))
        pygame.draw.rect(screenDisplay, black,(495,275,150,50),3)
        size75 = pygame.draw.rect(screenDisplay, white,(335,335,150,50))
        pygame.draw.rect(screenDisplay, black,(335,335,150,50),3)
        size100 = pygame.draw.rect(screenDisplay, white,(495,335,150,50))
        pygame.draw.rect(screenDisplay, black,(495,335,150,50),3)

        text = sizeFont.render('The size of grid is too small.',1, (black))
        textpos = (275,180)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Choose a bigger size.',1, (black))
        textpos = (300,230)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('25 x 25',1, (black))
        textpos = (355,285)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('50 x 50',1, (black))
        textpos = (515,285)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('75 x 75',1, (black))
        textpos = (355,345)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('100 x 100',1, (black))
        textpos = (496,345)
        screenDisplay.blit(text, textpos)

        pygame.display.update()
        clock.tick(11)

def grid10():
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if size10.collidepoint(pos):
                    sizeOfGridValue = 10
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size25.collidepoint(pos):
                    sizeOfGridValue = 25
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size50.collidepoint(pos):
                    sizeOfGridValue = 50
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size75.collidepoint(pos):
                    sizeOfGridValue = 75
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue
                elif size100.collidepoint(pos):
                    sizeOfGridValue = 100
                    chosen  = True
                    squareList = []
                    return sizeOfGridValue

        pygame.draw.rect(screenDisplay, white,(265,170,475,300))
        pygame.draw.rect(screenDisplay, black,(265,170,475,300),3)
        size10 = pygame.draw.rect(screenDisplay, white,(410,275,150,50))
        pygame.draw.rect(screenDisplay, black,(410,275,150,50),3)
        size25 = pygame.draw.rect(screenDisplay, white,(335,335,150,50))
        pygame.draw.rect(screenDisplay, black,(335,335,150,50),3)
        size50 = pygame.draw.rect(screenDisplay, white,(495,335,150,50))
        pygame.draw.rect(screenDisplay, black,(495,335,150,50),3)
        size75 = pygame.draw.rect(screenDisplay, white,(335,395,150,50))
        pygame.draw.rect(screenDisplay, black,(335,395,150,50),3)
        size100 = pygame.draw.rect(screenDisplay, white,(495,395,150,50))
        pygame.draw.rect(screenDisplay, black,(495,395,150,50),3)

        text = sizeFont.render('The size of grid is too small.',1, (black))
        textpos = (275,180)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('Choose a bigger size.',1, (black))
        textpos = (300,230)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('10 x 10',1, (black))
        textpos = (430,285)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('25 x 25',1, (black))
        textpos = (355,345)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('50 x 50',1, (black))
        textpos = (515,345)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('75 x 75',1, (black))
        textpos = (355,405)
        screenDisplay.blit(text, textpos)
        text = sizeFont.render('100 x 100',1, (black))
        textpos = (496,405)
        screenDisplay.blit(text, textpos)

        pygame.display.update()
        clock.tick(11)

def main():
    end = False

    while not end:
        screenDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        global speedValue, sizeOfGridValue, squareList, generations, stable, stableGen

        menuBackground()
        nameOfPattern, speed, sizeOfGrid, start, stop, step, clear = menuBoxes()
        menuText()
        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                screenDisplay.blit(squareList[row][col].image, squareList[row][col].rect)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos < (200,600):
                speedValue, sizeOfGridValue, squareList = button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos)
            else:
                squareChange(pos)

        pygame.display.update()
        clock.tick(11)

gridSetup(sizeOfGridValue, squareList)
main()
pygame.display.quit()
quit()
