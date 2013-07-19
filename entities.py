from random import randint

import actions



class Player(object):
	
	actions = actions.Actions()
	
	def __init__(self, name):
		self.name = name
		self.hp = 100
		self.mp = 100
		self.armor = 0
		self.lvl = 0


class Monster(object):
	
	def __init__(self, name):
		self.name = name
		self.hp = self.gen_hp()
	
	def gen_hp(self):
		if self.name == 'dragon':
			return 30
		else:
			return (10 + 2*randint(0, 5))
