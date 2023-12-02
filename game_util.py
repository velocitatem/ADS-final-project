from functools import lru_cache
from typing import Tuple
import heapq


@lru_cache(maxsize=128)
def CalculateHandValue(hand : tuple) -> int: # O(n) - no loops just recursion over the list

    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Returns:
        int: value of the hand
    Process:
    """
    legend = {
        'A': lambda x: 11 if x + 11 <= 21 else 1, # we need to see if we should use a soft ace or a hard ace
        # gotta love lambda functions :)
        'J': 10,
        'Q': 10,
        'K': 10,
    }
    if hand == ():
        return 0
    if hand[0][0] in legend:
        handFilter = legend[hand[0][0]]
        if callable(handFilter): # check callable for A
            # pylint: disable=line-too-long
            return handFilter(CalculateHandValue(hand[1:])) + CalculateHandValue(hand[1:])
        else:
            return handFilter + CalculateHandValue(hand[1:])
    else:
        return hand[0][0] + CalculateHandValue(hand[1:])


def GetIdealCards(handValue : int, deck : list):
    if deck == [] or deck is None: return []

    heap = []
    for card_index, card in enumerate(deck): # better
        card_diff = abs(handValue - CalculateHandValue([card]))

        if len(heap) < 3 or card_diff < heap[0][1]:
            if len(heap) == 3:
                heapq.heappop(heap)
            # TODO
            heapq.heappush(heap, (card_diff, card_index))

    return [(deck[i[1]], i[0]) for i in heap]

def ProbabilityOfCard(card: Tuple[str, int], game) -> float:

    """Calculate the probability of a cards value (ignore suit) for non seen cards.
    Args:
        card (tuple): card
    Returns:
        float: probability of the card
    """
    # check if the card is in the seen cards
    if card in game.seen_cards:
        return 0
    # get the number of cards in the deck
    # TODO count cards in deck with value of card
    return game.deck.count(card) / len(game.deck)


def GenerateCards() -> list:

    """Generates a list of cards.
    Returns:
        list: list of cards
    """
    # this is an array, but we use it as a queue
    return [(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in range(2, 11)] + [(value, suit) for suit in
                                                                                  ['S', 'H', 'D', 'C'] for value in
                                                                                  ['J', 'Q', 'K', 'A']]