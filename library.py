import random
import pygame 
import random
import sys
import time
from typing import List, Tuple



hand = [] # empty

def DealCard(deck, hand):
    if len(deck) > 0:  # must see if deck has cards
        card = random.choice(deck)  # choose random from deck
        deck.remove(card)  # take card out of deck
        hand.append(card)  # add new card to the hand
        return card # card
    else:
        print("The card deck is empty.")
        return None
