from Level import Level
from Platform import Platform
from Background import Background

class Level_2(Level):
	
	def __init__(self, player, screen_wdith, screen_height):		
		# Call the parent constructor.
		Level.__init__(self, player)

		# The borders of the level.
		self.left_edge = 0
		self.right_edge = 5000
		self.top_edge = 0
		self.bottom_edge = 5000
		
		# Where the camera stops moving on this level.
		self.shift_left_bound = self.left_edge + (screen_wdith/2)
		self.shift_right_bound = self.right_edge - (screen_wdith/2)
		self.shift_up_bound = self.top_edge + (screen_height/2)
		self.shift_down_bound = self.bottom_edge - (screen_height/2)
		
		# Where the player starts the level.
		self.start_x = 2930
		self.start_y = 4430
		
		
		# Array with type of platform, and x, y location of the platform.
		
		platforms = [
			[3140, 4500, 2],
			[3070, 4500, 1],
			[3000, 4500, 1],
			[2930, 4500, 1],
			[2860, 4500, 1],
			[2790, 4500, 0],
		
			[2670, 4430, 2],
			[2600, 4430, 1],
			[2530, 4430, 1],
			[2460, 4430, 1],
			[2390, 4430, 1],
			[2320, 4430, 1],
			[2250, 4430, 0],

			[2110, 4360, 2],
			[2040, 4360, 1],
			[1970, 4360, 0],
			
			[1830, 4290, 2],
			[1760, 4290, 1],
			[1690, 4290, 0],
	
			[1950, 4130, 0],
			[2020, 4130, 1],
			[2090, 4130, 2],
			
			[2230, 4060, 0],
			[2300, 4060, 1],
			[2370, 4060, 1],
			[2440, 4060, 1],
			[2510, 4060, 1],
			[2580, 4060, 1],
			[2650, 4060, 1],
			[2720, 4060, 2],
			
			[2860, 4060, 0],
			[2930, 4060, 1],
			[3000, 4060, 2],

			[3140, 3990, 0],
			[3210, 3990, 1],
			[3280, 3990, 2],
			
			[3420, 3920, 0],
			[3490, 3920, 1],
			[3560, 3920, 1],
			[3630, 3920, 1],
			[3700, 3920, 1],
			[3770, 3920, 2],
		
				]

		# Go through the array above and add platforms
		for temp in platforms:
			platform = Platform(temp[0], temp[1], temp[2])
			platform.player = self.player
			self.platform_list.add(platform)

