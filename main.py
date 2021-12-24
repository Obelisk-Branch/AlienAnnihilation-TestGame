import pygame
import nltk
import sys
import os

# Setting up intial values
width = 1280
height = 720





#Starting up execution and instantiation of objects
pygame.init()
clock = pygame.time.Clock()

displayScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Annihilator")

#Enemy Class
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.icon = pygame.sprite.Sprite
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((30, 130, 213))
        self.wrecked = self.surface.get_rect()

        self.speed = 0.75

class Mushroom(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((60, 40))
        self.surface.fill((0, 0, 244))
        self.wrecked = self.surface.get_rect()

        self.icon = pygame.sprite.Sprite
        self.speed = 0

#Player class
class Player():

    def __init__(self):
        super().__init__()
        #self.surface = pygame.Surface((35, 35))
        #self.surface.fill((128, 65, 0))
        self.icon = pygame.image.load(os.getcwd() + '/sprites/player/playerRun.gif')

        self.wrecked = self.icon.get_rect(center = (20, 360))

        self.speed = 1.0
        self.name = "Player"
        self.lives = 3
        self.gun = False

#Platform class
class Platform():

    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((5, 75))
        self.surface.fill((80, 160, 240))
        self.wrecked = self.surface.get_rect(center=(width/2, height - 10))
        self.icon = pygame.image.load(os.getcwd() + '/sprites/misc/plat1.png')
        self.speed = 0.0
        self.wrecked = self.surface.get_rect()

# Main Control Flow:

#if __name__ == "__main__":


platform1 = Platform()
PlayerOne = Player()
entities = []
entities.append(PlayerOne)
entities.append(platform1)

displayScreen.blit(PlayerOne.icon, (0,0))
while True:

    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            sys.exit(0)
    displayScreen.fill((0,0,0))
    displayScreen.blit(PlayerOne.icon, (0, 0))

    #for entity in entities:
        #displayScreen.blit(entity.surface, entity.wrecked)

    pygame.display.update()
    clock.tick(60)

