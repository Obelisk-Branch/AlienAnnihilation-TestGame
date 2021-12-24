import pygame
import nltk
import sys
import os
vec = pygame.math.Vector2
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
        self.icon = pygame.transform.scale(self.icon, (50, 50))
        self.wrecked = self.icon.get_rect(center = (20, height - 60))
        self.position = vec(200, 0)
        self.accel = vec(0,0)
        self.velocity = vec(0,0)
        self.speed = 1.0
        self.name = "Player"
        self.lives = 3
        self.gun = False

    def move(self):
        self.acc = vec(0,0)
        keysPressed = pygame.key.get_pressed()
        if keysPressed[K_w]:
            self.acc.y = 0.5
        if keys.Pressed[K_d]:
            self.acc.x = 0.5
        if keys.Pressed[K_s]:
            self.acc.y = -0.5
        if keys.Pressed[K_a]:
            self.acc.x = -0.5

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

displayScreen.blit(PlayerOne.icon, (20, height - 60))
while (1):

    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            sys.exit(0)
    displayScreen.fill((0,0,0))
    displayScreen.blit(PlayerOne.icon, (10, height - 60))

    for entity in entities:
        if not (isinstance(entity, Player)):
            displayScreen.blit(entity.surface, entity.wrecked)
        else:
            displayScreen.blit(PlayerOne.icon, PlayerOne.wrecked)
            PlayerOne.move()

    pygame.display.update()
    clock.tick(60)

