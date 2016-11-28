import pygame

GREEN = (0, 255, 0)

# Platforms have a width and height of 70.

class Platform(pygame.sprite.Sprite):

	def __init__(self):
		# Calls the Sprite constructor.
		super().__init__()

		# Set the platform's image and hitbox.
		self.image = pygame.image.load("Assets/Tile/tile_middle.png")
		self.rect = self.image.get_rect()
