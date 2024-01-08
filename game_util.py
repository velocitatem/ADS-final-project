from functools import lru_cache
from typing import Tuple
from bigonavigator import O



@O["n"]
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
    if hand[0][0] in legend: # check if the card is in the legend (i.e. JQKA)
        # we check first hand [0] and then the first element of the tuple [0] (i.e. the value)
        handFilter = legend[hand[0][0]] # get the value of the card
        if callable(handFilter): # check callable for A (i.e. ace)
            # we decide if we use a soft ace or a hard ace 1 or 11
            return handFilter(CalculateHandValue(hand[1:])) + CalculateHandValue(hand[1:])
            # if we can have a soft-ace, we need to add the value of the hand without the ace
        else:
            return handFilter + CalculateHandValue(hand[1:]) # if we have a JQK, we just add the value
    else:
        return hand[0][0] + CalculateHandValue(hand[1:]) # if we have a number, we just add the value and recurse


@O["n"]
def ProbabilityOfCard(card: Tuple[str, int], game) -> float:

    """Calculate the probability of a cards value (ignore suit) for non seen cards.
    Args:
        card (tuple): card
    Returns:
        float: probability of the card
    """
    # check if the card is in the seen cards
    # get the number of cards in the deck
    return game.deck.count(card) / len(game.deck) \
        if card not in game.seen_cards \
    else 0

@O["1"]
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
    # dinpos stands for "deck index number position"
    if value in dinpos:
        value = dinpos[value]
    else:
        value -= 1
    # we have say [4, 4, 4, 4] for the deck index
    # value is index, we have num cards at that index left
    # we just sum over the index (that value or smaller)
    ocos = sum(game.deck_index[:value + 1])
    # ocos stands for "occurences of card of size"
    return ocos / sum(game.deck_index)


@O["1"]
def GenerateCards() -> list: # O(1)

    """Generates a deck which acts as a queue.
    Returns:
        list: list of cards
    """
    # this is an array, but we use it as a queue
    # at first we use an array because we need to shuffle it
    # queue is crated in game_state __init__
    return [(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in range(2, 11)] + [(value, suit) for suit in
                                                                                  ['S', 'H', 'D', 'C'] for value in
                                                                                  ['J', 'Q', 'K', 'A']]
