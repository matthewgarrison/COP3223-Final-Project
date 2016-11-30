import pygame

# Platforms have a width and height of 70. Type 0 is a left brick, type 1 is a middle brick, and type 2
# is a right brick.

class Platform(pygame.sprite.Sprite):

	def __init__(self, x, y, type) :
		# Call the superconstructor.
		super().__init__()

		# Set the platform's image and hitbox.
		if type == 0 : self.image = pygame.image.load("Assets/Tile/tile_left.png")
		elif type == 1 : self.image = pygame.image.load("Assets/Tile/tile_middle.png")
		else : self.image = pygame.image.load("Assets/Tile/tile_right.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
