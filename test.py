import pygame
import time
import random

pygame.init()
crash_sound = pygame.mixer.Sound('Glass_Crunch.mp3')

# initialization
display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("RaceUP")
clock=pygame.time.Clock()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
brightGreen=(0,200,0)
brightRed=(200,0,0)

pause=False
img=pygame.image.load("racecar.png")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,width,height,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width,height))
    gameDisplay.blit(TextSurf, TextRect)
     
def crashed():
##    pygame.mixer.music.load('Crash.mp3')
##    pygame.mixer.music.play(-1)
    
    message_display("Game Over!",display_width/2,display_height/2,70)
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        button("PlayAgain",150,450,100,50,green,brightGreen,gameLoop)
        button("Quit",550,450,100,50,red,brightRed,quitGame)
        
        pygame.display.update()
        clock.tick(15)   

        

    
def thing(x,y,h,w):
    pygame.draw.rect(gameDisplay,red,[x,y,w,h])

def button(msg,x,y,w,h,ia,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    

    if x<mouse[0]<x+w and y<mouse[1]<y+h:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ia,(x,y,w,h))

    message_display(msg,x+(w/2),y+(h/2),20)
##    largeText = pygame.font.Font('freesansbold.ttf',20)
##    TextSurf, TextRect = text_objects(msg, largeText)
##    TextRect.center = ( (x+(w/2)), (y+(h/2)) )
##    gameDisplay.blit(TextSurf, TextRect)
##   
def quitGame():
    pygame.quit()
    quit()

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def unpaused():
    pygame.mixer.music.unpause()
    global pause
    pause=False
def paused():
    ############
    pygame.mixer.music.pause()
    #############
    
    message_display("Paused",display_width/2,display_height/2,100)
##    largeText = pygame.font.SysFont("comicsansms",115)
##    TextSurf, TextRect = text_objects("Paused", largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Continue",150,450,100,50,green,brightGreen,unpaused)
        button("Quit",550,450,100,50,red,brightRed,quitGame)

        pygame.display.update()
        clock.tick(15)   

def gameIntro():
    pygame.mixer.music.load('Rocking_Chair.mp3')
    pygame.mixer.music.play(-1)
    intro=True
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitGame()
        gameDisplay.fill(white)
        
        message_display("RaceUP",display_width/2,display_height/2,115)
        message_display("Devloped by Deepak",700,550,10)
        
##        largeText = pygame.font.Font('freesansbold.ttf',115)
##        TextSurf, TextRect = text_objects("RaceUP", largeText)
##        TextRect.center = ((display_width/2),(display_height/2))
##        gameDisplay.blit(TextSurf, TextRect)
##
##        largeText = pygame.font.Font('freesansbold.ttf',115)
##        TextSurf, TextRect = text_objects("RaceUP", largeText)
##        TextRect.center = ((display_width/2),(display_height/2))
##        gameDisplay.blit(TextSurf, TextRect)
    
        
        button("GO!",150,450,100,50,green,brightGreen,gameLoop)
        button("Quit",550,450,100,50,red,brightRed,quitGame)
        
        pygame.display.update()
        clock.tick(15)
    
def gameLoop():
    pygame.mixer.music.load('Race_Car.mp3')
    pygame.mixer.music.play(-1)
    global pause
    imgPos_x=(display_width * 0.45)
    imgPos_y=(display_height * 0.8)
    carWidth=73
    x=0
    count=0
    thingX=200
    thingY=50
    thingH=80
    thingW=80
    thingS=15

    gameExit=False

    while not gameExit:
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitGame()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x=-10
                if event.key==pygame.K_RIGHT:
                    x=10
                if event.key==pygame.K_p:
                    pause=True
                    paused()
                    
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x=0

        

        imgPos_x+=x
        

        if imgPos_x>display_width-carWidth or imgPos_x<0:
            crashed()

        if imgPos_y<thingY+thingH:
            if thingX<imgPos_x<thingX+thingW or thingX<imgPos_x+carWidth<thingX+thingW :
                crashed()

        if thingY>display_height:
            thingY=-thingH
            count+=1
            thingX=random.randrange(0,display_width-thingW)
            thingW+=5

        gameDisplay.fill(white)
        thing(thingX,thingY,thingH,thingW)
        thingY+=thingS
        score(count)

        gameDisplay.blit(img,(imgPos_x,imgPos_y))

        
        pygame.display.update()
        clock.tick(30)


gameIntro()
pygame.quit()
quit()
