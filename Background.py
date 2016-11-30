import pygame

class Background(pygame.sprite.Sprite):
	
	def __init__(self, image_file, x, y):
		# Initialize the sprite.
		super().__init__()
		# Set the background image.
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y