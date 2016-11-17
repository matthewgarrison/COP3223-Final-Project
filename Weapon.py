from enum import Enum

class Weapon :
	Type = Enum("Type", "Melee Ranged Magic")

	def Weapon(self, damageBonus, type) :
		self.damageBonus = damageBonus

		if type = Type.Melee : self.type = Type.Melee
		elif type = Type.Ranged : self.type = Type.Ranged
		else : self.type = Type.Magic