from Level import Level
from Platform import Platform
from Background import Background
from Portal import Portal

class Level_1(Level):
	
	def __init__(self, player, screen_wdith, screen_height):		
		# Call the parent constructor.
		Level.__init__(self, player)

		# The borders of the level.
		self.left_edge = 0
		self.right_edge = 4000
		self.top_edge = -500
		self.bottom_edge = 1000
		# Where the camera stops moving on this level.
		self.shift_left_bound = self.left_edge + (screen_wdith/2)
		self.shift_right_bound = self.right_edge - (screen_wdith/2)
		self.shift_up_bound = self.top_edge + (screen_height/2)
		self.shift_down_bound = self.bottom_edge - (screen_height/2)

		# Where the player starts the level.
		self.start_x = 20
		self.start_y = 212

		# The portal to the next level.
		self.portal = Portal(210, 288)
		self.portal_list.add(self.portal)
		
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

			[900, 288, 0],
			[970, 288, 2],

			[1110, 288, 0],
			[1180, 288, 2],

			[1320, 350, 0],
			[1390, 350, 2],

			[1510, 375, 0],
			[1580, 375, 1],
			[1650, 375, 1],
			[1720, 375, 2],

			[1880, 450, 0],
			[1950, 450, 1],
			[2020, 450, 2],

			[2100, 520, 0],
			[2170, 520, 1],
			[2240, 520, 1],
			[2310, 520, 1],
			[2380, 520, 1],
			[2450, 520, 1],
			[2520, 520, 2],

			[2610, 450, 0],
			[2680, 450, 2],

			[2770, 375, 0],
			[2840, 375, 1],
			[2910, 375, 1],
			[2980, 375, 1],
			[3050, 375, 1],
			[3120, 375, 1],
			[3190, 375, 1],
			[3260, 375, 1],
			[3330, 375, 1],
			[3400, 375, 1],
			[3470, 375, 1],
			[3540, 375, 1],
			[3610, 375, 2]
			]

		# Go through the array above and create the platforms.
		for temp in platforms:
			platform = Platform(temp[0], temp[1], temp[2])
			platform.player = self.player
			#print(block.rect.x, block.rect.y)
			self.platform_list.add(platform)
