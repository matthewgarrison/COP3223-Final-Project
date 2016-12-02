import pygame

from Enemy import Enemy
from Level import Level
from Platform import Platform
from Portal import Portal

class Level_1(Level):
	
	def __init__(self, screen_wdith, screen_height) :		
		# Call the parent constructor.
		super().__init__()

		# The borders of the level.
		self.left_edge = 0
		self.right_edge = 4590
		self.top_edge = -500
		self.bottom_edge = 1000
		# Where the camera stops moving on this level.
		self.shift_left_bound = self.left_edge + (screen_wdith/2)
		self.shift_right_bound = self.right_edge - (screen_wdith/2)
		self.shift_up_bound = self.top_edge + (screen_height/2)
		self.shift_down_bound = self.bottom_edge - (screen_height/2)

		# Where the player starts on this level.
		self.starting_x = 20
		self.starting_y = 212
		self.starting_right = True

		# The portal to the next level.
		self.portal = Portal(4480, -60)
		self.portal_list.add(self.portal)

		# Music for this level.
		self.music = "Assets/Music/Level_1.mp3"		
		
		# 2D array, containing the x and y coordinates and type for each platform.
		platforms = [
			[0, 288, 0],
			[70, 288, 1],
			[140, 288, 1],
			[210, 288, 1],
			[280, 288, 1],
			[350, 288, 1],
			[420, 288, 1],
			[490, 288, 1],
			[560, 288, 1],
			[630, 288, 1],
			[700, 288, 1],
			[770, 288, 2],

			[980, 168, 0],
			[1050, 168, 2],

			[1340, 168, 0],
			[1410, 168, 2],

			[1650, 168, 0],
			[1720, 168, 1],
			[1790, 168, 1],
			[1860, 168, 1],
			[1930, 168, 1],
			[2000, 168, 1],
			[2070, 168, 1],
			[2140, 168, 2],

			[2470, 330, 0],
			[2540, 330, 2],

			[2770, 350, 0],
			[2840, 350, 1],
			[2910, 350, 1],
			[2980, 350, 1],
			[3050, 350, 1],
			[3120, 350, 1],
			[3190, 350, 2],

			[3400, 230, 0],
			[3470, 230, 2],

			[3680, 110, 0],
			[3750, 110, 1],
			[3820, 110, 1],
			[3890, 110, 1],
			[3960, 110, 1],
			[4030, 110, 1],
			[4100, 110, 1],
			[4170, 110, 1],
			[4240, 110, 1],
			[4310, 110, 1],
			[4380, 110, 1],
			[4450, 110, 1],
			[4520, 110, 2]
			]

		# Go through the array above and create the platforms.
		for temp in platforms:
			platform = Platform(temp[0], temp[1], temp[2])
			self.platform_list.add(platform)

		# A 2D array containing the min-x, max-x, and y coordinates and color of each enemy.
		enemies = [
			[1650, 2210, 138, True],
			[2770, 3260, 320, False],
			[3680, 4310, 80, True],
			]

		# Go through the array above and create the enemies.
		for temp in enemies :
			enemy = Enemy(temp[0], temp[1], temp[2], temp[3])
			self.enemy_list.add(enemy)