import pygame

from Background import Background
from Level import Level
from Level_1 import Level_1
from Level_2 import Level_2
from Platform import Platform
from Player import Player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (215, 0, 0)

SCREEN_WIDTH = 900
SCREEN_MID_X = SCREEN_WIDTH/2
SCREEN_HEIGHT = 500
SCREEN_MID_Y = SCREEN_HEIGHT/2	

def lose_a_life(player, current_level) :
	# Reset world shift and move the player back to start.
	current_level.shift_world(current_level.world_shift_x, current_level.world_shift_y)
	player.lose_a_life(current_level.starting_right)

def is_on_portal(player, current_level) :
	if player.rect.left >= current_level.portal.rect.left and player.rect.right <= current_level.portal.rect.right and player.rect.top >= current_level.portal.rect.top - 42 and player.rect.bottom <= current_level.portal.rect.bottom :
		return True
	else : return False	

def main():
	pygame.init()
	font_small = pygame.font.SysFont("monospace", 5, True)
	font_medium = pygame.font.SysFont("monospace", 25, True)
	font_large = pygame.font.SysFont("monospace", 175, True)
	
	# Set the height and width of the screen.
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	# Game name.
	pygame.display.set_caption("The Triple-M Platformer")

	# Create both of the levels.
	level_list = []
	level_list.append(Level_1(SCREEN_WIDTH, SCREEN_HEIGHT))
	level_list.append(Level_2(SCREEN_WIDTH, SCREEN_HEIGHT))

	# Set the current level.
	current_level_num = 0
	current_level = level_list[current_level_num]

	# Create the player.
	player = Player(current_level)
	# We make a player list, even though there's only one player, because it's a lot easier 
	# to draw a SpriteGroup than a single Sprite.
	player_sprite_list = pygame.sprite.Group()
	player_sprite_list.add(player)

	# Loop until the user clicks the close button or loses. end_game is 0 if you quit, 1 if you lose, and 
	# 2 if you win.
	done = False
	end_game_state = 0

	is_paused = False
	# This is used to delay changing between paused and unpaused or vice vera because
	# of speed issues.
	can_change_pause = True
	pause_menu = pygame.Surface((700, 200))
	pause_menu.fill(GRAY)

	# Music setttings
	pygame.mixer.init()
	pygame.mixer.music.load(current_level.music)
	pygame.mixer.music.play(-1)

	# Used to manage how fast the screen updates.
	clock = pygame.time.Clock()

	# Main game loop.
	while not done :
		if is_paused : 
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					done = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_p :
					if can_change_pause : is_paused = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_p :
					can_change_pause = True
		else :
			# Process keyboard input.
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					done = True
					
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_p :
						if can_change_pause :is_paused = True
					if event.key == pygame.K_LEFT :
						player.go_left()
					if event.key == pygame.K_RIGHT :
						player.go_right()
					if event.key == pygame.K_UP :
						player.jump()
					if event.key == pygame.K_DOWN and is_on_portal(player, current_level) :
						if current_level_num != len(level_list)-1 :
							# Go to next level.
							current_level_num += 1
							# Reset world shift.
							#current_level.shift_world(current_level.world_shift_x, current_level.world_shift_y)
							current_level = level_list[current_level_num]
							# Reset the player.
							player.current_level = current_level
							player.rect.x = current_level.starting_x
							player.rect.y = current_level.starting_y
							player.facing_right = current_level.starting_right
							if not player.facing_right : player.image = pygame.image.load("Assets/Player/Left1.png")
							# Change the music.
							pygame.mixer.music.load(current_level.music)
							pygame.mixer.music.play(-1)
						else :
							# You win!
							done = True
							end_game_state = 2
					if event.key == pygame.K_SPACE :
						# You can't swing your sowrd if you already are swinging or are moving.
						if not player.is_swinging_sword and player.change_x ==0 and player.change_y == 0 : 
							player.swing_sword()
						
				if event.type == pygame.KEYUP :
					if event.key == pygame.K_LEFT and player.change_x < 0 :
						player.stop()
					if event.key == pygame.K_RIGHT and player.change_x > 0 :
						player.stop()
					if event.key == pygame.K_p :
						can_change_pause = True

			# Update the player.
			player_sprite_list.update()
			# See if the player was hit by an enemy or vice versa.
			enemy_hit_list = pygame.sprite.spritecollide(player,current_level.enemy_list, False)
			for enemy in enemy_hit_list :
				if not player.is_swinging_sword :
				# If the player isn't swinging his sword, then he takes damage.
					if not player.is_damaged :
						player.health -= 1
						player.is_damaged = True
				else :
					# If he is, we have to check which side the enemy hit.
					if (player.facing_right and player.rect.right < enemy.rect.right) or (not player.facing_right and player.rect.left > enemy.rect.left) :
						# We hit the enemy with the sword.
						if not enemy.is_damaged :
							enemy.health -= 1
							enemy.is_damaged = True
							# Remove it from the list of enemies if it dies.
							if enemy.health == 0 :
								current_level.enemy_list.remove(enemy)
					else :
						# The enemy hit out back, not our sword, so we take damage.
						if not player.is_damaged :
							player.health -= 1
							player.is_damaged = True
				
			# Update items in the level.
			current_level.update()

			# Prevents the player from going outside of the level (too far to the right or left).
			if not player.is_swinging_sword : 
				if player.rect.right > current_level.world_shift_x + current_level.right_edge : 
					player.rect.right = current_level.world_shift_x + current_level.right_edge
				if player.rect.left < current_level.world_shift_x + current_level.left_edge : 
					player.rect.left = current_level.world_shift_x + current_level.left_edge

			# If you fall off, reset back to the start and lose a life.
			if player.rect.bottom >= current_level.bottom_edge :
				lose_a_life(player, current_level)

			# Horizontal camera movement.
			# center_x is used to prevent the camera from glitching when the sword is swung.
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
				diff = center_x - SCREEN_MID_X
				player.rect.centerx = SCREEN_MID_X
				current_level.shift_world(diff, 0)
			
			# Vertical camera movement.
			if player.rect.centery > SCREEN_MID_Y and player.rect.centery < current_level.world_shift_y + current_level.shift_down_bound :
				diff = player.rect.centery - SCREEN_MID_Y
				player.rect.centery = SCREEN_MID_Y
				current_level.shift_world(0, diff)
			if player.rect.centery < SCREEN_MID_Y and player.rect.centery > current_level.world_shift_y + current_level.shift_up_bound :
				diff = player.rect.centery - SCREEN_MID_Y
				player.rect.centery = SCREEN_MID_Y
				current_level.shift_world(0, diff)

			# Losing a life (when you run out of health).
			if player.health <= 0 :
				lose_a_life(player, current_level)
			# Losing the game (when you run out of lives).
			if player.lives <= 0 :
				done = True
				end_game_state = 1
			
		# Drawing the level.
		current_level.draw(screen)

		# Writing the enemies' health to the screen
		for enemy in current_level.enemy_list :
			label = font_small.render(enemy.health_to_string(), True, RED)
			screen.blit(label, (enemy.rect.x, enemy.rect.y - 10))

		# Drawing the player.
		if player.is_damaged :
			if is_paused or player.damage_count % 3 == 0 : player_sprite_list.draw(screen)
		else : player_sprite_list.draw(screen)

		# Writing the player's lives and health to the screen.
		label = font_medium.render("Lives: " + str(player.lives), True, BLACK)
		screen.blit(label, (5, 5))
		label = font_medium.render("Health: ", True, BLACK)
		screen.blit(label, (5, 30))
		label = font_medium.render(player.health_to_string(), True, RED)
		screen.blit(label, (125, 30))
		
		# Draw the pause menu.
		if is_paused :
			screen.blit(pause_menu, (100, 150))
			label = font_large.render("Paused", True, WHITE)
			screen.blit(label, (130, 160))
		
		# Limit the game to 60 frames per second.
		clock.tick(60)

		# Move what was drawn to the screen.
		pygame.display.flip()
	
	# Show either the victory or game over screen, then exit.
	if end_game_state == 2 : 
		youwin = Background("Assets/youwin.png", 0, 0)
		pygame.mixer.music.load("Assets/Music/youwin.mp3")
		pygame.mixer.music.play(-1)
		for i in range(500) :
			screen.fill(WHITE)
			screen.blit(youwin.image, youwin.rect)
			pygame.display.flip()
	elif end_game_state == 1 :
		gameover = Background("Assets/gameover.png", 0, 0)
		pygame.mixer.music.load("Assets/Music/gameover.ogg")
		pygame.mixer.music.play(-1)
		for i in range(500) :
			screen.fill(WHITE)
			screen.blit(gameover.image, gameover.rect)
			pygame.display.flip()

	# Prevents the game from freezing when you close it.
	pygame.quit()



main()