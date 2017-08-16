from deck import Hand
import random

class Player:
	def __init__(self, name="Player 1", hand=Hand()):
		self.name = name
		self.hand = hand
		self.pairs = 0

	def scored_pair(self):
		self.pairs += 1

	def see_hand(self):
		print("{} Hand".format(self.name))
		for index, card in enumerate(self.hand, start=1):
			print("{}: {}".format(index, card))

	def contains(self, card):
		return card in self.hand

	def add(self, card):
		self.hand.add(card)

	def remove(self, card=None):
		if self.hand.contains(card):
			return True, self.hand.pop(card)
		elif card == None:
			return True, self.hand.pop(random.choice(self.hand))
		else:
			return False, None