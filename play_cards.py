#!/usr/bin/env python
# from cardfactory import make_deck, shuffle_deck, draw_card
#
# cards = make_deck()
#
# shuffle_deck(cards)
#
# for i in range(5):
#     print(draw_card(deck))

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Abby")
print(d1)
d1.shuffle()
print(d1.cards)

for i in range(5):
    print(d1.draw())
print()

d2 = CardDeck("Bart")

# not as pythonic:
# print(d1.get_dealer())

print(d1.dealer) # -> CardDeck.dealer(d1)
print(d2.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)

j1 = JokerDeck("Charlie")
j2 = JokerDeck("Delilah")

j2.shuffle()
print(j2.cards)

