import pygame
import time
import random

pygame.init()

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
brightGreen=(0,190,0)
brightRed=(190,0,0)

img=pygame.image.load("racecar.png")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    pygame.display.update()

    time.sleep(2)

   # gameLoop()

def crashed():
    message_display("Crashed")
    
def thing(x,y,h,w):
    pygame.draw.rect(gameDisplay,red,[x,y,w,h])
def gameIntro():
    intro=True
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_display("RaceUP 24*7")

        mouse=pygame.mouse.get_pos()

        if 150<mouse[0]<150+100 and 450<mouse[1]<450+50:
            pygame.draw.rect(gameDisplay, brightGreen,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay,green,(550,450,100,50))
        
        pygame.display.update()
        clock.tick(15)
    
def gameLoop():
    imgPos_x=(display_width * 0.45)
    imgPos_y=(display_height * 0.8)
    carWidth=73
    x=0
    thingX=200
    thingY=50
    thingH=80
    thingW=80
    thingS=7

    gameExit=False

    while not gameExit:
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x=-10
                if event.key==pygame.K_RIGHT:
                    x=10

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
            thingX=random.randrange(0,display_width-thingW)
            thingW+=2

        gameDisplay.fill(white)
        thing(thingX,thingY,thingH,thingW)
        thingY+=thingS
        

        gameDisplay.blit(img,(imgPos_x,imgPos_y))

        
        pygame.display.update()
        clock.tick(30)


gameIntro()
pygame.quit()
quit()
