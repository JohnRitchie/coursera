# Testing template for the Hand class
from Blackjack import Card, Hand


c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print c1, c2, c3
print type(c1), type(c2), type(c3)

test_hand = Hand()
print test_hand

test_hand.add_card(c1)
print test_hand

test_hand.add_card(c2)
print test_hand

test_hand.add_card(c3)
print test_hand

print type(test_hand)

###################################################
# Output to console
# note that the string representation of a hand will
# vary based on how you implemented the __str__ method

# SA C2 DT
# <class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
# Hand contains
# Hand contains SA
# Hand contains SA C2
# Hand contains SA C2 DT
# <class '__main__.Hand'>