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
    from game_state import Players

    # Create a dictionary to keep track of the count of each card in the deck
    card_counts = {card: game.deck.count(card) for card in game.deck}

    # change this into a tree
    max_card_value = 21 - game.handValue(Players.DEALER)
    favorable_outcomes = sum(count for card, count in card_counts.items()
                             if CalculateHandValue([card]) <= max_card_value)

    total_cards = len(game.deck)
    probability = favorable_outcomes / total_cards
    return probability > 0.5

