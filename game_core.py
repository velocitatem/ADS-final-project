from game_util import CalculateHandValue as CalculateHandValueR
from game_util import GetIdealCards, ProbabilityOfCard
from game_state import GameState
from functools import cache

@cache
def CalculateHandValue(hand : list) -> int: # O(n)
    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Returns:
        int: value of the hand
    This is a simple adapter function that converts the list to a tuple.
    """
    return CalculateHandValueR(tuple(hand))


def DealerAI(game : GameState) -> bool:
    """A Simple algorithm to determine if the dealer should hit or stand.
    Args:
        dealerHand (list): dealer's hand
    Returns:
        bool: True = hit, False = stand
    This algorithm is a card-counter algorithm, based on the predicted probability it will hit or stand.
    """

    # using cached valur
    left = 21 - game.dealerHandValue()
    ideal = GetIdealCards(game.dealerHandValue(), game.deck)
    print(ideal)
    # we need to check the probability of the card
    while ideal != []:
        card = ideal.pop()
        card_probability = ProbabilityOfCard(card[0])
        if card[1] <= left and card_probability > 0:
            print("Dealer hits")
            return True
        else:
            print("Dealer stands")
            return False
