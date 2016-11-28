from Level import Level
from Platform import Platform
from Background import Background

LEFT_EDGE = 0
RIGHT_EDGE = 2500
TOP_EDGE = 0
BOTTOM_EDGE = 500

# Create platforms for the level
class Level_1(Level):
	""" Definition for level 2. """
	
	def __init__(self, player):
		""" Create level 1. """
		
		# Call the parent constructor
		Level.__init__(self, player)

		self.level_limit = -1000
		
		# Array with type of platform, and x, y location of the platform.
		level = [[340, 250],
			[410, 250],
			[480, 250],
			[550, 250],
			[620, 250],
			[690, 250],
			[760, 250],

			[830, 250],
			[900, 250],
			[970, 250],
			[1040, 250],
			[1110, 250],
			[1180, 250],
			[1250, 250],

			[900, 320]
			]

		# Go through the array above and add platforms.
		for platform in level:
			block = Platform()
			block.rect.x = platform[0]
			block.rect.y = platform[1]
			block.player = self.player
			self.platform_list.add(block)
