from Level import Level
from Platform import Platform
from Background import Background

class Level_2(Level):
	
	def __init__(self, player):		
		# Call the parent constructor.
		Level.__init__(self, player)

		self.level_limit = -1000
		
		# Array with type of platform, and x, y location of the platform.
		
		'''level = [[210, 30, 450, 570],
				[210, 30, 850, 420],
				[210, 30, 1000, 520],
				[210, 30, 1120, 280],
				]

		# Go through the array above and add platforms
		for platform in level:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)'''

