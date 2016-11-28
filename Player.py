import pygame

RED = (255, 0, 0)
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class Player(pygame.sprite.Sprite):
	"""
	This class represents the bar at the bottom that the player controls.
	"""
 
	# -- Methods
	def __init__(self):
		""" Constructor function """
 
		# Call the parent's constructor
		super().__init__()
 
		# Sets the player's image, width, height, and hitbox.
		width = 42
		height = 77
		self.image = pygame.image.load("Assets/Player/Guy1Right.png")
		self.rect = self.image.get_rect()
 
		# Set speed vector of player.
		self.change_x = 0
		self.change_y = 0

		# Initialize movement counter, boolean and direction.
		self.move_count = 0
		self.is_moving = False
		self.facing_right = True
 
		# List of sprites we can bump against.
		self.level = None

	def update(self):
		# Gravity.
		self.calc_grav()
 
		# Move left/right.
		self.rect.x += self.change_x
 
		# See if we hit anything.
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right, set our right side to the left side of the item we hit.
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
 
			# Stop our vertical movement
			self.change_y = 0

		# Animation
		if self.is_moving :
			self.move_count += 1
			if self.move_count == 5 :
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy2Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy2Left.png")
			elif self.move_count == 10:
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy3Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy3Left.png")
			elif self.move_count == 15 :
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy1Left.png")
				self.move_count = 0
 
	def calc_grav(self):
		""" Calculate effect of gravity. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35
 
		# See if we are on the ground.
		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height
 
	def jump(self):
		""" Called when user hits 'jump' button. """
 
		# move down a bit and see if there is a platform below us.
		# Move down 2 pixels because it doesn't work well if we only move down 1
		# when working with a platform moving down.
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
 
		# If it is ok to jump, set our speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.change_y = -10
 
	def go_left(self):
		self.change_x = -MOVEMENT_SPEED
		self.facing_right = False
		self.image = pygame.image.load("Assets/Player/Guy1Left.png")
		self.is_moving = True
 
	def go_right(self):
		self.change_x = MOVEMENT_SPEED
		self.facing_right = True
		self.image = pygame.image.load("Assets/Player/Guy1Right.png")
		self.is_moving = True

	def stop(self):
		self.change_x = 0
		self.move_count = 0
		self.is_moving = False
		if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1Right.png")
		else : self.image = pygame.image.load("Assets/Player/Guy1Left.png")
