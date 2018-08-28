import pygame
import time

pygame.init()

#Size of the screen
displayWidth = 800
displayHeight = 600

#Colours
white = (255,255,255)
blue = (0,155,255)
black = (0,0,0)
grey = (128,128,128)
red = (255,0,0)

#Fonts used for displaying text
font = pygame.font.Font('freesansbold.ttf', 16)
speedFont = pygame.font.Font('freesansbold.ttf', 32)
sizeFont = pygame.font.Font('freesansbold.ttf', 32)
#Start value for speed, size of the grid and the square size
speedValue = 5
sizeOfGridValue = 10
#The amount of the screen used for the grid
gridWidth = 600
#Grids used for running through the algorithm
grid = []
tempGrid = []
liveCells = []

#Set the size of the screen. the name of the screen and sefine the clock
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

def button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue, sizeOfGridValue):
    if nameOfPattern.collidepoint(pos):
        print 'Name of pattern'
    elif speed.collidepoint(pos):
        chosen = False
        while chosen == False:
            chosen, speedValue = speedMenu(speedValue, pos)
    elif sizeOfGrid.collidepoint(pos):
        chosen = False
        while chosen == False:
            chosen, sizeOfGridValue = sizeOfGridMenu(sizeOfGridValue, pos)
        gridSetup(sizeOfGridValue)
    elif start.collidepoint(pos):
        print 'Start'
        run(grid)
    elif stop.collidepoint(pos):
        print 'Stop'
    elif step.collidepoint(pos):
        print 'Step'
    elif clear.collidepoint(pos):
        clearGrid()
    else:
        print 'False'
    return speedValue, sizeOfGridValue

def speedMenu(speedValue, pos):
    time.sleep(0.1)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

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

        pygame.display.update()
        clock.tick(11)

def gridSetup(sizeOfGridValue):
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

def run(grid):
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

        del grid[:]

        for i in range(sizeOfGridValue):
            grid.append([])

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                if squareList[row][col].colour == red:
                    grid[row].append('*')
                else:
                    grid[row].append(' ')

        del tempGrid[:]

        for row in range(sizeOfGridValue):
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
                    else:
                        tempGrid[row][column] = ' '

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
                    else:
                        tempGrid[row][column] = ' '

        del grid [:]
        grid = tempGrid

        del liveCells[:]

        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                if grid[row][col] == '*':
                    squareList[row][col].colour = red
                    squareList[row][col].image.fill(red)
                else:
                    squareList[row][col].colour = white
                    squareList[row][col].image.fill(white)

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

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if size5.collidepoint(pos):
                sizeOfGridValue = 5
                chosen  = True
##                clearGrid()
                squareList = []
                return chosen, sizeOfGridValue
            elif size10.collidepoint(pos):
                sizeOfGridValue = 10
                chosen  = True
##                squareList.empty()
                squareList = []
                return chosen, sizeOfGridValue
            elif size25.collidepoint(pos):
                sizeOfGridValue = 25
                chosen  = True
                squareList = []
                return chosen, sizeOfGridValue
            elif size50.collidepoint(pos):
                sizeOfGridValue = 50
                chosen  = True
                squareList.empty()
                return chosen, sizeOfGridValue
            elif size75.collidepoint(pos):
                sizeOfGridValue = 75
                chosen  = True
                squareList.empty()
                return chosen, sizeOfGridValue
            elif size100.collidepoint(pos):
                sizeOfGridValue = 100
                chosen  = True
                squareList.empty()
                return chosen, sizeOfGridValue

        pygame.display.update()
        clock.tick(11)

def main():
    end = False

    while not end:
        screenDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        global speedValue, sizeOfGridValue

        menuBackground()
        nameOfPattern, speed, sizeOfGrid, start, stop, step, clear = menuBoxes()
        menuText()
##        squareList.draw(screenDisplay)
        for row in range(len(squareList)):
            for col in range(len(squareList[row])):
                screenDisplay.blit(squareList[row][col].image, squareList[row][col].rect)

##    for row in range(len(BlockList)):
##        for col in range(len(BlockList[row])):
####            print BlockList[row][col]
####            BlockList[row][col].draw()
##            screen.blit(BlockList[row][col].image, BlockList[row][col].rect)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos < (200,600):
                speedValue, sizeOfGridValue = button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue, sizeOfGridValue)
            else:
                squareChange(pos)

        pygame.display.update()
        clock.tick(11)

gridSetup(sizeOfGridValue)
main()
pygame.display.quit()
quit()
