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
    Number cards have a value equal to their number, while all the picture cards (Jacks, Queens, and Kings) are worth
    10. Aces can be worth 11 or one, whichever is more beneficial to the person holding the hand. For example, a hand
    with an Ace and an Eight is worth 19 (the Ace is valued at 11, known as a soft Ace). A hand with an Ace, a Four,
    and a Nine is worth 14 (the Ace is valued at one, known as a hard Ace, because if it were valued at 11 the hand
    would bust).
    We are making use of recursion.
    https://entertainment.howstuffworks.com/blackjack2.htm
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

    """This function returns the ideal cards in a heap in order to win the game.
    Args:
        handValue (int): hand value
    Returns:
        list: ideal cards
    An ideal card is a card that will get the player closer to 21 but not over 21.
    WE can do this by getting the absolute value of the difference between the hand value and the card value.
    Then we can get the top 3 cards.
    """
    if deck == [] or deck is None:
        return []

    heap = []
    for card in deck:
        card_index = deck.index(card)
        heapq.heappush(heap, (card_index, abs(handValue - CalculateHandValue([card]))))
    ideal = heapq.nsmallest(3, heap)
    ideal = [(deck[i[0]], i[1]) for i in ideal]

    return ideal


def ProbabilityOfCard(card: Tuple[str, int], game) -> float:

    """Calculate the probability of a card.
    Args:
        card (tuple): card
    Returns:
        float: probability of the card
    """
    # check if the card is in the seen cards
    if card in game.seen_cards:
        return 0
    # check if the card is in the deck
    if card in game.deck:
        return 1 / len(game.deck)
    # if not then return 0


def GenerateCards() -> list:

    """Generates a list of cards.
    Returns:
        list: list of cards
    """
    return [(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in range(2, 11)] + [(value, suit) for suit in
                                                                                  ['S', 'H', 'D', 'C'] for value in
                                                                                  ['J', 'Q', 'K', 'A']]