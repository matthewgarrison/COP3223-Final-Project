import pygame
from Background import Background

WHITE = (255, 255, 255)

# A superclass for all levels. Each individual level will be a sub-class of this.
class Level():
 
	def __init__(self, player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		# We make a portal list, even though there's only one portal per level, because it's a lot easier 
		# to draw a SpriteGroup than a single Sprite.
		self.portal_list = pygame.sprite.Group()
		self.player = player
		
		self.background = Background("Assets/Background/sky_big.png", 0, -500)

		# How far this world has been scrolled left/right and up/down. (Because the world moves offscreen, 
 		# we shift in the opposite direction from the player.)
		self.world_shift_x = 0
		self.world_shift_y = 0
 
	# Update everything on this level.
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()
 
 	# Draw everything on this level.
	def draw(self, screen):
		# Draw the background.
		screen.fill(WHITE)
		screen.blit(self.background.image, self.background.rect)
		# Draw all the platforms and enemies.
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
		self.portal_list.draw(screen)
 
 	# Shifts the world left/right and up/down based on the player's movement.
	def shift_world(self, shift_x, shift_y):
		print(shift_x, shift_y, type(shift_x), type(shift_y))
		# Keep track of the shift amount.
		self.world_shift_x -= shift_x
		self.world_shift_y -= shift_y
		# Shift the background.
		self.background.rect.x -= shift_x
		self.background.rect.y -= shift_y
 		
		# Go through all the sprite lists and shift.
		for platform in self.platform_list :
			platform.rect.x -= shift_x
			platform.rect.y -= shift_y
		for enemy in self.enemy_list :
			enemy.rect.x -= shift_x
			enemy.rect.y -= shift_y
		for portal in self.portal_list :
			portal.rect.x -= shift_x
			portal.rect.y -= shift_y