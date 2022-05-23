import sys
import pygame

from pygame.locals import *
from pygame import sprite
from player import *
from enemy import *
from game import *
from floor import *
from item import Item
from shot import Shot
from pygame import mixer
from random import randrange
def main():
    pygame.init()
    surface = pygame.display.set_mode((640,640))
    pygame.display.set_caption("Sample game")

    game = Game("./image/game.jpg")
    
    sound1 =mixer.Sound("./sound/pop.wav")
    sound2 =mixer.Sound("./sound/crunch.wav")


    playerfile =[
        "./image/blue01.png","./image/blue02.png",
        "./image/space.png",

    ]
    player = Player(playerfile, 288, 512)

    enemyfile =[
        "./image/fire01.png","./image/fire02.png",

    ]

    enemylist = []
    enemylist.append(Enemy (enemyfile, 128, 64))
    enemylist.append(Enemy (enemyfile, 256, 64))

    
    shotfile=[
        "./image/shot01.png","./image/shot02.png",

    ]
    shotlist =[]
    shotlist.append(Shot(shotfile, 128, 640))
    shotlist.append(Shot(shotfile, 448, 640))
    #shotlist[0].setimage(1)
    #shotlist[0].setimage(8)
    #shotlist[1].setimage(1)
    #shotlist[1].setimage(8)



    floorfile=[
        "./image/space.png","./image/floor.png",

    ]
    floorlist =[]
    for i in range(8):
        speed = -2 *(i % 2) -2
        floor = Floor(floorfile, 0, 128)
        floor.setimage(1)
        floor.setspeed(speed)
        floorlist.append(floor)
    floor = Floor(floorfile,272, 528)
    floor.setimage(1)
    floorlist.append(floor)

    itemfile = [
        "./image/space.png","./image/coin.png",
    ]
    itemlist =[]
    for i in range(3):
        x = randrange(0, 576, 96)
        y = randrange(128, 448, 96)
        item = Item(itemfile,x,y)
        item.setimage(1)
        itemlist.append(item)



    group = sprite.Group()
    group.add(game)
    group.add(floorlist)
    group.add(enemylist)
    group.add(shotlist)
    group.add(itemlist)
    group.add(player)
    
    player.setfloor(floorlist)

    enemylist[0].setshot(shotlist[0])
    enemylist[1].setshot(shotlist[1])
    play = False
    
    font = pygame.font.SysFont("Verdana", 30, bold = True)

    while(True):
        surface.blit((pygame.image.load("./image/game1.png")),(0,0))
        playtext = font.render("PRESS P KEY TO PLAY GAME",True, "white")
        surface.blit(playtext,(80,320))
       

        if play == True:
            group.update()
            group.draw(surface)
            if game.scene == "PLAY":
                for item in itemlist:
                    if pygame.sprite.collide_rect(player,item):
                        item.setplace(640,640)
                        game.score += 100
                        sound1.play()

                for shot in shotlist:
                    if pygame.sprite.collide_rect(player,shot):
                        shot.setplace(640,640)
                        player.setimage(2)
                        player.setcount(50)
                        game.score -= 50
                        sound2.play()

            scoretext = font.render(f"SCORE :{game.score}",True, "white")
            surface.blit(scoretext,(400,50))

            timetext = font.render(f"TIME:{game.time:5.0f}",True,"white")
            surface.blit(timetext,(32,50))

            if game.scene == "OVER":
                surface.blit((pygame.image.load("./image/game1.png")),(0,0))
                overtext = font.render("GAME OVER",True,"white")
                surface.blit(overtext,(220,240))
                scoretext = font.render(f"SCORE :{game.score}",True, "white")
                surface.blit(scoretext,(220,400))
                if game.score >= 1000:
                    surface.blit((pygame.image.load("./image/game1.png")),(0,0))
                    cleartext = font.render("GAME CLEAR", True, "white")
                    surface.blit(cleartext,(220,240))
                    scoretext = font.render(f"SCORE :{game.score}",True, "white")
                    surface.blit(scoretext,(220,400))


        pygame.display.update()
        pygame.time.wait(25)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and game.scene in ["OVER"]:
                for i in range(8):
                    floorlist[i].rect.y = 128
                player.rect.x = 288
                player.rect.y = 0
                game.setinit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    play = True

if __name__ == "__main__":
    main()
