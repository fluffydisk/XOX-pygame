# Example file showing a circle moving on screen
import pygame
# pygame setup
pygame.init()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
thicknesOFBorders=15
currentZone=0

ButtonColor = "white"
TextColor = "black"

mouseClicked=False

firstAreaMarked = False
secondAreaMarked = False
thirdAreaMarked = False
fourthAreaMarked = False
fifthAreaMarked = False
sixthAreaMarked = False
seventhAreaMarked = False
eighthAreaMarked = False
ninthAreaMarked = False

firstAreaDraw="A"
secAreaDraw="A"
thirdAreaDraw="A"
fourthAreaDraw="A"
fifthAreaDraw="A"
sixthAreaDraw="A"
seventhAreaDraw="A"
eighthAreaDraw="A"
ninthAreaDraw="A"


undertaleFont = pygame.font.Font("Gamer.ttf", 100)
firstArea = undertaleFont.render("1", 1, "black")
secondArea = undertaleFont.render("2", 1, "black")
thirdArea = undertaleFont.render("3", 1, "black")
fourthArea = undertaleFont.render("4", 1, "black")
fifthArea = undertaleFont.render("5", 1, "black")
sixthArea = undertaleFont.render("6", 1, "black")
seventhArea = undertaleFont.render("7", 1, "black")
eighthArea = undertaleFont.render("8", 1, "black")
ninthArea = undertaleFont.render("9", 1, "black")

def writeX(xStart, yStart, SCREEN_WIDTH, SCREEN_HEIGHT):
    pygame.draw.line(screen, "black", (xStart, yStart), (xStart+SCREEN_WIDTH/3, yStart+SCREEN_HEIGHT/3), 5)
    pygame.draw.line(screen, "black", (xStart+SCREEN_WIDTH/3, yStart), (xStart, yStart+SCREEN_HEIGHT/3), 5)

def writeO(xStart, yStart, SCREEN_WIDTH, SCREEN_HEIGHT):
    pygame.draw.circle(screen, "black", (xStart, yStart), SCREEN_HEIGHT/6, 5)


