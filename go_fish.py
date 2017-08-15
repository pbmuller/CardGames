from card import Card
from deck import Deck, Hand, CardCollection

class GoFish:

	def __init__(self):
		self.game_deck = Deck()
		self.game_deck.shuffle()
		self.player_pairs = 0
		self.computer_pairs = 0

		starter_hand_tuple = self.game_deck.deal(piles=2, size=5)
		self.players = (PLayer("Human Player", starter_hand_tuple[0]), Player("Computer Player", starter_hand_tuple[1]))
		del starter_hand_tuple

		#This is going to be the index of the player whose turn it is. 
		self.turn = 0


	def game_loop():
		print("Hi! We're going to play anice fun game of go fish. It's gonna be you versus the computer!")
		print("To be fair, we are going to let you lesser human go first against this magnificent computer!")


	def help(self):
		print("""
Rules:
""")


	#def guess(self, card):