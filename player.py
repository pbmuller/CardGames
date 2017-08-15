from hand import Hand

class Player:
	def __init__(self, name="Player 1", hand):
		self.name = name
		self.hand = hand
		self.pairs = 0

	def scored_pair(self):
		self.pairs += 1

	def see_hand(self):
		print("{} Hand".format(self.name))
		for index, card in enumerate(self.hand, start=1):
			print("{}: {}".format(index, card))