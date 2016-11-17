class Player:

	def __init__(self, x, y) :
		self.x = x
		self.y = y
		self.items = []
		self.currWeapon = None
		self.currArmor = None
		# status effects?

	def unequipWeapon(self) :
		self.currWeapon = None

	def equipWeapon(self, weapon) :
		self.currWeapon = weapon
	
	def hasWeaponEquipped(self) :
		return self.currWeapon is None

	def unequipWeapon(self) :
		self.currArmor = None

	def equipWeapon(self, armor) :
		self.armor = armor
	
	def hasWeaponEquipped(self) :
		return self.currArmor is None

player = Player(0, 0)
print(player.x)
print(player.y)
print(player.items)
print(player.currWeapon)
print(player.currArmor)