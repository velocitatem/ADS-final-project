"""
ADS Final Project
=================
A black-jack implementation in Python.
Using:
+ Pygame
"""

import pygame
import sys
# import module for typing
from typing import List, Tuple



def CalculateHandValue(hand : list) -> int:
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
        'A': 11,
        'J': 10,
        'Q': 10,
        }
    if hand == []:
        return 0
    if hand[0] in legend:
        return legend[hand[0]] + CalculateHandValue(hand[1:])
    else:
        return int(hand[0]) + CalculateHandValue(hand[1:])


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
