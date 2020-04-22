#!/usr/bin/env python
from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()

        j1 = 1, "Joker"
        j2 = 2, "Joker"
        self.cards.append(j1)
        self.cards.append(j2)
