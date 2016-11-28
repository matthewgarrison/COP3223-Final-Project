import pygame
from Background import Background

WHITE = (255, 255, 255)

# A superclass for all levels. Each individual level will be a sub-class of this.
class Level():
 
	def __init__(self, player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		
		self.background = Background("Assets/Background/sky.png", [0,0])

		# How far this world has been scrolled left/right
		self.world_shift_x = 0
		self.world_shift_y = 0
 
	# Update everything on this level.
	def update(self):
		""" Update everything in this level."""
		self.platform_list.update()
		self.enemy_list.update()
 
 	#Draw everything on this level.
	def draw(self, screen):
		# Draw the background
		screen.fill(WHITE)
		screen.blit(self.background.image, self.background.rect)
 
		# Draw all the sprite lists that we have
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
 
 	# Shifts th world left/right and up/down based on the player's movement.
	def shift_world(self, shift_x, shift_y):
		# Keep track of the shift amount
		self.world_shift_x -= shift_x
		self.world_shift_y -= shift_y
 
		# Go through all the sprite lists and shift.
		for platform in self.platform_list :
			platform.rect.x -= shift_x
			platform.rect.y -= shift_y
		for enemy in self.enemy_list :
			enemy.rect.x -= shift_x
			enemy.rect.y -= shift_y