import pygame

class Portal(pygame.sprite.Sprite):

	def __init__(self, x, y) :
		# Call the superconstructor.
		super().__init__()

		# Set the portal's image and hitbox.
		self.image = pygame.image.load("Assets/portal.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
