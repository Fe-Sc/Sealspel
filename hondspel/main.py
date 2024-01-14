import pygame
import math
import sys

import pygame.time

pygame.init()

#scherm
screenwidth = 800
screenheight = 500

#x, y en de positie van de zeehond
x = 0
y = 0
xpos, ypos = 100, 380
ygrav = 0.6
jumpheight = 15
yvel = jumpheight



#clock voor fps
clock = pygame.time.Clock()

#floor en background
background = pygame.image.load('ocean.jpg')
floor = pygame.image.load('oceanfloor.png.png')


#main loop
run = True
display = pygame.display.set_mode((screenwidth, screenheight))

#animation en character en jumping
seal = pygame.transform.scale(pygame.image.load('sealsprite.png'), (140, 80))

sealrect = seal.get_rect(center=(xpos, ypos))
jumping = False

    #sealrect = jumpseal.get_rect(center=(xpos, ypos))
       # display.blit(jumpseal, sealrect)
       #MOET HIER NOG MEE VERDER
       
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()
    clock.tick(60)
    display.blit(background,(-200,-200))
    display.blit(floor, (0,400))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        ypos -= yvel
        yvel -= ygrav
        if yvel < -jumpheight:
            jumping = False
            yvel = jumpheight
        sealrect = seal.get_rect(center=(xpos, ypos))
        display.blit(seal, sealrect)
    else:
        sealrect = seal.get_rect(center=(xpos,ypos))
        display.blit(seal, sealrect)
