#!/usr/bin/env python
import random

class CardDeck:
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, dealer):  # constructor (AKA initializer)
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self.cards.append(card)



    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, value):  # setter property
        if isinstance(self, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    # @property
    # def spam(self):
    #     return self._whatever
    #
    # @property
    # def ham(self):
    #     return self._ham
    #
    # @ham.setter
    # def ham(self, value):
    #     self._ham = value
