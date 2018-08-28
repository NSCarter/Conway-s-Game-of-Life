import pygame

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
blue = (0,155,255)
black = (0,0,0)
grey = (128,128,128)

font = pygame.font.Font('freesansbold.ttf', 24)
speed = 5
sizeOfGrid = 10

screenDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Conway\'s game of life')
clock = pygame.time.Clock()

def menuBackground():
    pygame.draw.rect(screenDisplay, grey, (0,0,200,600))
    pygame.draw.line(screenDisplay, black,(200,0),(200,600),3)
    pygame.draw.line(screenDisplay, black,(0,90),(200,90),3)
    pygame.draw.line(screenDisplay, black,(0,260),(200,260),3)

def menuBoxes():
    #Name of pattern
    pygame.draw.rect(screenDisplay, white,(50,20,100,50))
    pygame.draw.rect(screenDisplay, black,(50,20,100,50),3)
    #Speed
    pygame.draw.rect(screenDisplay, white,(25,110,75,25))
    pygame.draw.rect(screenDisplay, black,(25,110,75,25),3)
    pygame.draw.rect(screenDisplay, white,(125,110,25,25))
    pygame.draw.rect(screenDisplay, black,(125,110,25,25),3)
    #Size of grid
    pygame.draw.rect(screenDisplay, white,(25,160,150,25))
    pygame.draw.rect(screenDisplay, black,(25,160,150,25),3)
    pygame.draw.rect(screenDisplay, white,(62,210,75,25))
    pygame.draw.rect(screenDisplay, black,(62,210,75,25),3)
    #Start
    start = pygame.draw.rect(screenDisplay, white,(62,285,75,25))
    pygame.draw.rect(screenDisplay, black,(62,285,75,25),3)
    #Stop
    pygame.draw.rect(screenDisplay, white,(62,335,75,25))
    pygame.draw.rect(screenDisplay, black,(62,335,75,25),3)
    #Step
    pygame.draw.rect(screenDisplay, white,(62,385,75,25))
    pygame.draw.rect(screenDisplay, black,(62,385,75,25),3)
    #Clear
    pygame.draw.rect(screenDisplay, white,(62,435,75,25))
    pygame.draw.rect(screenDisplay, black,(62,435,75,25),3)

def menuText():
    #Name of pattern
##    pText = textFont.render('P', True, white)
    text = font.render("Name of", True, black)
    textpos = (65,25)
    screenDisplay.blit(text, textpos)
    text = font.render("pattern", 1, (10, 10, 10))
    textpos = (70,45)
    screenDisplay.blit(text, textpos)
    #Speed
    text = font.render("Speed:", 1, (10, 10, 10))
    textpos = (32,115)
    screenDisplay.blit(text, textpos)
    text = font.render(str(speed), 1, (10, 10, 10))
    textpos = (132,115)
    screenDisplay.blit(text, textpos)
    #Size of grid
    text = font.render("Size of the grid:", 1, (10, 10, 10))
    textpos = (35,165)
    screenDisplay.blit(text, textpos)
    text = font.render("%d x %d" % tuple([sizeOfGrid]*2), 1, (10, 10, 10))
    textpos = (32,210)
    screenDisplay.blit(text, textpos)
    #Start
    text = font.render("Start", 1, (10, 10, 10))
    textpos = (77,290)
    screenDisplay.blit(text, textpos)
    #Stop
    text = font.render("Stop", 1, (10, 10, 10))
    textpos = (80,340)
    screenDisplay.blit(text, textpos)
    #Step
    text = font.render("Step", 1, (10, 10, 10))
    textpos = (80,390)
    screenDisplay.blit(text, textpos)
    #Clear
    text = font.render("Clear", 1, (10, 10, 10))
    textpos = (77,440)
    screenDisplay.blit(text, textpos)

def main ():
    stop = False

    while not stop:
        screenDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        menuBackground()
        menuBoxes()
        menuText()

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start.collidepoint(pos):
                print 'True'

        pygame.display.update()
        clock.tick(60)

main()
pygame.display.quit()
quit()