Play=False
turn = "X"
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked=True
        else:
            mouseClicked=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        Play = False

    screen.fill("blue")
    # fill the screen with a color to wipe away anything from last frame
    if Play==False:


        OpeningScreen = undertaleFont.render("BASLA", 1, TextColor)
        pygame.draw.rect(screen, ButtonColor, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-40, 200, 80))
        mousePos=pygame.mouse.get_pos()
        screen.blit(OpeningScreen, (SCREEN_WIDTH/2-90, SCREEN_HEIGHT/2-40))
        if(mousePos[0]>=SCREEN_WIDTH/2-100 and mousePos[0]<=SCREEN_WIDTH/2+100) and (mousePos[1]>=SCREEN_HEIGHT/2-40 and mousePos[1]<=SCREEN_HEIGHT/2+40):
            ButtonColor="black"
            TextColor="white"
            if mouseClicked==True:
                mouseClicked = False
                Play=True
                turn = "X"
                firstAreaMarked = False
                secondAreaMarked = False
                thirdAreaMarked = False
                fourthAreaMarked = False
                fifthAreaMarked = False
                sixthAreaMarked = False
                seventhAreaMarked = False
                eighthAreaMarked = False
                ninthAreaMarked = False
                firstAreaDraw = "A"
                secAreaDraw = "A"
                thirdAreaDraw = "A"
                fourthAreaDraw = "A"
                fifthAreaDraw = "A"
                sixthAreaDraw = "A"
                seventhAreaDraw = "A"
                eighthAreaDraw = "A"
                ninthAreaDraw = "A"



        else:
            ButtonColor="white"
            TextColor = "black"


        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    if Play==True:
        pygame.draw.line(screen, "black", [SCREEN_WIDTH/3, 0], [SCREEN_WIDTH/3, SCREEN_HEIGHT])
        pygame.draw.line(screen, "black", [SCREEN_WIDTH / 3*2, 0], [SCREEN_WIDTH / 3*2, SCREEN_HEIGHT])

        pygame.draw.line(screen, "black", [0, SCREEN_HEIGHT/3], [SCREEN_WIDTH, SCREEN_HEIGHT/3])
        pygame.draw.line(screen, "black", [0, SCREEN_HEIGHT/3*2], [SCREEN_WIDTH, SCREEN_HEIGHT/3*2])





        mousePos = pygame.mouse.get_pos()

        if(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]<=SCREEN_HEIGHT/3):
            if currentZone!=1:
                currentZone = 1
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, ("black"), (0, 0, SCREEN_WIDTH/3, SCREEN_HEIGHT/3), thicknesOFBorders)
            if mouseClicked == True:
                firstAreaMarked = True

        elif(mousePos[0]<=SCREEN_WIDTH/3*2 and mousePos[0]>SCREEN_WIDTH/3) and (mousePos[1]<=SCREEN_HEIGHT/3):
            if currentZone != 2:
                currentZone = 2
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                secondAreaMarked=True
        elif(mousePos[0]<=SCREEN_WIDTH and mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]<=SCREEN_HEIGHT/3):
            if currentZone!=3:
                currentZone = 3
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (SCREEN_WIDTH / 3*2, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                thirdAreaMarked=True

        elif(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
            if currentZone!=4:
                currentZone = 4
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (0, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                fourthAreaMarked=True
        elif(mousePos[0]>SCREEN_WIDTH/3 and mousePos[0]<=SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
            if currentZone!=5:
                currentZone = 5
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked == True:
                fifthAreaMarked = True

        elif(mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
            if currentZone!=6:
                currentZone = 6
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3*2, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                sixthAreaMarked=True

        elif(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]>SCREEN_HEIGHT/3*2):
            if currentZone!=7:
                currentZone = 7
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (0, SCREEN_HEIGHT / 3*2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                seventhAreaMarked=True
        elif(mousePos[0]>SCREEN_WIDTH/3 and mousePos[0]<=SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3*2):
            if currentZone!=8:
                currentZone = 8
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, SCREEN_HEIGHT / 3 * 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                eighthAreaMarked=True

        elif(mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3*2):
            if currentZone!=9:
                currentZone = 9
                print("{}. Alandasin".format(currentZone))
            pygame.draw.rect(screen, "black",(SCREEN_WIDTH / 3*2, SCREEN_HEIGHT / 3 * 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
            if mouseClicked==True:
                ninthAreaMarked=True

        if not firstAreaMarked:
            screen.blit(firstArea, (SCREEN_WIDTH/6, SCREEN_HEIGHT/6))
        else:
            if turn == "X" and firstAreaDraw=="A":
                turn="O"
                firstAreaDraw="X"
            if turn=="O" and firstAreaDraw == "A":
                turn="X"
                firstAreaDraw="O"

        if not secondAreaMarked:
            screen.blit(secondArea, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
        else:
            if turn=="X" and secAreaDraw=="A":
                turn = "O"
                secAreaDraw="X"
            if turn=="O" and secAreaDraw=="A":
                turn = "X"
                secAreaDraw = "O"

        if not thirdAreaMarked:
            screen.blit(thirdArea,(SCREEN_WIDTH/6*5, SCREEN_HEIGHT / 6))
        else:
            if turn=="X" and thirdAreaDraw=="A":
                turn="O"
                thirdAreaDraw="X"
            if turn=="O" and thirdAreaDraw=="A":
                turn="X"
                thirdAreaDraw="O"

        if not fourthAreaMarked:
            screen.blit(fourthArea, (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2))
        else:
            if turn=="X" and fourthAreaDraw=="A":
                turn="O"
                fourthAreaDraw="X"
            if turn=="O" and fourthAreaDraw=="A":
                turn="X"
                fourthAreaDraw="O"
        if not fifthAreaMarked:
            screen.blit(fifthArea, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        else:
            if turn=="X" and fifthAreaDraw=="A":
                turn="O"
                fifthAreaDraw="X"
            if turn=="O" and fifthAreaDraw=="A":
                turn="X"
                fifthAreaDraw="O"
        if not sixthAreaMarked:
            screen.blit(sixthArea, (SCREEN_WIDTH / 6*5, SCREEN_HEIGHT / 2))
        else:
            if turn=="X" and sixthAreaDraw=="A":
                turn="O"
                sixthAreaDraw="X"
            if turn=="O" and sixthAreaDraw=="A":
                turn="X"
                sixthAreaDraw="O"
        if not seventhAreaMarked:
            screen.blit(seventhArea, (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6*5))
        else:
            if turn == "X" and seventhAreaDraw == "A":
                turn = "O"
                seventhAreaDraw = "X"
            if turn == "O" and seventhAreaDraw == "A":
                turn = "X"
                seventhAreaDraw = "O"
        if not eighthAreaMarked:
            screen.blit(eighthArea, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6 * 5))
        else:
            if turn=="X" and eighthAreaDraw=="A":
                turn="O"
                eighthAreaDraw="X"
            if turn=="O" and eighthAreaDraw=="A":
                turn="X"
                eighthAreaDraw="O"
        if not ninthAreaMarked:
            screen.blit(ninthArea, (SCREEN_WIDTH / 6*5, SCREEN_HEIGHT / 6 * 5))
        else:
            if turn=="X" and ninthAreaDraw=="A":
                turn="O"
                ninthAreaDraw="X"
            if turn=="O" and ninthAreaDraw=="A":
                turn="X"
                ninthAreaDraw="O"

        if firstAreaDraw=="X":
            writeX(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif firstAreaDraw=="O":
            writeO(SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)

        if secAreaDraw=="X":
            writeX(SCREEN_WIDTH / 3, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif secAreaDraw=="O":
            writeO(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)

        if thirdAreaDraw=="X":
            writeX(SCREEN_WIDTH / 3 * 2, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif thirdAreaDraw=="O":
            writeO(SCREEN_WIDTH / 6 * 5, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)

        if fourthAreaDraw=="X":
            writeX(0, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif fourthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)

        if fifthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif fifthAreaDraw=="O":
            writeO(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)

        if sixthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3*2, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif sixthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6*5, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)

        if seventhAreaDraw=="X":
            writeX(0, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif seventhAreaDraw=="O":
            writeO(SCREEN_WIDTH/6, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)

        if eighthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif eighthAreaDraw=="O":
            writeO(SCREEN_WIDTH/2, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)

        if ninthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3*2, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif ninthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6*5, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)



        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

pygame.quit()