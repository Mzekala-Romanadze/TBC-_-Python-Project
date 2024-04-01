# This program prints a random card by randomly choosing a suit and rank.
# there are 13 ranks in each of the four suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠).

import random

# Define suit and rank lists
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


def random_card():
    suit = random.randint(0, len(suits) - 1)
    rank = random.randint(0, len(ranks) - 1)
    return ranks[rank] + " of " + suits[suit]


card = random_card()
print(card)
