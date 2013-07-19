from sys import exit
from random import randint

import actions
from entities import *



class Save(object):
	""" Stores the player instance and handles loading, saving, etc """
	def save(self, player):
		self.player = player
	
	def load(self):
		return self.player
	
	def sleep(self):
		self.player.hp = 100
		
		
class Engine(object):
	""" Runs the maps """
	def __init__(self, map_obj):
		self.map = map_obj
	
	def play(self):
		print("\n----------")
		current_map = self.map.first_map()
		
		while True:
			next_map_name = current_map.enter()
			
			print("\n----------")
			print("Location: %s" % next_map_name.capitalize())
			current_map = self.map.get_map(next_map_name)



class Start(Save):
	
	def enter(self):
		print("Hello, adventurer!")
		print("Welcome to our quaint little town of Parrington. My name is Steve. What's your name?")
		name = input("> ")
		
		Save.player = Player(name)
		#super(Start, self).save(Player(name)) Wrong because it uses Save's save function to
		# create a local save in Start
		player = self.load()
		
		print("Hi, %s. There's a village general store just down this road, and on" % player.name)
		print("this street, you will pass by many places to eat if you are hungry. I have to")
		print("recommend trying Amy's Bakery for the best loaves around this area. Anyway,")
		print("you're free to explore. I hope you enjoy your stay!")
		input()
		return 'parrington'

class Parrington(Save):
	
	def enter(self):
		print("Places: INN / OUTSIDE")
		#print("BAKERY / INN / STORE / BLKSMTH / OUTSIDE")
		print("Where would you like to go?")
		go = input("> ")
		
		if go == 'OUTSIDE' or go == 'outside':
			return 'plains'
		elif go == 'INN' or go == 'inn':
			return 'parrington_inn'
		else:
			return 'parrington'

class Plains(Save):
	
	messages = [
		"\"AHH! A MONSTER! Help me!!\"",
		"*Scream*\n\"Help me!\"",
		"\"Hey, you! We need your help!\"",
		"\"Hey! Please, could you help me fend off the monsters attacking my house?\""
	]
	
	def enter(self):
		print(Plains.messages[randint(0, len(Plains.messages) - 1)])
		print("Will you help the farmer? (Y / N)")
		help = input("> ")
		
		while help not in 'Y, y, N, n':
			help = input("> ")
		
		if help == 'Y' or help == 'y':
			print("You pull out your sword and prepare for battle.")
			
			player = self.load()
			goblin = Monster('goblin')
			win = player.actions.battle(player, goblin)
			
			if win:
				print("\n\"Thank you for your help!\"")
				input()
				return 'parrington'
			else:
				return 'death'
			
		elif help == 'N' or help == 'n':
			print("As you leave the farmer to die, you feel like a total faggot.")
			return 'parrington'
		else:
			print("This isn't supposed to happen")
			exit(1)
			
class ParringtonInn(Save):
	
	def enter(self):
		print("Welcome to the Parrington Inn!")
		print("Actions: SLEEP / EXIT")
		choice = input("> ")
		
		if choice == 'SLEEP' or choice == 'sleep':
			self.sleep()
			print("You wake up energized and replenished.")
			return 'parrington'
		elif choice == 'EXIT' or choice == 'exit':
			print("You exit the inn.")
			return 'parrington'
		else:
			return 'parrington'

class CastleRamparts(Save):
	
	def enter(self):
		pass

class Castle(Save):
	
	def enter(self):
		pass

class Dead(Save):
	
	messages = [
		"You have fallen",
		"You have died",
		"You died",
		"You're dead",
		"Dead is thou",
		"Thou art dead",
		"Thy body collapses to the ground. You have died"
	]
	
	def enter(self):
		print(Death.messages[randint(0, len(Death.messages) - 1)])
		exit(0)

class Map(object):
	
	maps = {
		'start': Start(),
		'parrington': Parrington(),
		'parrington_inn': ParringtonInn(),
		'plains': Plains(),
		'castle_ramparts': CastleRamparts(),
		'castle': Castle(),
		'death': Dead()
	}
	
	def __init__(self, start_map):
		self.start_map = start_map
	
	def get_map(self, map_name):
		return Map.maps.get(map_name)
	
	def first_map(self):
		return self.get_map(self.start_map)



the_start = Map('start')
to_start = Engine(the_start)
to_start.play()