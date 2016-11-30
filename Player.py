import pygame

MOVEMENT_SPEED = 5
MAX_HEALTH = 30

class Player(pygame.sprite.Sprite):

	def __init__(self):
		# Call the superconstructor.
		super().__init__()
 
		# Sets the player's image and hitbox.
		self.image = pygame.image.load("Assets/Player/Guy1Right.png")
		self.rect = self.image.get_rect()
 
		# Set speed vector of player.
		self.change_x = 0
		self.change_y = 0

		# Initialize movement animation counter, boolean and direction.
		self.move_ani_count = 0
		self.facing_right = True

		# Initialize sword swinging variables.
		self.sword_ani_count = 0
		self.is_swinging_sword = False
 
		# We set this in Main.py. It's used for hitbox collisions.
		self.level = None

		self.lives = 5
		self.health = MAX_HEALTH

	def update(self):
		self.calc_grav()
 
		# Move left/right.
		self.rect.x += self.change_x
		# See if that movement caused us to hit anything.
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0:
				# If we are moving right, set our right side to the left side of the item we hit.
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right

		# Move up/down.
		self.rect.y += self.change_y
		# See if that movement caused us to hit anything.
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			# Stop our vertical movement.
			self.change_y = 0

		# Movement animation.
		if self.change_x != 0 and self.change_y == 0 :
			self.move_ani_count += 1
			if self.move_ani_count == 5 :
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy2Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy2Left.png")
			elif self.move_ani_count == 10:
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy3Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy3Left.png")
			elif self.move_ani_count == 15 :
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1Right.png")
				else : self.image = pygame.image.load("Assets/Player/Guy1Left.png")
				self.move_ani_count = 0

		# Sword animation.
		if self.is_swinging_sword :
			self.sword_ani_count += 1
			if self.sword_ani_count > 10 :
				# Finish the sword animation.
				self.is_swinging_sword = False
				self.sword_ani_count = 0
				x = self.rect.x
				y = self.rect.y
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1Right.png")
				else : 
					self.image = pygame.image.load("Assets/Player/Guy1Left.png")
					# Now we move the player back to where they were.
					x += 42
				# Get the dimensions of the new sprite, and set the x and y coordinates.
				self.rect = self.image.get_rect()
				self.rect.x = x
				self.rect.y = y
 
 	# Calculate gravity.
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = .75
		else:
			self.change_y += .35
 
	def jump(self):
		# We move down two pixels to see if we collide with a a platform. If we do collide, then we 
		# can jump (we need to hit a platform to make sure we're not double jumping in midair).
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
 
		# If it is ok to jump (we collided with at least one platform), set our speed upwards.
		if len(platform_hit_list) > 0:
			self.change_y = -10
 
	def go_left(self):
		self.change_x = -MOVEMENT_SPEED
		self.facing_right = False
		self.image = pygame.image.load("Assets/Player/Guy1Left.png")
 
	def go_right(self):
		self.change_x = MOVEMENT_SPEED
		self.facing_right = True
		self.image = pygame.image.load("Assets/Player/Guy1Right.png")

	def stop(self):
		self.change_x = 0
		self.move_ani_count = 0
		if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1Right.png")
		else : self.image = pygame.image.load("Assets/Player/Guy1Left.png")

	def swing_sword(self) : 
		self.is_swinging_sword = True
		x = self.rect.x
		y = self.rect.y
		if self.facing_right : self.image = pygame.image.load("Assets/Player/Guy1RightSword.png")
		else : 
			self.image = pygame.image.load("Assets/Player/Guy1LeftSword.png")
			# Because the sword is 42 pixels long, we have to move the sprite back 42 pixels.
			x -= 42
		# Get the dimensions of the new sprite, and set the x and y coordinates.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
