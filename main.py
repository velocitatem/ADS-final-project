"""
ADS Final Project
=================
A black-jack implementation in Python.
Using:
+ Pygame
"""
import pygame
import random
import sys
import time
from typing import List, Tuple



def CalculateHandValue(hand : list) -> int: # O(n) - no loops just recursion over the list
    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Returns:
        int: value of the hand
    Process:
    Number cards have a value equal to their number, while all the picture cards (Jacks, Queens, and Kings) are worth 10. Aces can be worth 11 or one, whichever is more beneficial to the person holding the hand. For example, a hand with an Ace and an Eight is worth 19 (the Ace is valued at 11, known as a soft Ace). A hand with an Ace, a Four, and a Nine is worth 14 (the Ace is valued at one, known as a hard Ace, because if it were valued at 11 the hand would bust).
    https://entertainment.howstuffworks.com/blackjack2.htm
    """
    legend = {
        'A': lambda x: 11 if x + 11 <= 21 else 1, # we need to see if we should use a soft ace or a hard ace
        # gotta love lambda functions :)
        'J': 10,
        'Q': 10,
        }
    if hand == []:
        return 0
    if hand[0][0] in legend:
        handFilter = legend[hand[0][0]]
        if callable(handFilter):
            # pylint: disable=line-too-long
            return handFilter(CalculateHandValue(hand[1:])) + CalculateHandValue(hand[1:])
        else:
            return handFilter + CalculateHandValue(hand[1:])
    else:
        return hand[0][0] + CalculateHandValue(hand[1:])

def ShuffleDeck(deck: list) -> list: # O(n)
    """Shuffle the deck.
    Args:
        deck (list): list of cards
    Returns:
        list: shuffled deck
    """
    # this algorithm is called Fisher-Yates shuffle
    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

    n = len(deck)
    while n > 1: # O(n)
        n -= 1
        k = random.randint(0, n) # we take some random item j
        deck[k], deck[n] = deck[n], deck[k] # we just swap the last index with the random index
        # where the last index moves closer to the beginning of the list
    return deck




def main():
    pygame.init()
    pygame.display.set_caption('Black Jack')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
