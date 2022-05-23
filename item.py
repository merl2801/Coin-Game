import pygame
from pygame.locals import * 
from pygame import sprite, image, Rect
from random import randint, randrange

class Item(sprite.Sprite):
    def __init__(self, imagelist, x = 0, y= 0, width = 64, height=64):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x,y,width,height)
        self.setimage(0)
        self.settimer()
    
    def settimer(self):
        self.time = randint(5, 9)

    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])

    def setplace(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.time == 3:
            self.setplace(640,640)
        if self.time > 0.025:
            self.time -= 0.025
        else:
            x = randrange(0 ,576, 64)
            y = randrange(128 ,448, 64)
            self.setplace(x, y)
            self.settimer()



