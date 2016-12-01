import pygame

class Enemy(pygame.sprite.Sprite):

	def_init_(self, x, y, type):
		
		super()._init_()
		
		# Get enemy image and hitbox
		if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame1.png")
		else : self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame1.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		# Controls velocity of the enemy
		self.change_x = 0
		
		# Declares leftmost and rightmost limits of the enemy's patrol, respectively
		self.boundary_left = 0
		self.boundary_right = 0
		
		# Player/level references 
        	self.level = None
       		self.player = None
		
	def update(self):
		self.calc_grav()
		
		# Move left/right
		self.rect.x += self.change_x
		
		# Check to see if patrol limit has been reached
        	cur_pos = self.rect.x - self.level.world_shift
        	# Update enemy for case where leftmost boundary is reached
		if cur_pos < self.boundary_left:
			self.change_x *= -1
			if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame1R.png")
			else: self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame1R.png")
		# Update enemy for case where rightmost boundary is reached
		if cur_pos > self.boundary_right: 
			self.change_x *= -1
			if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame1.png")
			else: self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame1.png")
       		
		# This is so that the enemy doesn't fall through the platform
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# Reset enemy position based on the top/bottom of the object.
			if self.change_y > 0: self.rect.bottom = block.rect.top
			elif self.change_y < 0: self.rect.top = block.rect.bottom
			# Stop enemy's vertical movement.
			self.change_y = 0
			
		
		# Moving Animation
		if self.change_x != 0 and self.change_y == 0 :
			self.move_ani_count += 1
			# Second enemy frame
			if self.move_ani_count == 5 :
				if self.facing_right : 
					if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame2R.png")
					else: self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame2R.png")
				else: 
					if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame2.png")
					else: self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame2.png")
			# Back to first enemy frame. Reset animation count
			elif self.move_ani_count == 10:
				if self.facing_right: 
					if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame1R.png")
					else : self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame1R.png")
				else: 
					if type == 0: self.image = pygame.image.load("Assets/Enemy/BlueSlimeFrame1.png")
					else : self.image = pygame.image.load("Assets/Enemy/RedSlimeFrame1.png")
				self.move_ani_count = 0
				
		# Check if player collides with the enemy
        	hit = pygame.sprite.collide_rect(self, self.player)
        	# Player did collide with enemy
        	if hit:
			# Only declare enemy as dead if the player is swinging 
			if self.is_swinging_sword = True:
				self.change_x = 0
		
		
