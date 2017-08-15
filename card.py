class Card:
	valid_suits = ["hearts", "spades", "clubs", "diamonds"]

	value_to_int = {
		"ace": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7,
		"eight": 8,
		"nine": 9,
		"ten": 10,
		"jack": 10,
		"queen": 10,
		"king": 10
	}

	valid_values = list(value_to_int.keys())

	def __init__(self, suit="hearts", value="ace"):
		if not suit.lower() in Card.valid_suits:
			raise ValueError("Invalid Suit for a playing card")
		if not value.lower() in Card.value_to_int.keys():
			raise ValueError("Invalid value for a playing card")
		self.suit = suit.lower()
		self.value = value.lower()

	def __repr__(self):
		return "{} of {}".format(self.value.capitalize(), self.suit.capitalize())

	def __int__(self):
		return Card.value_to_int[self.value]

	def __add__(self, other):
		return int(self) + other

	def __radd__(self, other):
		return int(self) + other

	def __eq__(self, other):
		if self.value == other.value and self.suit == other.suit:
			return True
		return False

	def __ne__(self, other):
		if self.value != other.value or self.suit != other.suit:
			return True
		return False

	def __lt__(self, other):
		return Card.valid_values.index(self.value) < other

	def __gt__(self, other):
		return Card.valid_values.index(self.value) > other

	def __le__(self, other):
		return Card.valid_values.index(self.value) < other or Card.value_values.index(self.value) == other

	def __ge__(self, other):
		return Card.valid_values.index(self.value) > other or Card.value_values.index(self.value) == other

	def value_equal(self, other):
		if self.value == other.value:
			return True
		return False

	def suit_equal(self, other):
		if self.suit == other.suit:
			return True
		return False
