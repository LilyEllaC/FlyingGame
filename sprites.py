import pygame
import constants as const
#player

class Player(pygame.sprite.Sprite):
    def __init__(self, height, width, x, y, acceleration, airResistance, gravity):
        self.height=height
        self.width=width
        self.x=x
        self.y=y

        #moving stuff
        self.acceleration=acceleration
        self.gravity=gravity
        self.speedV=0
        self.speedH=0
        self.movingL=False
        self.movingR=False
        self.movingU=False
        self.movingD=False
        self.slowDown=airResistance

        #appearances
        image = pygame.image.load("assets/bird.png")
        self.image = pygame.transform.scale(image, (width, height))
        self.upImages=[pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height)), pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height))]
        self.leftImages=[pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height)), pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height))]
        self.rightImages=[pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height)), pygame.transform.scale(pygame.image.load("assets/bird.png"), (width, height))]

        #hitbox
        self.rect = self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    def startMove(self, key):
        #moving down
        self.speedV+=self.gravity

        # deciding movement
        if key==pygame.K_LEFT:
            self.movingL=True
        elif key==pygame.K_RIGHT:
            self.speedH=1
            self.movingR=True
        if key==pygame.K_UP:
            self.movingU=True
        elif key==pygame.K_DOWN:
            self.movingD=True

        
    def move(self):
        #speeding up
        if self.movingL:
            self.speedH-=self.acceleration
        if self.movingR:
            self.speedH+=self.acceleration
        if self.movingU:
            self.speedV-=self.acceleration
        if self.movingD:
            self.speedV+=self.acceleration

        #slowing down
        self.speedH/=self.slowDown
        self.speedV/=self.slowDown


        #moving
        self.x+=self.speedH
        self.y+=self.speedV
        self.rect.x=self.x
        self.rect.y=self.y

    def stopMove(self, key):
        if key==pygame.K_RIGHT:
            self.movingR=False
        if key==pygame.K_LEFT:
            self.movingL=False
        if key==pygame.K_DOWN:
            self.movingD=False
        if key==pygame.K_UP:
            self.movingU=False


    def display(self):
        const.SCREEN.blit(self.image, self.rect)


        