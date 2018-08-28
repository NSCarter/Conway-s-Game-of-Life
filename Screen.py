import pygame

pygame.init()

displayWidth = 800
displayHeight = 600

white = (255,255,255)
blue = (0,155,255)
black = (0,0,0)
grey = (128,128,128)
red = (255,0,0)

font = pygame.font.Font('freesansbold.ttf', 16)
speedFont = pygame.font.Font('freesansbold.ttf', 32)
speedValue = 5
sizeOfGrid = 10
squareSize = 1.2
gridWidth = 600
tempGrid = []

screenDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Conway\'s game of life')
clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        super(Block, self).__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((width,height))
        self.colour = colour
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animate = False
    def update(self):
        self.image = pygame.Surface((self.height/2,self.width/2))

blockList = pygame.sprite.Group()

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
    sizeOfGrid = pygame.draw.rect(screenDisplay, white,(62,210,75,25))
    pygame.draw.rect(screenDisplay, black,(62,210,75,25),3)
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
    text = font.render("%d x %d" % tuple([sizeOfGrid]*2), 1, (black))
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

def button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue):
    if nameOfPattern.collidepoint(pos):
        print 'Name of pattern'
    elif speed.collidepoint(pos):
        print 'Speed'
        chosen = False
        while chosen == False:
            chosen, speedValue = speedMenu(speedValue, pos)
    elif sizeOfGrid.collidepoint(pos):
        print 'Size of the grid'
    elif start.collidepoint(pos):
        print 'Start'
        startRun()
    elif stop.collidepoint(pos):
        print 'Stop'
    elif step.collidepoint(pos):
        print 'Step'
    elif clear.collidepoint(pos):
        print 'Clear'
        clearGrid()
    else:
        print 'False'

def speedMenu(speedValue, pos):
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
##        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if speed1.collidepoint(pos):
            print '1'
            speedValue = 1
            chosen = True
        elif speed2.collidepoint(pos):
            print '2'
            speedValue = 2
            chosen = True
        elif speed3.collidepoint(pos):
            print '3'
            speedValue = 3
            chosen = True
        elif speed4.collidepoint(pos):
            print '4'
            speedValue = 4
            chosen = True
        elif speed5.collidepoint(pos):
            print '5'
            speedValue = 5
            chosen = True
        elif speed6.collidepoint(pos):
            print '6'
            speedValue = 6
            chosen = True
        elif speed7.collidepoint(pos):
            print '7'
            speedValue = 7
            chosen = True
        elif speed8.collidepoint(pos):
            print '8'
            speedValue = 8
            chosen = True
        elif speed9.collidepoint(pos):
            print '9'
            speedValue = 9
            chosen = True
            return chosen, speedValue

        pygame.display.update()
        clock.tick(12)

def gridSetup():
    row = 0
    column = 0
    x = 0
    y = 0
    for i in range(squareSize**2):
        if column * (gridWidth/squareSize) > gridWidth - (gridWidth/squareSize):
            row += 1
            column = 0
        x = 202 + (column * (gridWidth/squareSize))
        y = row * (displayHeight/squareSize)
        column += 1
        blockList.add(Block(x,y,gridWidth/squareSize,displayHeight/squareSize,white))

def blockChange(pos):
    for Block in blockList:
        if Block.rect.collidepoint(pos):
            Block.animate = True
            if Block.colour == white:
                Block.colour = red
                Block.image.fill(red)
            elif Block.colour == red:
                Block.colour = white
                Block.image.fill(white)

def startRun():
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.display.quit()
                quit()

        for Block in blockList:
            if Block.colour == red:
                print '*'

        del tempGrid[:]

##        for row in range(10):
##                tempGrid.append([])
##                for column in range(10):
##                    tempGrid[row].append(' ')
##
##        for row in range(10):
##            for column in range(10):
##                count = 0
##                if blockList[row][column] == '*':
##                    if row+1 < 10:
##                        if blockList[row+1][column] == '*':
##                            count += 1
##                    if row-1 > -1:
##                        if blockList[row-1][column] == '*':
##                            count += 1
##                    if column+1 < 10:
##                        if blockList[row][column+1] == '*':
##                            count += 1
##                    if column-1 > -1:
##                        if blockList[row][column-1] == '*':
##                            count += 1
##                    if column+1 < 10 and row+1 < 10:
##                        if blockList[row+1][column+1] == '*':
##                            count += 1
##                    if row-1 > -1 and column-1 > -1:
##                        if blockList[row-1][column-1] == '*':
##                            count += 1
##                    if row+1 < 10 and column-1 > -1:
##                        if blockList[row+1][column-1] == '*':
##                            count += 1
##                    if row-1 > -1 and column+1 < 10:
##                        if grid[row-1][column+1] == '*':
##                            count += 1
##
##                    if count == 2 or count == 3:
##                        tempGrid[row][column] = '*'
##                    else:
##                        tempGrid[row][column] = ' '
##
##                elif blockList[row][column] == ' ':
##                    if row+1 < 10:
##                        if blockList[row+1][column] == '*':
##                            count += 1
##                    if row-1 > -1:
##                        if blockList[row-1][column] == '*':
##                            count += 1
##                    if column+1 < 10:
##                        if blockList[row][column+1] == '*':
##                            count += 1
##                    if column-1 > -1:
##                        if blockList[row][column-1] == '*':
##                            count += 1
##                    if column+1 < 10 and row+1 < 10:
##                        if blockList[row+1][column+1] == '*':
##                            count += 1
##                    if row-1 > -1 and column-1 > -1:
##                        if blockList[row-1][column-1] == '*':
##                            count += 1
##                    if row+1 < 10 and column-1 > -1:
##                        if blockList[row+1][column-1] == '*':
##                            count += 1
##                    if row-1 > -1 and column+1 < 10:
##                        if blockList[row-1][column+1] == '*':
##                            count += 1
##
##                    if count == 3:
##                        tempGrid[row][column] = '*'
##                    else:
##                        tempGrid[row][column] = ' '
##
##        del grid [:]
##        grid = tempGrid

def clearGrid():
    for Block in blockList:
        Block.colour = white
        Block.image.fill(white)

def main():
    end = False

    while not end:
        screenDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        menuBackground()
        nameOfPattern, speed, sizeOfGrid, start, stop, step, clear = menuBoxes()
        menuText()
        blockList.draw(screenDisplay)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos < (200,600):
                button(nameOfPattern, speed, sizeOfGrid, start, stop, step, clear, pos, speedValue)
            else:
                blockChange(pos)

        pygame.display.update()
        clock.tick(12)

gridSetup()
main()
pygame.display.quit()
quit()
