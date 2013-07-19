from random import randint, random



class Actions(object):
	""" Contains all the methods for a player's action selection
	
		Player can ATTACK an enemy, FLEE from the fight, or CAST a spell
		during a BATTLE
	
	"""
	
	def battle(self, player, monster):
		p_name = player.name
		p_hp = player.hp
		p_mp = player.mp
		m_name = monster.name.capitalize()
		m_hp = monster.hp
		dmg = 0
		
		fighting = True
		
		# Battle ends when player or monster HP falls to or below 0, or when player flees
		while p_hp > 0 and m_hp > 0:
			print("\n\n----------")
			print("%s vs %s" % (p_name, m_name))
			print("%d        %d" % (p_hp, m_hp))
			print()
			print("Commands: ATTACK / CAST / FLEE")
			choice = input("> ")
			
			# Player's choice and then whether or not player hits
			if choice == 'ATTACK' or choice == 'attack':
				p_hit = self.hit('a')
				if p_hit == 0:
					dmg = self.attack('p')
					print("You hit the %s for %d damage." % (m_name, dmg))
					m_hp -= dmg
				elif p_hit == 1:
					print("You missed the %s." % m_name)
			
			elif choice == 'CAST' or choice == 'cast':
				p_hit = self.hit('c')
				if p_hit == 0:
					dmg = self.cast('p')
					print("You blasted the %s for %d damage." % (m_name, dmg))
					m_hp -= dmg
				elif p_hit == 1:
					print("You missed the %s with your spell." % m_name)
			else:
				self.flee()
				break
			
			# Checks to see if monster's HP is less than or equal to 0
			if m_hp <= 0:
				break
			else:
				pass
			
			# Randomly generate monster's attack choice and whether or not it hits
			m_rand_choice = randint(0, 1)
			if m_rand_choice:
				m_hit = self.hit('a')
				if m_hit == 0:
					dmg = self.attack('m')
					print("The %s hit you for %d damage." % (m_name, dmg))
					p_hp -= dmg
				elif m_hit == 1:
					print("You dodged the %s's attack." % m_name)
			else:
				m_hit = self.hit('c')
				if m_hit == 0:
					dmg = self.cast('m')
					print("The %s blasted you with his spell for %d damage." % (m_name, dmg))
					p_hp -= dmg
				elif m_hit == 1:
					print("You evaded the %s's spell." % m_name)
		
		if m_hp <= 0:
			print("You defeated the %s!" % m_name)
			player.hp = p_hp
			return 'win'
		elif p_hp <= 0:
			return 'death'
		else:
			return 'flee'
	
	def hit(self, type):
		""" Determines whether or not an attack hits or misses """
		if type == 'a': # a for attack
			return int(random()*1.2)
		elif type == 'c': # c for cast
			return int(random()*1.05)
		else:
			return None

	def attack(self, mult):
		multiplier = { # p for player, m for monster, b for boss
			'p': 2,
			'm': 1,
			'b': 1.8
		}
		
		for key in multiplier:
			if key == mult:
				damage = multiplier[key]*randint(2, 5) + 5
			else:
				pass
		
		return damage
	
	def flee(self):
		print("You run away.")
	
	def cast(self, mult):
		multiplier = { # p for player, m for monster, b for boss
			'p': 2,
			'm': 1,
			'b': 1.8
		}
		
		for key in multiplier:
			if key == mult:
				damage = multiplier[key]*randint(3, 6) + 5
			else:
				pass
		
		return damage
