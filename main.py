import pygame
pygame.init()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
thicknesOFBorders=15
currentZone=0

var=""

option1="X"
option2="O"

ButtonColor = "white"
TextColor = "black"

againButtonColor="black"
againTextColor="white"
exitTextColor="black"
exitButtonColor="white"


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


changingtoX=False
changingtoO=False

user_x_text = ''
user_o_text = ''
userXName=""
userOName=""

base_font = pygame.font.Font(None, 30)
oyuncuX = base_font.render("Oyuncu X'in ismi: ", 1, "black")
oyuncuO = base_font.render("OyuncuO'nun ismi: ", 1, "black")
oyuncuXNameInput = base_font.render(user_x_text, 1, "black")
oyuncuONameInput = base_font.render(user_o_text, 1, "black")
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

def gameRuleCheck(list):
    selectedOption=""
    if list[0][0]==option1 or list[0][0]==option2:
        selectedOption=list[0][0]
        if list[0][1]==selectedOption and list[0][2]==selectedOption:
            pygame.draw.line(screen, "yellow", [0, 100], [600, 100], 10)
            return selectedOption
        if list[1][1]==selectedOption and list[2][2]==selectedOption:
            pygame.draw.line(screen, "yellow", [0, 0], [600, 600], 10)
            return selectedOption
        if list[1][0]==selectedOption and list[2][0]==selectedOption:
            pygame.draw.line(screen, "yellow", [100, 0], [100, 600], 10)
            return selectedOption
    if list[2][2]==option1 or list[2][2]==option2:
        selectedOption=list[2][2]
        if list[1][2]==selectedOption and list[0][2]==selectedOption:
            pygame.draw.line(screen, "yellow", [500, 0], [500, 600], 10)
            return selectedOption
        if list[2][1]==selectedOption and list[2][0]==selectedOption:
            pygame.draw.line(screen, "yellow", [0, 500], [600, 500], 10)
            return selectedOption
    if list[2][0]==option1 or list[2][0]==option2:
        selectedOption=list[2][0]
        if list[1][1]==selectedOption and list[0][2]==selectedOption:
            pygame.draw.line(screen, "yellow", [0, 600], [600, 0], 10)
            return selectedOption
    if list[1][0]==option1 or list[1][0]==option2:
        selectedOption=list[1][0]
        if list[1][1] == selectedOption and list[1][2] == selectedOption:
            pygame.draw.line(screen, "yellow", [0, 300], [600, 300], 10)
            return selectedOption
    if list[0][1] == option1 or list[0][1] == option2:
        selectedOption=list[0][1]
        if list[1][1] == selectedOption and list[2][1] == selectedOption:
            pygame.draw.line(screen, "yellow", [300, 0], [300, 600], 10)
            return selectedOption
    return "P"

gameFinish=""
def gameFinished(winner, mouseClicked):
    mousePos = pygame.mouse.get_pos()
    if (mousePos[0]>=170 and mousePos[0]<=270) and (mousePos[1]>=300 and mousePos[1]<=350):
        if mouseClicked==True:
            return "StartScreen"
        againButtonColor="white"
        againTextColor="black"
    else:
        againTextColor="white"
        againButtonColor="black"
    if (mousePos[0] >= 330 and mousePos[0] <= 430) and (mousePos[1] >= 300 and mousePos[1] <= 350):
        if mouseClicked==True:
            return "Exit"
        exitButtonColor="black"
        exitTextColor="white"
    else:
        exitButtonColor="white"
        exitTextColor="black"
    again1 = base_font.render("Tekrar", 1, againTextColor)
    again2 = base_font.render("Oyna", 1, againTextColor)
    exit = base_font.render("Cikis Yap", 1, exitTextColor)

    background = pygame.Rect(150, 225, 300, 150)
    pygame.draw.rect(screen, "red", background)
    button1 = pygame.Rect(170, 300, 100, 50)
    button2 = pygame.Rect(330, 300, 100, 50)
    pygame.draw.rect(screen, againButtonColor, button1)
    pygame.draw.rect(screen, exitButtonColor, button2)

    screen.blit(again1, (170, 305))
    screen.blit(again2, (170, 325))
    screen.blit(exit, (330, 315))
    if winner=="X":
        screen.blit(base_font.render("Oyun bitti kazanan:", 1, "black"), (170, 240))
        screen.blit(base_font.render(userXName, 1, "black"), (270, 270))
    elif winner == "O":
        screen.blit(base_font.render("Oyun bitti kazanan: {}".format(userOName), 1, "black"), (170, 240))
        screen.blit(base_font.render(userOName, 1, "black"), (270, 270))
