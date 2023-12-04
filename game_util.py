from functools import lru_cache
from typing import Tuple



@lru_cache(maxsize=128)
def CalculateHandValue(hand : tuple) -> int: # O(n) - no loops just recursion over the list + memoization

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
    return game.deck.count(card) / len(game.deck)

def ProbabilityOfCardValue(value: int, game) -> float: # O(13) # deck indices are constant
    # we just sum over the index (more optimal)

    """Calculate the probability of a cards value (ignore suit) for non seen cards.
    Args:
        card (tuple): card
    Returns:
        float: probability of the card
    """
    # check if the card is in the seen cards
    dinpos = {"A": 0, "J": 10, "Q": 11, "K": 12}
    if value in dinpos:
        value = dinpos[value]
    else:
        value -= 1
    # we have say [4, 4, 4, 4] for the deck index
    # value is index, we have num cards at that index left
    # we just sum over the index (that value or smaller)
    ocos = 0
    for i in range(value + 1):
        ocos += game.deck_index[i]
    return ocos / sum(game.deck_index)






def GenerateCards() -> list: # O(1)

    """Generates a deck which acts as a queue.
    Returns:
        list: list of cards
    """
    # this is an array, but we use it as a queue
    q = [(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in range(2, 11)] + [(value, suit) for suit in
                                                                                  ['S', 'H', 'D', 'C'] for value in
                                                                                  ['J', 'Q', 'K', 'A']]

    return q



