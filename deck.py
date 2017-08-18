from card import Card
import random


class CardCollection:
	def __init__(self):
		self.cards = []

	def __iter__(self):
		yield from self.cards

	def __len__(self):
		return len(self.cards)

	def add(self, card):
		self.cards.append(card)

	def remove(self, card):
		try:
			self.cards.remove(card)
		except ValueError:
			return False
		else:
			return True

	def sort(self):
		self.cards.sort()

	def shuffle(self):
		self.cards = random.sample(self.cards, len(self))

	def draw(self):
		try:
			card = self.cards.pop(0)
		except IndexError:
			return None
		else:
			return card

class Deck(CardCollection):
	def __init__(self):
		super().__init__()
		for suit in Card.valid_suits:
			for value in Card.valid_values:
				self.cards.append(Card(suit=suit, value=value))

	def deal(self, piles=2, size=1):
		if not len(self):
			return False
		if piles < 1 and piles <= len(self):
			raise ValueError("Piles must be a positive number that is less than or equal to the length of the deck")

		card_piles = []
		for _ in range(piles):
			card_piles.append([])

		while len(card_piles[-1]) < size and len(self):
			for pile in card_piles:
				try:
					pile.append(self.cards.pop(0))
				except IndexError:
					break

		for pile in card_piles:
			pile = Hand.from_card_list(pile)
		return tuple(card_piles)

class EukerDeck(CardCollection):
	pass


class Hand(CardCollection):
	def __init__(self, cards=[]):
		super().__init__()
		self.cards = cards

	def __repr__(self):
		return ", ".join(self.cards)

	@classmethod
	def from_card_list(cls, cards):
		return cls(cards)