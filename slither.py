import pygame
import time
import random
import os


pygame.init() 

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,180,0)
orange = (200,150,50)
yellow = (250,150,0)

gamewidth = 900
gameheight = 650
gamedisplay = pygame.display.set_mode((gamewidth,gameheight)) 
thickness = 30

pygame.display.set_caption('Python Slither')        
icon =pygame.image.load('image/apple.jpg')
pygame.display.set_icon(icon)


snakesize = 20
clock = pygame.time.Clock()
smallsize = pygame.font.SysFont(None, 25)
medsize = pygame.font.SysFont(None, 35)
largesize = pygame.font.SysFont(None , 45)
simg = pygame.image.load('image/shead.jpg')
aimg = pygame.image.load('image/apple.jpg')

def gamestart():
    start = True
    hist = False
    while start:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                start = False
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            
        gamedisplay.fill(white)
        message("Welcome to Python Slither",green, -100, "large")
        message("Eat as much apples as you can",blue, -60, "medium")
        message("But If you run over your snake or touch boundaries you will die!",red, -20, "small")
        message("press c to continue, p to pause , or q to quit",black, 40, "large")
        direc = os.path.dirname(__file__)
        new = "src/donot_change.txt"
        newdirec = os.path.join(direc , new)    
        if os.path.exists(newdirec):
            f = open(newdirec,"r")
            prLevel = f.read()
        else:
            store(0)
            f = open(newdirec,"r")
            prLevel = f.read()
        f.close()
        message("Highest Level reached : "+str(prLevel),blue,80,"medium")
        pygame.display.update()

    
def gameloop():
    global direct
    direct = "right"
    gameexit = False
    gameover = False
    lBoundary= gamewidth//2
    uBoundary = gameheight//2
    lBoundarychange =0
    uBoundarychange = 0
    speed = 8
    snakelist = []
    snakelength = 1
    sc = 0
    highscore = 5
    Level = 0
    addSpeed = 0.45
    applex,appley = apple()
    pygame.mixer.init(44100)
    while not gameexit:

        while gameover == True:
            gamedisplay.fill(black)
            direc = os.path.dirname(__file__)
            new = "src/donot_change.txt"
            newdirec = os.path.join(direc , new)
            if os.path.exists(newdirec):
                f = open(newdirec,"r")
                prevLevel = f.read()
            else:
                store(0)
                f = open(newdirec,"r")
                prevLevel = f.read()
            f.close()
            if Level >= int(prevLevel):
                message(" ""WOW""  ",orange ,-15, size= "large")
                message("!!TOP SCORER!!  ",orange ,25, size= "large")
                message("Level reached: "+str(Level),orange ,60, size= "medium")
                message("GAME OVER!",red, -70, size = "large")
                message("press c to try again or q to quit", blue, 90, size= "medium")
                pygame.display.update()
                store(Level)
            else:
                message("Level reached: "+str(Level),orange ,40, size= "medium")
                message("GAME OVER!",red, -20, size = "large")
                message("press c to try again or q to quit", blue, 80, size= "medium")
                pygame.display.update()
            
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if direct != "right":
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        direct = "left"
                        lBoundarychange = -snakesize
                        uBoundarychange = 0
                if direct != "left":
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        direct = "right"
                        lBoundarychange = snakesize
                        uBoundarychange= 0
                if direct != "down":
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        direct = "up"
                        uBoundarychange = -snakesize
                        lBoundarychange= 0
                if direct != "up":
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        direct = "down"
                        uBoundarychange= snakesize
                        lBoundarychange= 0
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_q:
                    gameexit = True

        if lBoundary >= gamewidth or lBoundary <0 or uBoundary >=gameheight or uBoundary < 0:
            pygame.mixer.music.load('src/gameover.wav')
            pygame.mixer.music.play(0)
     ##       while pygame.mixer.music.get_busy():
     ##           pygame.time.wait(1)
            gameover  = True
            
            




        lBoundary += lBoundarychange
        uBoundary += uBoundarychange
        gamedisplay.fill(black)   
        

        gamedisplay.blit(aimg, (applex, appley))
        

        snakehead = []
        snakehead.append(lBoundary)
        snakehead.append(uBoundary)
        snakelist.append(snakehead)

        
        if len(snakelist) > snakelength:
            del snakelist[0]

        for anypart in snakelist[:-1]:
            if anypart == snakehead:
                gameover = True
        Highscore1(highscore)
        Level2(Level)
        score(sc)
        snake(snakelist, snakesize) 
        pygame.display.update()
        clock.tick(speed)
        if sc > highscore:
            addSpeed -= 0.05
            highscore += 10
            Level +=1
            speed += 1
            
        if sc == highscore:
            message("Level up", red, -20, "large")
            pygame.display.update()
            pygame.mixer.music.load('src/levelup.wav')
            pygame.mixer.music.play(0)
            clock.tick(10)
            pygame.time.wait(66)
            sc += 1
        if lBoundary >= applex and lBoundary <= applex + thickness or lBoundary+ snakesize >= applex and lBoundary + snakesize <= applex + thickness:
            if uBoundary >= appley and uBoundary <= appley + thickness or uBoundary + snakesize >= appley and uBoundary+snakesize <= appley+thickness:
                pygame.mixer.music.load('src/eat.wav')
                pygame.mixer.music.play(0)
                applex,appley = apple()
                snakelength += 1
                sc += 1
                if addSpeed >= 0.0:
                    speed += addSpeed
    pygame.quit()
    quit()

