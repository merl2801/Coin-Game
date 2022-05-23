import pygame 
from pygame.locals import *
from pygame import sprite, image, Rect

class Game(sprite.Sprite):

    def __init__(self, file, x= 0, y= 0, width= 640, height= 640):        
        super().__init__()
        self.image = image.load(file)
        self.rect = Rect(x, y, width, height)
        self.setinit()

    def setinit(self):
        self.score = 0
        self.scene = "PLAY"
        self.before = False
        self.time = 100
    def update(self):
        if self.time > 0:
            self.time -= 0.025
        else:
            self.scene = "OVER"
    

        

    