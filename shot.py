import pygame
from pygame.locals import * 
from pygame import sprite, image, Rect

class Shot(sprite.Sprite):
    def __init__(self, imagelist, x = 0, y= 0, width = 64, height=64):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x,y,width,height)
        self.setimage(0)
        self.setspeed(0)
    
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])
    
    def setspeed(self,speed):
        self.speed = speed

    def setplace(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.y < 640:
            self.rect.move_ip(0,self.speed)
        
        
