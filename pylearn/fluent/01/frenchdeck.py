#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/04/11 17:49:39
# @Author  : che
# @Email   : ch1huizong@gmail.com

import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]  # 计算规则?

    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high):
        print(card)
