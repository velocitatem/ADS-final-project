import random
from typing import Tuple, List
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

def DealCard(deck: list, seen_cards : list) -> Tuple[str, int]: # O(1)
    """Deal a card from the deck.
    Args:
        deck (list): list of cards
    Returns:
        tuple: card
    """
    # also add to the seen cards
    card = deck.pop()
    seen_cards.add(card)
    return card

def DealHand(deck: list) -> List[Tuple[str, int]]: # O(2) ~ O(1)
    """Deal a hand from the deck.
    Args:
        deck (list): list of cards
    Returns:
        list: hand
    """
    return [DealCard(deck) for _ in range(2)]

def PrettyPrintCard(card: Tuple[str, int]) -> str: # O(1)
    """Pretty print a card.
    Args:
        card (tuple): card
    Returns:
        str: pretty printed card
    """
    # S = S, ♥ = H, ♦ = D, ♣ = C
    symbol = {
        'S': '♠',
        'H': '♥',
        'D': '♦',
        'C': '♣',
    }
    # TODO Make a verbose function that gives use the full name of the card
    print(f'{symbol[card[1]]} {card[0]}')
