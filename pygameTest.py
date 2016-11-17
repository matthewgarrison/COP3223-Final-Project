import pygame
from pygame import *

# Global Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()

        # Velocity vectors
        self.xVel = 0
        self.yVel = 0

        # Enemies the player can bump against
        self.level = None

    def update(self):
        # Level Gravity
        self.calc_grav()

        # Horizontal Movement
        self.rect.x += self.xVel

        # Hit check
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If moving right, player can move flush to obstacle
            if self.xVel > 0:
                self.rect.right = block.rect.left
            # If moving left, the opposite occurs
            elif self.xVel < 0:
                self.rect.left = block.rect.right

        # Vertical Movement
        self.rect.y += self.yVel

        # Hit check
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            
            # Reset position based on the top / bottom of the object
            if self.yVel > 0:
                self.rect.bottom = block.rect.top
            elif self.yVel < 0:
                self.rect.top = block.rect.bottom
                
            # Reset vertical movement
            self.yVel = 0
            
    def calc_grav(self):
        if self.yVel == 0:
            self.yVel = 1
        else:
            self.yVel += 0.35

        # See if we are on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.yVel >= 0:
            self.yVel = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # Checks if there is a platform below us
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If we are cleared to jump, jump
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.xVel = -6

    def go_right(self):
        self.xVel = 6

    def stop(self):
        self.xVel = 0

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        
        self.rect = self.image.get)rect()

class Level():

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.world_shift = 0

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):

        screen.fill(BLACK)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
                


def main():
    pygame.init()

        

    
