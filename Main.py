import pygame
from Player import Player
from Platform import Platform
from Level import Level
from Level_1 import Level_1
from Level_2 import Level_2

SCREEN_WIDTH = 900
SCREEN_MID_X = SCREEN_WIDTH/2
SCREEN_HEIGHT = 500
SCREEN_MID_Y = SCREEN_HEIGHT/2
SHIFT_HORIZONTAL = 250
SHIFT_VERTICAL = 100
SHIFT_RIGHT_BOUND = SCREEN_WIDTH - SHIFT_HORIZONTAL
SHIFT_LEFT_BOUND = SHIFT_HORIZONTAL
SHIFT_UP_BOUND = SCREEN_HEIGHT - SHIFT_VERTICAL
SHIFT_DOWN_BOUND = SHIFT_VERTICAL

def lose_a_life(player, current_level) :
	player.health = Player.MAX_HEALTH
	player.lives -= 1
	player.x = current_level.start_x
	player.y = current_level.start_y
	# reset world shift

def on_portal(player, current_level) :
	if player.rect.left >= current_level.portal.rect.left and player.rect.right <= current_level.portal.rect.right and player.rect.top >= current_level.portal.rect.top - 42 and player.rect.bottom <= current_level.portal.rect.bottom :
		return True
	else : return False

def main():
	pygame.init()
	
	# Set the height and width of the screen.
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	# Game name.
	pygame.display.set_caption("The Triple-M Platformer")
	
	# Create the player.
	player = Player()

	# Create both of the levels.
	level_list = []
	level_list.append(Level_1(player, SCREEN_WIDTH, SCREEN_HEIGHT))
	level_list.append(Level_2(player))

	# Set the current level.
	current_level_num = 0
	current_level = level_list[current_level_num]

	active_sprite_list = pygame.sprite.Group()

	# Start the player off.
	player.level = current_level
	player.rect.x = current_level.start_x
	player.rect.y = current_level.start_y
	active_sprite_list.add(player)

	# Loop until the user clicks the close button or loses.
	done = False

	# Used to manage how fast the screen updates.
	clock = pygame.time.Clock()
 
	# Main game loop.
	while not done :
		# Process keyboard input.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					player.go_left()
				elif event.key == pygame.K_RIGHT :
					player.go_right()
				elif event.key == pygame.K_UP :
					player.jump()
				elif event.key == pygame.K_DOWN and on_portal(player, current_level) :
					# Go to next level.
					print("Go to next level.")
				elif event.key == pygame.K_SPACE :
					# You can't swing your sowrd if you already are swinging or are moving.
					if not player.is_swinging_sword and player.change_x ==0 and player.change_y == 0 : 
						player.swing_sword()
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0 :
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0 :
					player.stop()

		# Update the player.
		active_sprite_list.update()
		
		# Update items in the level.
		current_level.update()

		# Prevents the player from going outside of the level (too far to the right or left).
		if not player.is_swinging_sword : 
			if player.rect.right > current_level.right_edge : player.rect.right = current_level.right_edge
			if player.rect.left < current_level.left_edge : player.rect.left = current_level.left_edge

		# If you fall off, reset back to the start and lose a life.
		if player.rect.bottom >= current_level.bottom_edge :
			lose_a_life(player, current_level)

		# Horizontal camera movement.
		center_x = player.rect.centerx
		if player.is_swinging_sword :
			if player.facing_right : center_x -= 21
			else : center_x += 21
		# Shift the world right.
		if center_x > SCREEN_MID_X and center_x < current_level.world_shift_x + current_level.shift_right_bound  :
			diff = center_x - SCREEN_MID_X
			player.rect.centerx = SCREEN_MID_X
			current_level.shift_world(diff, 0)
		# Shift the world left.
		if center_x < SCREEN_MID_X and center_x > current_level.world_shift_x + current_level.shift_left_bound :
			print("Shift left")
			diff = center_x - SCREEN_MID_X
			player.rect.centerx = SCREEN_MID_X
			current_level.shift_world(diff, 0)
		
		print(player.rect.centery)
		# Vertical camera movement.
		if player.rect.centery > SCREEN_MID_Y and player.rect.centery < current_level.world_shift_y + current_level.shift_down_bound :
			print("Shift down")
			diff = player.rect.centery - SCREEN_MID_Y
			player.rect.centery = SCREEN_MID_Y
			current_level.shift_world(0, diff)
		if player.rect.centery < SCREEN_MID_Y and player.rect.centery > current_level.world_shift_y + current_level.shift_up_bound :
			print("Shift up")
			diff = player.rect.centery - SCREEN_MID_Y
			player.rect.centery = SCREEN_MID_Y
			current_level.shift_world(0, diff)

		# Losing the game.
		if player.lives <= 0 :
			done = True		
		
		# Drawing:
		current_level.draw(screen)
		active_sprite_list.draw(screen)
		
		# Limit to 60 frames per second.
		clock.tick(60)

		# Move what was drawn to the screen.
		pygame.display.flip()
	
	print("game over")

	# Prevents the game from freezing when you close it.
	pygame.quit()



main()