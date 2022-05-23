import pygame 
from pygame.locals import *
from pygame import sprite, image, Rect
from random import choice,randint

class Enemy(sprite.Sprite):

    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x, y, width, height)
        self.setcount(0)
        self.setimage(0)
        self.setspeed(0)
    
    def setcount(self, count):
        self.count = count
    
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])
    
    def setspeed(self,speed):
        self.speed = speed

    def setshot(self, shot):
        self.shot = shot

    def update(self):

        self.count += 1
        if self.count == 20:
            self.setimage(1)
        if self.count == 40:
            self.setimage(0)
            self.setcount(0)
            speed = [-4,+4]
            self.speed = choice(speed)

            if self.shot.rect.y >= 640 and randint(0,3) == 0:
                self.shot.setplace(self.rect.x, self.rect.y)
                self.shot.setimage(1)
                self.shot.setspeed(8)

        if self.rect.x > 0 and self.speed < 0:        
            self.rect.move_ip(self.speed, 0)
        if self.rect.x < 576 and self.speed > 0:
            self.rect.move_ip(self.speed,0)
