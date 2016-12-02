import pygame

STARTING_HEALTH = 3
MOVEMENT_SPEED = 3
BLACK_SQUARE = "█"
WHITE_SQAURE = "▒"

# The sprite is 50x30.

class Enemy(pygame.sprite.Sprite) :
	
	def __init__(self, min_x, max_x, y, is_blue) :
		# Call the superconstructor.
		super().__init__()
 
		# Sets the enemy's image and hitbox.
		if is_blue == True : self.image = pygame.image.load("Assets/Enemy/BlueRight1.png")
		else : self.image = pygame.image.load("Assets/Enemy/RedRight1.png")
		self.rect = self.image.get_rect()

		self.is_blue = is_blue

		self.rect.x  = min_x
		self.rect.y = y
		self.health = STARTING_HEALTH
		self.change_x = MOVEMENT_SPEED

		self.min_x = min_x
		self.max_x = max_x

		# Initialize movement animation counter, boolean and direction.
		self.ani_count = 0
		self.facing_right = True

		# This prevents the enemy from being damaged multiple times by one hit.
		self.is_damaged = False
		self.damage_count = 0

	def update(self) :
		if self.is_damaged :
			self.damage_count += 1
			if self.damage_count >= 50 :
				self.is_damaged = False
				self.damage_count = 0
				
		# Update position, changing direction when you hit the end of the enemy's movement range.
		new_x = self.rect.x + self.change_x
		if  new_x >= self.min_x and new_x <= self.max_x - self.rect.width : self.rect.x = new_x
		else : 
			self.change_x *= -1
			self.facing_right = not self.facing_right

		# Animation.
		self.ani_count += 1
		if self.ani_count == 10 :
			if self.is_blue == True :
				if self.facing_right : self.image = pygame.image.load("Assets/Enemy/BlueRight2.png")
				else : self.image = pygame.image.load("Assets/Enemy/BlueLeft2.png")
			else :
				if self.facing_right : self.image = pygame.image.load("Assets/Enemy/RedRight2.png")
				else : self.image = pygame.image.load("Assets/Enemy/RedLeft2.png")
		elif self.ani_count == 20 :
			if self.is_blue == True :
				if self.facing_right : self.image = pygame.image.load("Assets/Enemy/BlueRight1.png")
				else : self.image = pygame.image.load("Assets/Enemy/BlueLeft1.png")
			else :
				if self.facing_right : self.image = pygame.image.load("Assets/Enemy/RedRight1.png")
				else : self.image = pygame.image.load("Assets/Enemy/RedLeft1.png")
			self.ani_count = 0

	def health_to_string(self) :
		s = ""
		for i in range(self.health*6) : s += BLACK_SQUARE
		diff = STARTING_HEALTH - self.health
		for i in range(diff*6) : s += WHITE_SQAURE
		return s