##'''Function to show messages on screen'''
    
def message(msg, color, displace, size):
    
    textsurface , textrect = text(msg, color, size)
    
    textrect.center = (gamewidth/2), (gameheight/2) + displace
    gamedisplay.blit(textsurface, textrect)

## Checking HighScore Of current Level
    
def Highscore1(highscore):
    text1 = medsize.render("HighScore = "+str(highscore), True, white)
    gamedisplay.blit(text1, [600,0])

## Current Level
    
def Level2(speed):
    text2 = medsize.render("Level = "+str(speed),True, white)
    gamedisplay.blit(text2, [300,0])
    
## Pause The Game
    
def pause():
    paused= True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_n:
                    gameloop()

            gamedisplay.fill(black)
            message("PAUSED", red, -100, size="large")
            message("press c to continue, n for a new game or q to quit",white, 40, "large")
            pygame.display.update()
            clock.tick(10)

## Current Score
            
def score(score):
    text = medsize.render("Score: " + str(score), True, white)
    gamedisplay.blit(text, [0,0])
    
## Apples on screen
    
def apple():
    applex = round(random.randrange(0, gamewidth-thickness))
    appley = round(random.randrange(0, gameheight-thickness))
    return applex, appley
applex,appley = apple()


## Our Python ;}

def snake(snakelist, snakesize ):
    if direct == "up":
        head = simg
    if direct == "right":
        head = pygame.transform.rotate(simg, 270)
    if direct == "left":
        head = pygame.transform.rotate(simg, 90)
    if direct == "down":
        head = pygame.transform.rotate(simg, 180)
    gamedisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    for xy in snakelist[:-1]:
        gamedisplay.fill(orange, rect=[xy[0], xy[1], snakesize ,snakesize])

def text(txt, color, size):
    if size == "small":
        textsurface = smallsize.render(txt, True, color)
    elif size == "medium":
        textsurface = medsize.render(txt, True, color)
    elif size == "large":
        textsurface = largesize.render(txt, True, color)
    
    return textsurface, textsurface.get_rect()

## store highest level

def store(Level):
    direc = os.path.dirname(__file__)
    new = "src/donot_change.txt"
    newdirec = os.path.join(direc , new)
    if not os.path.exists("src"):
        os.makedirs("src")
    f = open(newdirec,"w+")
    f.write(str(Level))
    f.close()


gamestart()
gameloop()

