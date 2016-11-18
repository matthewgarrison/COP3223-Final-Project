class MovingPlatform(Platform):
    
    def __init__(self, sprite_sheet_data):
 
        super().__init__(sprite_sheet_data)

        # Controls horizontal velocity of the platform
        self.change_x = 0
        # Controls vertical velocity of the platform
        self.change_y = 0

        # Upper limit of a vertical moving platform
        self.boundary_top = 0
        # Lower limit of a vertical moving platform
        self.boundary_bottom = 0
        # Leftmost limit of a horizontal moving platform
        self.boundary_left = 0
        # Rightmost limit of a horizontal moving platform
        self.boundary_right = 0
 
        self.level = None
        self.player = None
 
    def update(self):
 
        # Move left/right for a horizontal moving platform
        self.rect.x += self.change_x
 
        # Check if player collides with the platform
        hit = pygame.sprite.collide_rect(self, self.player)
        # Player did collide with platform
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


''' Custom Horizontal moving platform example

    # Create platform with its (width,height)
    block = MovingPlatform(80,40)

    # Set platform's current location 
    block.rect.x = 1020
    block.rect.y = 260

    # Set platform's boundaries
    block.boundary_left = 1020
    block.boundary_right = 1260

    # Set platform's velocity
    block.change_x = 1

    # Reference to player/level
    block.player = self.player
    block.level = self
    self.platform_list.add(block)     '''

''' Custom Vertical moving platform: only changes are that
    it uses vertical boundaries/velocity instead of horizontal     '''


    

    
    

