# Testing template for the Card class
from Blackjack import Card


c1 = Card("S", "A")
print c1
print c1.get_suit(), c1.get_rank()
print type(c1)

c2 = Card("C", "2")
print c2
print c2.get_suit(), c2.get_rank()
print type(c2)

c3 = Card("D", "T")
print c3
print c3.get_suit(), c3.get_rank()
print type(c3)

###################################################
# Output to console


# SA
# S A
# <class '__main__.Card'>
# C2
# C 2
# <class '__main__.Card'>
# DT
# D T
# <class '__main__.Card'>