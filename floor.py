from os import supports_effective_ids
import pygame # pygame のモジュール
from pygame.locals import * # pygame で定義済みの定数
from pygame import sprite, image, Rect
from random import choice # 任意の要素を選択する

class Floor(sprite.Sprite):

    def __init__(self, imagelist, x = 0, y = 0, width = 96, height = 32):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x, y, width, height)
        self.setimage(0)
        self.setspeed(0)

    def setimage(self, num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])

    def setspeed(self, speed):
        self.speed = speed
        

    def update(self):
        if self.speed == 0:
            return
        
        x = [ 16, 144, 400, 528]
        y = [640, 720, 800, 880, 960]
        if self.speed < 0 and self.rect.y == 128:
            self.rect.x = choice(x)
            self.rect.y = choice(y)
        self.rect.move_ip(0, self.speed)
        