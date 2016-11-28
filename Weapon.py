from enum import Enum

class Weapon :
	Type = Enum("Type", "Melee Ranged")

	def Weapon(self, damageBonus, type) :
		self.damageBonus = damageBonus
		if type = Type.Melee : self.type = Type.Melee
		else : self.type = Type.Ranged
