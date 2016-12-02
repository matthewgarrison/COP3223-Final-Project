import pygame

from Enemy import Enemy
from Level import Level
from Platform import Platform
from Portal import Portal

class Level_2(Level):
	
	def __init__(self, screen_wdith, screen_height) :		
		# Call the parent constructor.
		super().__init__()

		# The borders of the level.
		self.left_edge = -1500
		self.right_edge = 2500
		self.top_edge = -1800
		self.bottom_edge = 1000
		# Where the camera stops moving on this level.
		self.shift_left_bound = self.left_edge + (screen_wdith/2)
		self.shift_right_bound = self.right_edge - (screen_wdith/2)
		self.shift_up_bound = self.top_edge + (screen_height/2)
		self.shift_down_bound = self.bottom_edge - (screen_height/2)

		# Where the player starts on this level.
		self.starting_x = 429
		self.starting_y = 212
		self.starting_right = False

		# The portal to the next level.
		self.portal = Portal(460, -1430)
		self.portal_list.add(self.portal)

		# Music for this level.
		self.music = "Assets/Music/Level_2.mp3"		
		
		# 2D array, containing the x and y coordinates and type for each platform.
		platforms = [
			[210, 288, 0],
			[280, 288, 1],
			[350, 288, 1],
			[420, 288, 1],
			[490, 288, 1],
			[560, 288, 2],

			[-700, 168, 0],
			[-630, 168, 1],
			[-560, 168, 1],
			[-490, 168, 1],
			[-420, 168, 1],
			[-350, 168, 1],
			[-280, 168, 1],
			[-210, 168, 1],
			[-140, 168, 1],
			[-70, 168, 1],
			[0, 168, 1],
			[70, 168, 2],

			[-910, 28, 0],
			[-840, 28, 2],

			[-680, -108, 0],
			[-610, -108, 1],
			[-540, -108, 1],
			[-470, -108, 1],
			[-400, -108, 1],
			[-330, -108, 1],
			[-260, -108, 1],
			[-190, -108, 1],
			[-120, -108, 2],

			[150, -108, 0],
			[220, -108, 2],

			[490, -108, 0],
			[560, -108, 1],
			[630, -108, 2],

			[910, -108, 0],
			[980, -108, 2],

			[1130, -230, 0],
			[1200, -230, 1],
			[1270, -230, 1],
			[1340, -230, 1],
			[1410, -230, 1],
			[1480, -230, 1],
			[1550, -230, 2],

			[1700, -360, 0],
			[1770, -360, 2],

			[1410, -480, 0],
			[1480, -480, 2],

			[1700, -600, 0],
			[1770, -600, 2],

			[1410, -730, 0],
			[1480, -730, 2],

			[1700, -860, 0],
			[1770, -860, 2],

			[-200, -1000, 0],
			[-130, -1000, 1],
			[-60, -1000, 1],
			[10, -1000, 1],
			[80, -1000, 1],
			[150, -1000, 1],
			[220, -1000, 1],
			[290, -1000, 1],
			[360, -1000, 1],
			[430, -1000, 1],
			[500, -1000, 1],
			[570, -1000, 1],
			[640, -1000, 1],
			[710, -1000, 1],
			[780, -1000, 1],
			[850, -1000, 1],
			[920, -1000, 1],
			[990, -1000, 1],
			[1060, -1000, 1],
			[1130, -1000, 1],
			[1200, -1000, 1],
			[1270, -1000, 1],
			[1340, -1000, 1],
			[1410, -1000, 1],
			[1480, -1000, 2],

			[-490, -1120, 0],
			[-420, -1120, 2],

			[-200, -1260, 0],
			[-130, -1260, 1],
			[-60, -1260, 1],
			[10, -1260, 1],
			[80, -1260, 1],
			[150, -1260, 1],
			[220, -1260, 1],
			[290, -1260, 1],
			[360, -1260, 1],
			[430, -1260, 1],
			[500, -1260, 2]
			]

		# Go through the array above and create the platforms.
		for temp in platforms:
			platform = Platform(temp[0], temp[1], temp[2])
			self.platform_list.add(platform)

		# A 2D array containing the min-x, max-x, and y coordinates and color of each enemy.
		enemies = [
			[-700, -350, 138, False],
			[-350, 140, 138, True],

			[490, 700, -138, False],

			[-680, -50, -138, False],

			[1130, 1620, -260, True],

			[-200, 220, -1030, True],
			[220, 640, -1030, False],
			[640, 1060, -1030, True],
			[1060, 1550, -1030, False],

			[-200, 290, -1290, True]
			]

		# Go through the array above and create the enemies.
		for temp in enemies :
			enemy = Enemy(temp[0], temp[1], temp[2], temp[3])
			self.enemy_list.add(enemy)

