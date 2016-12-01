import pygame
from Platform import Platform

VELOCITY = 5

class MovingPlatform(Platform):
    
    def __init__(self, type, is_horizontal, min, max, fixed_coor):
 
        super().__init__(min if is_horizontal else fixed_coor, fixed_coor if is_horizontal else min, type)

        # Controls moving platform velocity
		if is_horizontal:
			self.change_x = VELOCITY
		else:
			self.change_y = VELOCITY
		
		# Sets limits for horizontal moving platform
		if is_horizontal:
			self.boundary_left = min
			self.boundary_right = max
		
        # Sets limits for vertical moving platform
		else:
			self.boundary_top = min
			self.boundary_bottom = max
        
        # Player/level references 
        self.level = None
        self.player = None
		
    def update(self):
 	
		if is_horizontal:
            # Move left/right for a horizontal moving platform
			self.rect.x += self.change_x
 
            # Check if player collides with the platform
			hit = pygame.sprite.collide_rect(self, self.player)
			if hit:
                # If player is moving right, set right side to left side of item hit
				if self.change_x < 0:
					self.player.rect.right = self.rect.left
				else:
                    # Otherwise if player is moving left, do the opposite.
					self.player.rect.left = self.rect.right
 	     	# Check to see if horizontal boundaries are reached.
			cur_pos = self.rect.x - self.level.world_shift

			if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
				# Boundary is reached. Reverse direction.
				self.change_x *= -1

		else:
			# Move up/down for a vertical moving platform
			self.rect.y += self.change_y
 
			# Check if player collides with the platform
			hit = pygame.sprite.collide_rect(self, self.player)

			# Player did collide with platform
			if hit:

				# Reset player position based on the top/bottom of the object.
				if self.change_y < 0:
					self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
 
			# Check to see if vertical boundaries are reached.
			if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
				# Boundary is reached. Reverse direction.
				self.change_y *= -1
	

'''
    # Adding a custom horizontal moving platform in level
    block = platforms.MovingPlatform(1350,300,1)
    block.boundary_left = 1200
    block.boundary_right = 1500
    block.change_x = 1
    block.player = self.player
    block.level = self
    self.platform_list.add(block)
'''
    

    
    