XOX = [["0","1","2"],["0","1"," 2"],["0","1","2"]]

Play=False
turn = "X"


active=False
inputFromX=False
inputFromO=False
input_first_player_rect = pygame.Rect(200, 150, 200, 40)
input_second_player_rect = pygame.Rect(200, 200, 200, 40)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
colorX = color_passive
colorO = color_passive

while running:
    oyuncuXNameInput = base_font.render(user_x_text, 1, "black")
    oyuncuONameInput = base_font.render(user_o_text, 1, "black")
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
        if event.type == pygame.KEYDOWN:
            if inputFromX:
                if event.key == pygame.K_RETURN:
                    inputFromX=False
                elif event.key == pygame.K_BACKSPACE:
                    user_x_text = user_x_text[:-1]
                else:
                    user_x_text += event.unicode
            if inputFromO:
                if event.key == pygame.K_RETURN:
                    inputFromO = False
                elif event.key == pygame.K_BACKSPACE:
                    user_o_text = user_o_text[:-1]
                else:
                    user_o_text += event.unicode



    screen.fill("blue")
    # fill the screen with a color to wipe away anything from last frame
    if Play==False:
        mousePos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, colorX, input_first_player_rect)
        pygame.draw.rect(screen, colorO, input_second_player_rect)
        text_surface_player_x = base_font.render(user_x_text, True, (255, 255, 255))

        if(mousePos[0]>=200 and mousePos[0]<=400) and (mousePos[1]>=200 and mousePos[1]<=240):
            colorO=color_active
            pygame.draw.rect(screen, colorO, input_second_player_rect)
            if mouseClicked==True:
                inputFromO=True
                if inputFromX==True:
                    changingtoO=True
                    inputFromX=False
                else:
                    changingtoO = False
        if inputFromO == True:
            screen.blit(oyuncuONameInput, (200,210))
            colorO = color_active
        elif changingtoO == True:
            screen.blit(oyuncuONameInput, (200,210))
            colorO = color_active
        elif changingtoX==True:
            if user_o_text=="":
                screen.blit(oyuncuO, (200, 210))
                colorO = color_passive
            else:
                screen.blit(oyuncuONameInput, (200, 210))
                colorO = color_passive
        elif inputFromO == False and user_o_text=="":
            screen.blit(oyuncuO, (200, 210))
            colorO = color_passive
        else:
            screen.blit(oyuncuONameInput, (200, 210))
            colorO = color_passive


        if(mousePos[0]>=200 and mousePos[0]<=400) and (mousePos[1]>=150 and mousePos[1]<=190):
            colorX=color_active
            pygame.draw.rect(screen, colorX, input_first_player_rect)
            if mouseClicked==True:
                inputFromX = True
                if inputFromO==True:
                    changingtoX=True
                    inputFromO= False
                else:
                    changingtoX=False
        if inputFromX == True:
            screen.blit(oyuncuXNameInput, (200,160))
            colorX = color_active
        elif changingtoX==True:
            screen.blit(oyuncuXNameInput, (200,160))
            colorX = color_active
        elif changingtoO==True:
            if user_x_text=="":
                screen.blit(oyuncuX, (200, 160))
                colorX = color_passive
            else:
                screen.blit(oyuncuXNameInput, (200, 160))
                colorX = color_passive
        elif inputFromX == False and user_x_text=="":
            screen.blit(oyuncuX, (200, 160))
            colorX = color_passive
        else:
            screen.blit(oyuncuXNameInput, (200, 160))
            colorX = color_passive

        OpeningScreen = undertaleFont.render("BASLA", 1, TextColor)
        pygame.draw.rect(screen, ButtonColor, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-40, 200, 80))

        screen.blit(OpeningScreen, (SCREEN_WIDTH/2-90, SCREEN_HEIGHT/2-40))
        if(mousePos[0]>=SCREEN_WIDTH/2-100 and mousePos[0]<=SCREEN_WIDTH/2+100) and (mousePos[1]>=SCREEN_HEIGHT/2-40 and mousePos[1]<=SCREEN_HEIGHT/2+40):
            ButtonColor="black"
            TextColor="white"
            if mouseClicked==True and (user_o_text != "" and user_x_text != ""):
                userXName=user_x_text
                userOName=user_o_text
                user_x_text=""
                user_o_text=""
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
                XOX = [["0", "1", "2"], ["0", "1", "2"], ["0", "1", "2"]]
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
        if var == "P":
            if(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]<=SCREEN_HEIGHT/3):
                if currentZone!=1:
                    currentZone = 1
                pygame.draw.rect(screen, ("black"), (0, 0, SCREEN_WIDTH/3, SCREEN_HEIGHT/3), thicknesOFBorders)
                if mouseClicked == True:
                    firstAreaMarked = True

            elif(mousePos[0]<=SCREEN_WIDTH/3*2 and mousePos[0]>SCREEN_WIDTH/3) and (mousePos[1]<=SCREEN_HEIGHT/3):
                if currentZone != 2:
                    currentZone = 2
                pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    secondAreaMarked=True
            elif(mousePos[0]<=SCREEN_WIDTH and mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]<=SCREEN_HEIGHT/3):
                if currentZone!=3:
                    currentZone = 3
                pygame.draw.rect(screen, "black", (SCREEN_WIDTH / 3*2, 0, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    thirdAreaMarked=True

            elif(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
                if currentZone!=4:
                    currentZone = 4
                pygame.draw.rect(screen, "black", (0, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    fourthAreaMarked=True
            elif(mousePos[0]>SCREEN_WIDTH/3 and mousePos[0]<=SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
                if currentZone!=5:
                    currentZone = 5
                pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked == True:
                    fifthAreaMarked = True

            elif(mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3 and mousePos[1]<=SCREEN_HEIGHT/3*2):
                if currentZone!=6:
                    currentZone = 6
                pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3*2, SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    sixthAreaMarked=True

            elif(mousePos[0]<=SCREEN_WIDTH/3) and (mousePos[1]>SCREEN_HEIGHT/3*2):
                if currentZone!=7:
                    currentZone = 7
                pygame.draw.rect(screen, "black", (0, SCREEN_HEIGHT / 3*2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    seventhAreaMarked=True
            elif(mousePos[0]>SCREEN_WIDTH/3 and mousePos[0]<=SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3*2):
                if currentZone!=8:
                    currentZone = 8
                pygame.draw.rect(screen, "black", (SCREEN_WIDTH/3, SCREEN_HEIGHT / 3 * 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3), thicknesOFBorders)
                if mouseClicked==True:
                    eighthAreaMarked=True

            elif(mousePos[0]>SCREEN_WIDTH/3*2) and (mousePos[1]>SCREEN_HEIGHT/3*2):
                if currentZone!=9:
                    currentZone = 9
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
            XOX[0][0]="X"
        elif firstAreaDraw=="O":
            writeO(SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[0][0] = "O"

        if secAreaDraw=="X":
            writeX(SCREEN_WIDTH / 3, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[0][1] = "X"
        elif secAreaDraw=="O":
            writeO(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[0][1] = "O"

        if thirdAreaDraw=="X":
            writeX(SCREEN_WIDTH / 3 * 2, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[0][2] = "X"
        elif thirdAreaDraw=="O":
            writeO(SCREEN_WIDTH / 6 * 5, SCREEN_HEIGHT / 6, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[0][2] = "O"

        if fourthAreaDraw=="X":
            writeX(0, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][0] = "X"
        elif fourthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][0] = "O"

        if fifthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][1] = "X"
        elif fifthAreaDraw=="O":
            writeO(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][1] = "O"

        if sixthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3*2, SCREEN_HEIGHT/3, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][2] = "X"
        elif sixthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6*5, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[1][2] = "O"

        if seventhAreaDraw=="X":
            writeX(0, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][0] = "X"
        elif seventhAreaDraw=="O":
            writeO(SCREEN_WIDTH/6, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][0] = "O"

        if eighthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][1] = "X"
        elif eighthAreaDraw=="O":
            writeO(SCREEN_WIDTH/2, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][1] = "O"

        if ninthAreaDraw=="X":
            writeX(SCREEN_WIDTH/3*2, SCREEN_HEIGHT/3*2, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][2] = "X"
        elif ninthAreaDraw=="O":
            writeO(SCREEN_WIDTH/6*5, SCREEN_HEIGHT/6*5, SCREEN_WIDTH, SCREEN_HEIGHT)
            XOX[2][2] = "O"
        var = gameRuleCheck(XOX)
        if var=="P":
            Play=True
        elif var=="O" or var=="X":
            gameFinish=gameFinished(var, mouseClicked)
            if gameFinish=="StartScreen":
                Play=False
            elif gameFinish=="Exit":
                running=False

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

pygame.quit()