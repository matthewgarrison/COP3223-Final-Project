class MovingPlatform(Platform):
    
    def __init__(self, x, y, type):
 
        super().__init__(x, y, type)

        # Controls moving platform velocity
        self.change_x = 0
        self.change_y = 0

        # Sets limits for vertical moving platform
        self.boundary_top = 0
        self.boundary_bottom = 0
        
        # Sets limits for horizontal moving platform
        self.boundary_left = 0
        self.boundary_right = 0

        # Player/level references 
        self.level = None
        self.player = None
 
    def update(self):
 
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

        # Check to see if horizontal boundaries are reached.
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            # Boundary is reached. Reverse direction.
            self.change_x *= -1


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
    

    
    

