from card import Card
from deck import Deck, Hand, CardCollection
from player import Player
import os
import random

class GoFish:

	def __init__(self):
		self.game_deck = Deck()
		self.game_deck.shuffle()

		starter_hand_tuple = self.game_deck.deal(piles=2, size=10)
		self.players = (Player("Human Player", starter_hand_tuple[0]), Player("Computer Player", starter_hand_tuple[1]))
		del starter_hand_tuple

		#This is going to be the index of the player whose turn it is. 
		self.turn = 0

	def clear_screen(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def game_loop(self):
		self.clear_screen()
		print("Hi! We're going to play anice fun game of go fish. It's gonna be you versus the computer!")
		print("To be fair, we are going to let you lesser human go first against this magnificent computer!")

		self.help()
		input("Press Enter to continue")

		playAgain = True
		while playAgain:
			if self.game_over():
				if self.players[0].pairs > self.players[1].pairs:
					print("Congratulations! You win")
				elif self.players[0].pairs == self.players[1].pairs:
					print("Looks like this game was a draw")
				else:
					print("Bummer, the computer won")
				quit = input("Would you like to play again? [Y/n]")
				if quit:
					playAgain = False
				else:
					self.__init__()
			else:
				self.clear_screen()
				self.print_game_state()
				if self.is_human_turn():
					repeat_turn = self.player_turn()
				else:
					repeat_turn = self.computer_turn()
				if repeat_turn == None:
					print("Well, it was fun while it lasted")
					break
				elif not repeat_turn:
					self.next_turn()

	def player_turn(self):
		move = input(">").lower().split()
		if len(move) == 0:
			input("Sorry, but you gotta enter something")
			return True
		if move[0] == "pair":
			if len(move) > 1 and move[1] in Card.valid_values:
				return self.pair_in_hand(move[1])
			else:
				input("You must enter a valid card value")
				return True
		elif move[0] == "fish":
			if len(move) > 1 and move[1] in Card.valid_values:
				return self.fish(move[1])
			else:
				input("You must enter a valid card value")
				return True
		elif move[0] == "help":
			self.help()
			input("Press Enter to continue")
			return True
		elif move[0] == "quit":
			return None
		else:
			input("Sorry, that was an invalid commad")
			return True
		

	def help(self):
		print("""
Rules:

In the high stakes game of Go Fish, the suit of the card doesn't matter. The only thing that does matter is the value of the card.
As you know, there are 13 different values that a card can have, ace, two, three, four, five, six, seven, eight, nine, 10,
jack, queen, and king.

At the start of the game, we're gonna shuffle the deck, and both you and the computer are going to be dealt a hand of 5 cards. Your hand will
be shown to you at the bottom of the screen and it is going to be visible to you through out the game. The game runs out when a player runs out of
cards. The winner is then going to be determined by the whoever has the most pairs.

Wow! These pairs sound super cool and great! I bet you want to know how to get pairs, don't you? Well you have to go fishing to get them!

You will be able to ask your opponent for any value of card, which you also happen to have in your hand. So if you have a five in your hand, you
can ask if your opponent has any fives. To ask for a card value, you simply type in the value that you want to ask for, in this case "five".
You can't ask for values that you don't have, so if the only card that you have in your hand in the five, you can't ask for anything else.

Here is the cool part, your opponent has to answer truthfully, and when you get asked, you have to answer truthfully too! So to get back to the example, 
if you ask for a five, and your opponent has five, they will give you their five, and this counts as a pair for you. If they don't have a five, then you
will draw the top card from the deck. If that card happens to be a five, then you still get the pair! If it's not, then you add it to your hand, and it becomes
the oppenents turn.

If you got a pair somehow, then it stays your turn, and you will be able to ask for another pair.

That was a lot of rules, but here are the main things:
	- fish (card value)
		type this when you want to fish for a card, and remember, the card value must be one that you have in hand. 
		Ex: fish two
	- pair (card value)
		type this when you see that you have a pair of cards in your own hand. So if you see that you have 2 fours, type
		pair four
	- quit
		type this if you want to quit the game early
	- help
		type this if you want to see this wall of text again.
""")

	def next_turn(self):
		self.turn = (self.turn + 1) % 2 

	def game_over(self):
		over = False
		for player in self.players:
			if len(player.hand) == 0:
				over = True
		return over

	def is_human_turn(self):
		return not self.turn

	def _print_score(self):
		print("Score")
		self._print_separators
		print("You | {} pairs".format(self.players[0].pairs))
		self._print_separators()
		print("Computer | {} pairs".format(self.players[1].pairs))

	def _print_hand(self):
		print("Your Hand")
		self._print_separators()
		for card in self.players[0].hand:
			print(card)

	def _print_separators(self):
		print("-" * 30)

	def print_game_state(self):
		self._print_score()
		self._print_separators()
		print()
		self._print_hand()
		self._print_separators()

	def pair_in_hand(self, card_value):
		card_count = 0
		for card in self.players[self.turn].hand:
			card.value == card_value
			card_count += 1
		if card_count > 1:
			self.players[self.turn].scored_pair()
			card_count = 2
			for card in self.players[self.turn].hand:
				if card.value == card_value and card_count > 0:
					self.players[self.turn].hand.remove(card)
					card_count -= 1
			if self.is_human_turn():
				input("Found a pair of {}{}s!".format(card_value, "e" if card_value == "six" else ""))
			else:
				input("The computer found a pair of {}{}s in hand!".format(card_value, "e" if card_value == "six" else ""))
			return True #Do repeat the turn because we found a pair
		else:
			return False #Don't repeat the turn because we didn't find a pair
	
	def fish(self, card_value):
		caller = self.players[self.turn]
		opponent = self.players[(self.turn + 1) % 2]
		caller_has_card = False
		# import pdb; pdb.set_trace()
		for card in caller.hand:
			if card.value == card_value:
				caller_has_card = True
				caller_card = card
		if caller_has_card:
			matched_card = None
			for card in opponent.hand:
				if card.value == card_value:
					matched_card = card
			if matched_card:
				caller.hand.remove(caller_card)
				opponent.hand.remove(matched_card)
				caller.scored_pair()
				if self.is_human_turn():
					input("Your oppenent had a {}".format(matched_card.value))
				else:
					input("The computer asked for a {} and you had one".format(card_value))
				return True
			else:
				drawn_card = self.game_deck.draw()
				if not drawn_card:
					input("There are no more cards in the deck to draw!")
					return False
				elif drawn_card.value == card_value:
					caller.hand.remove(caller_card)
					caller.scored_pair()
					if self.is_human_turn():
						input("You drew a {} from the deck".format(drawn_card.value))
					else:
						input("The computer asked for a {} and drew {} from the deck".format(card_value, drawn_card.value))
					return True
				else:
					caller.hand.append(drawn_card)
					if self.is_human_turn():
						input("Go Fish!")
					else:
						input("The computer asked for a {} and had to go fish".format(card_value))
					return False
		else:
			if self.is_human_turn():
				input("You must enter a card that you have in hand")
			return True #because I want to give them another chance

	def computer_turn(self):
		computer = self.players[1]
		for card in computer.hand:
			for other_card in computer.hand:
				if card == other_card:
					continue
				if card.value == other_card.value:
					return self.pair_in_hand(card.value)
		return self.fish(random.choice(computer.hand).value)


