import pygame
from Player import Player
from Platform import Platform
from Level import Level
from Level_1 import Level_1
from Level_2 import Level_2

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
SHIFT_HORIZONTAL = 120
SHIFT_VERTICAL = 60
SHIFT_RIGHT_BOUND = SCREEN_WIDTH - SHIFT_HORIZONTAL
SHIFT_LEFT_BOUND = SHIFT_HORIZONTAL
SHIFT_UP_BOUND = SCREEN_HEIGHT - SHIFT_VERTICAL
SHIFT_DOWN_BOUND = SHIFT_VERTICAL
 
def main():
	pygame.init()
	
	# Set the height and width of the screen.
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("Garrison-Cunada-Pham")
	
	# Create the player.
	player = Player()

	# Create all the levels.
	level_list = []
	level_list.append(Level_1(player))
	level_list.append(Level_2(player))

	# Set the current level.
	current_level_num = 0
	current_level = level_list[current_level_num]

	active_sprite_list = pygame.sprite.Group()

	# Start the player off.
	player.level = current_level
	player.rect.x = 340
	player.rect.y = 250
	active_sprite_list.add(player)

	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
 
	# Main game loop.
	while not done :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					print("Go left")
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()

		# Update the player.
		active_sprite_list.update()
		
		# Update items in the level.
		current_level.update()
		
		# If the player gets near the right side, shift the world left (-x)
		if player.rect.right > SHIFT_RIGHT_BOUND:
			diff = player.rect.right - SHIFT_RIGHT_BOUND
			player.rect.right = SHIFT_RIGHT_BOUND
			current_level.shift_world(-diff, 0)

		# If the player gets near the left side, shift the world right (+x)
		if player.rect.left < SHIFT_LEFT_BOUND:
			diff = SHIFT_LEFT_BOUND - player.rect.left
			player.rect.left = SHIFT_LEFT_BOUND
			current_level.shift_world(diff, 0)

		# If the player gets near the top, shift the world up (-y)
		if player.rect.top > SHIFT_UP_BOUND:
			diff = player.rect.top - SHIFT_UP_BOUND
			player.rect.top = SHIFT_UP_BOUND
			current_level.shift_world(0, -diff)

		# If the player gets near the bottom, shift the world down (+y)
		if player.rect.bottom < SHIFT_DOWN_BOUND:
			diff = SHIFT_DOWN_BOUND - player.rect.left
			player.rect.bottom = SHIFT_DOWN_BOUND
			current_level.shift_world(0, diff)

		# If the player gets to the end of the level, go to the next level
		'''current_position = player.rect.x + current_level.world_shift
		if current_position < current_level.level_limit :
			player.rect.x = 120
			if current_level_no < len(level_list)-1 :
				current_level_num += 1
				current_level = level_list[current_level_num]
				player.level = current_level'''
		
		# Drawing:
		current_level.draw(screen)
		active_sprite_list.draw(screen)
		
		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		
	# Prevents the game from freezing when you close it.
	pygame.quit()



main()