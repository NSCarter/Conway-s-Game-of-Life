'''
~~~~~To Do~~~~~
Number of generations
Stable? + number of generations
Validate something is entered - run
Validate something is entered - step
Help - rules
Help - How to use
Pattern validation
Name of pattern
Grid lines maybe
More patterns
'''

import pygame
import time

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

def menuText():
    #Name of pattern
    text = font.render("Name of", 1, black)
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

def button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue, sizeOfGridValue, squareList):
    #If the nameOfPattern button was clicked
    if nameOfPattern.collidepoint(pos):
        chosen = False
        #While the user hasn't chosen a pattern
        while chosen == False:
##            chosen, squareList = patternMenu()
            #Display the pattern menu
            chosen = patternMenu()
    elif speed.collidepoint(pos):
        chosen = False
        while chosen == False:
            chosen, speedValue = speedMenu(speedValue, pos)
    elif sizeOfGrid.collidepoint(pos):
        chosen = False
        while chosen == False:
            chosen, sizeOfGridValue, squareList = sizeOfGridMenu(sizeOfGridValue, pos)
        gridSetup(sizeOfGridValue, squareList)
    elif start.collidepoint(pos):
        stopped = False
        while not stopped:
            stopped = startRun(grid, stop, sizeOfGridValue)
    elif stop.collidepoint(pos):
        print 'Stop'
    elif step.collidepoint(pos):
        stepRun(grid, sizeOfGridValue)
    elif clear.collidepoint(pos):
        clearGrid()
    else:
        print 'False'
    return speedValue, sizeOfGridValue, squareList

def speedMenu(speedValue, pos):
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

        #Clicked
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if speed1.collidepoint(pos):
                    speedValue = 1
                    chosen = True
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

        pygame.display.update()
        clock.tick(11)

def gridSetup(sizeOfGridValue, squareList):
    xPos = 0
    yPos = 0
    row = 0
    column = 0
    for i in range (sizeOfGridValue):
        squareList.append([])
        for j in range (sizeOfGridValue):
            if column * (gridWidth/sizeOfGridValue) > gridWidth - (gridWidth/sizeOfGridValue):
                row += 1
                column = 0
            xPos = 202 + (column * (gridWidth/sizeOfGridValue))
            yPos = row * (displayHeight/sizeOfGridValue)
            column += 1
            squareList[i].append(Square(xPos,yPos,gridWidth/sizeOfGridValue,displayHeight/sizeOfGridValue,white))

def squareChange(pos):
    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            if squareList[row][col].rect.collidepoint(pos):
                squareList[row][col].animate = True
                if squareList[row][col].colour == white:
                    squareList[row][col].colour = red
                    squareList[row][col].image.fill(red)
                elif squareList[row][col].colour == red:
                    squareList[row][col].colour = white
                    squareList[row][col].image.fill(white)

def startRun(grid, stop, sizeOfGridValue):
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if stop.collidepoint(pos):
                    stopped = True
                    return stopped

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

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                screenDisplay.blit(squareList[row][col].image, squareList[row][col].rect)

        time.sleep(9-speedValue)

        pygame.display.update()
        clock.tick(11)

def clearGrid():
    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            squareList[row][col].colour = white
            squareList[row][col].image.fill(white)


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

def patternMenu():
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
                    patterns(x)
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
    if x == 'blinker':
        pattern = blinker()
    elif x == 'toad':
        pattern = toad()
    elif x == 'beacon':
        pattern = beacon()
    elif x == 'pulsar':
        if sizeOfGridValue > 15:
            pattern = pulsar()
    elif x == 'pentadecathalon':
        if sizeOfGridValue > 15:
            pattern = pentadecathalon()
    elif x == 'glider':
        pattern = glider()
    elif x == 'lightweight spaceship':
        if sizeOfGridValue > 6:
            pattern = lightweightSpaceship()
    elif x == 'the r pentomino':
        pattern = theRPentomino()
    elif x == 'die hard':
        if sizeOfGridValue > 6:
            pattern = dieHard()
    for row in range(len(squareList)):
        for col in range(len(squareList[row])):
            if pattern[row][col] == '*':
                squareList[row][col].colour = red
                squareList[row][col].image.fill(red)
            else:
                squareList[row][col].colour = white
                squareList[row][col].image.fill(white)

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


def main():
    end = False

    while not end:
        screenDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        global speedValue, sizeOfGridValue, squareList

        menuBackground()
        nameOfPattern, speed, sizeOfGrid, start, stop, step, clear = menuBoxes()
        menuText()

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                screenDisplay.blit(squareList[row][col].image, squareList[row][col].rect)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos < (200,600):
                speedValue, sizeOfGridValue, squareList = button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue, sizeOfGridValue, squareList)
            else:
                squareChange(pos)

        pygame.display.update()
        clock.tick(11)

gridSetup(sizeOfGridValue, squareList)
main()
pygame.display.quit()
quit()
