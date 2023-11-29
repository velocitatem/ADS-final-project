from game_util import CalculateHandValue as CalculateHandValueR
from game_util import GetIdealCards, ProbabilityOfCard

def CalculateHandValue(hand : list) -> int: # O(n)

    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Returns:
        int: value of the hand
    This is a simple adapter function that converts the list to a tuple.
    """
    return CalculateHandValueR(tuple(hand))


def DealerAI(game) -> bool:

    """A Simple algorithm to determine if the dealer should hit or stand.
    Args:
        game (GameState): game state
    Returns:
        bool: True = hit, False = stand
    This algorithm is a card-counter algorithm, based on the predicted probability it will hit or stand.
    """

    from game_state import Players
    # using cached valur
    left = 21 - game.handValue(Players.DEALER)
    ideal = GetIdealCards(game.handValue(Players.DEALER), game.deck)
    print(ideal)
    # we need to check the probability of the card
    while ideal:
        card = ideal.pop()
        card_probability = ProbabilityOfCard(card[0])
        if card[1] <= left and card_probability > 0:
            print("Dealer hits")
            return True
        else:
            print("Dealer stands")
            return False
