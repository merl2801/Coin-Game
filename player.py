import pygame 
from pygame.locals import *
from pygame import sprite, image, Rect

class Player(sprite.Sprite):

    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x, y, width, height)
        
        self.setcount(0)
        self.setimage(0)
    
    def setcount(self, count):
        self.count = count
    
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])

    def setfloor(self, floorlist):
        self.accel = 0
        self.floorlist = floorlist
    
    def landcheck(self):
        for floor in self.floorlist:
            x, y, width = floor.rect.x, floor.rect.y, floor.rect.width
            if x - 32 <= self.rect.x <= x + width - 32:
                if y - 64 <= self.rect.y <= y - 32:
                    self.rect.y = y - 64
                    return True

    def update(self):

        self.count += 1

        if self.count == 20:
            self.setimage(1)
        if self.count in [40, 56, 80]:
            self.setimage(0)
        if self.count in [62,74] :
            self.setimage(2)
        if self.count in [40,80]:
            self.setcount(0)

        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-8, 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(+8, 0)

        if self.landcheck():
            if pressed[K_UP]:
                self.accel = -16
                self.rect.y += self.accel
                
                
            else:
                self.accel = 0
                
        else:
            self.accel += 1
            self.rect.y += self.accel
            if self.rect.y > 640:
                self.rect.y = -10
                self.accel = 0

        
