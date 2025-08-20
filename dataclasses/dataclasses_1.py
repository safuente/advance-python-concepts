from dataclasses import dataclass, field
from typing import List


@dataclass
class DataClassCard:
    rank: str
    suit: str


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [DataClassCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[DataClassCard] = field(default_factory=make_french_deck)


# Example Usage (dataclasses best option for storing data)
# By default, data classes implement a .__repr__() method to provide a nice string representation
# and an .__eq__() method that can do basic object comparisons
card1 = DataClassCard(rank="Ace", suit="Spades")
card2 = DataClassCard(rank="Ace", suit="Spades")
print(card1)  # Output: DataClassCard(rank='Ace', suit='Spades')
print(card1 == card2)  # Output: True (compared by value)
print(card1.rank)  # Output: Ace

queen_of_hearts = DataClassCard('Queen', 'Hearts')
ace_of_spades = DataClassCard('Ace', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

# Print default factory value assigned
deck = Deck()
for card in deck.cards:
    print(card)




