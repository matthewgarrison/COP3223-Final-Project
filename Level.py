import pygame

from Background import Background

WHITE = (255, 255, 255)

# A superclass for all levels. Each individual level will be a sub-class of this.
class Level():
 
	def __init__(self):
		# Create the SpriteGroups for the platforms, enemies, and portal.
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.damaged_enemy_list = pygame.sprite.Group()
		# We make a portal list, even though there's only one portal per level, because it's a lot easier 
		# to draw a SpriteGroup than a single Sprite.
		self.portal_list = pygame.sprite.Group()
		
		# Set the background.
		self.background = Background("Assets/background.png", -1600, -2000)

		# How far this world has been scrolled left/right and up/down. (Because the world moves offscreen, 
 		# we shift in the opposite direction from the player.)
		self.world_shift_x = 0
		self.world_shift_y = 0
 
	# Update everything on this level.
	def update(self):
		self.platform_list.update()
		# This is used to make the enemies flicker when damaged. (They only draw to the screen when 
		# they are in enemy_list).
		for enemy in self.enemy_list :
			if enemy.is_damaged :
				self.damaged_enemy_list.add(enemy)
				self.enemy_list.remove(enemy)
		for enemy in self.damaged_enemy_list :
			if enemy.damage_timer % 3 == 0 :
				self.enemy_list.add(enemy)
				self.damaged_enemy_list.remove(enemy)
		self.enemy_list.update()
		self.damaged_enemy_list.update()
 
 	# Draw everything on this level.
	def draw(self, screen) :
		# Draw the background.
		screen.fill(WHITE)
		screen.blit(self.background.image, self.background.rect)
		# Draw all the platforms and enemies.
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
		self.portal_list.draw(screen)
 
 	# Shifts the world left/right and up/down based on the player's movement.
	def shift_world(self, shift_x, shift_y):
		# Keep track of the shift amount.
		self.world_shift_x -= shift_x
		self.world_shift_y -= shift_y
		# Shift the background.
		self.background.rect.x -= shift_x
		self.background.rect.y -= shift_y
 		
		# Go through all the sprite lists and shift them.
		for platform in self.platform_list :
			platform.rect.x -= shift_x
			platform.rect.y -= shift_y
		for enemy in self.enemy_list :
			enemy.rect.x -= shift_x
			enemy.rect.y -= shift_y
			enemy.min_x -= shift_x
			enemy.max_x -= shift_x
		for enemy in self.damaged_enemy_list :
			enemy.rect.x -= shift_x
			enemy.rect.y -= shift_y
			enemy.min_x -= shift_x
			enemy.max_x -= shift_x
		for portal in self.portal_list :
			portal.rect.x -= shift_x
			portal.rect.y -= shift_y