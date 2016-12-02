import pygame

MOVEMENT_SPEED = 4
STARTING_LIVES = 5
STARTING_HEALTH = 5
BLACK_SQUARE = "█"
WHITE_SQAURE = "░"

class Player(pygame.sprite.Sprite):

	def __init__(self, curr_level):
		# Call the superconstructor.
		super().__init__()
 
		# Sets the player's image and hitbox.
		self.image = pygame.image.load("Assets/Player/Right1.png")
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
 
		self.current_level = curr_level
		self.rect.x = self.current_level.starting_x
		self.rect.y = self.current_level.starting_y

		self.lives = STARTING_LIVES
		self.health = STARTING_HEALTH

		# This prevents the player from being damaged multiple times by one hit.
		self.is_damaged = False
		self.damage_count = 0

	def update(self) :
		if self.is_damaged :
			self.damage_count += 1
			if self.damage_count >= 50 :
				self.is_damaged = False
				self.damage_count = 0

		self.calc_grav()
 
		# Move left/right.
		self.rect.x += self.change_x
		# See if that movement caused us to hit anything.
		block_hit_list = pygame.sprite.spritecollide(self, self.current_level.platform_list, False)
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
		block_hit_list = pygame.sprite.spritecollide(self, self.current_level.platform_list, False)
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
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Right2.png")
				else : self.image = pygame.image.load("Assets/Player/Left2.png")
			elif self.move_ani_count == 10:
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Right3.png")
				else : self.image = pygame.image.load("Assets/Player/Left3.png")
			elif self.move_ani_count == 15 :
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Right1.png")
				else : self.image = pygame.image.load("Assets/Player/Left1.png")
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
				if self.facing_right : self.image = pygame.image.load("Assets/Player/Right1.png")
				else : 
					self.image = pygame.image.load("Assets/Player/Left1.png")
					# Now we move the player back to where they were.
					x += 42
				# Get the dimensions of the new sprite, and set the x and y coordinates.
				self.rect = self.image.get_rect()
				self.rect.x = x
				self.rect.y = y
 
 	# Calculate gravity.
	def calc_grav(self):
		if self.change_y == 0 :
			self.change_y = 1
		else:
			self.change_y += .35
 
	def jump(self):
		# We move down two pixels to see if we collide with a a platform. If we do collide, then we 
		# can jump (we need to hit a platform to make sure we're not double jumping in midair).
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.current_level.platform_list, False)
		self.rect.y -= 2
 
		# If it is ok to jump (we collided with at least one platform), set our speed upwards.
		if len(platform_hit_list) > 0:
			self.change_y = -10
 
	def go_left(self):
		self.change_x = -MOVEMENT_SPEED
		self.facing_right = False
		self.image = pygame.image.load("Assets/Player/Left1.png")
 
	def go_right(self):
		self.change_x = MOVEMENT_SPEED
		self.facing_right = True
		self.image = pygame.image.load("Assets/Player/Right1.png")

	def stop(self):
		self.change_x = 0
		self.move_ani_count = 0
		if self.facing_right : self.image = pygame.image.load("Assets/Player/Right1.png")
		else : self.image = pygame.image.load("Assets/Player/Left1.png")

	def swing_sword(self) : 
		self.is_swinging_sword = True
		x = self.rect.x
		y = self.rect.y
		if self.facing_right : self.image = pygame.image.load("Assets/Player/RightSword.png")
		else : 
			self.image = pygame.image.load("Assets/Player/LeftSword.png")
			# Because the sword is 42 pixels long, we have to move the sprite back 42 pixels.
			x -= 42
		# Get the dimensions of the new sprite, and set the x and y coordinates.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def lose_a_life(self, facing_right) :
		self.lives -= 1
		self.health = STARTING_HEALTH
		self.rect.x = self.current_level.starting_x
		self.rect.y = self.current_level.starting_y
		self.facing_right = facing_right
		if facing_right : self.image = self.image = pygame.image.load("Assets/Player/Right1.png")
		else : self.image = self.image = pygame.image.load("Assets/Player/Left1.png")

	def health_to_string(self) :
		s = ""
		for i in range(self.health*2) : s += BLACK_SQUARE
		diff = STARTING_HEALTH - self.health
		for i in range(diff*2) : s += WHITE_SQAURE
		return s