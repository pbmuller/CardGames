from card import Card
from deck import Deck, Hand
from go_fish import GoFish

# c = Card(value="ace", suit="spades")
# c2 = Card(value="five", suit="clubs")
# c3 = Card(value="jack", suit="spades")
# c4 = Card(value="ten", suit="spades")

d = Deck()
# d.shuffle()


# testing the equality methods
# print("{}, {}, {}".format(c, c2, c3))
# print()
# print("{} == {}: {}".format(c, c2, c == c2))
# print("{} == {}: {}".format(c2, c3, c2 == c3))
# print("{} == {}: {}".format(c, c3, c == c3))
# print()
# print("{} != {}: {}".format(c, c2, c != c2))
# print("{} != {}: {}".format(c2, c3, c2 != c3))
# print("{} != {}: {}".format(c, c3, c != c3))
# print()
# print("{}.value_equal({}): {}".format(c, c2, c.value_equal(c2)))
# print("{}.value_equal({}): {}".format(c2, c3, c.value_equal(c3)))
# print("{}.value_equal({}): {}".format(c, c3, c.value_equal(c3)))
# print()
# print("{}.suit_equal({}): {}".format(c, c2, c.suit_equal(c2)))
# print("{}.suit_equal({}): {}".format(c2, c3, c2.suit_equal(c3)))
# print("{}.suit_equal({}): {}".format(c, c3, c.suit_equal(c3)))

# print("{} < {}: {}".format(c, c2, c < c2))
# print("{} < {}: {}".format(c2, c3, c2 < c3))
# print("{} < {}: {}".format(c3, c4, c3 < c4))

# hand1, hand2 = d.deal(piles=2, size=5)
# for i, card in enumerate(hand1):
# 	print(i, card)

gf = GoFish()


