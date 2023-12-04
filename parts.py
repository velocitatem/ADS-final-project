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
    # !! we did not learn this in class but having done online research !!
    # it came up as the most efficient way to shuffle a deck

    n = len(deck)
    while n > 1: # O(n)
        n -= 1
        k = random.randint(0, n) # we take some random item j
        deck[k], deck[n] = deck[n], deck[k] # we just swap the last index with the random index
        # where the last index moves closer to the beginning of the list
    return deck


def DealCard(game) -> Tuple[str, int]: # O(1)

    """Deal a card from the deck.
    Args:
        game (GameState): game state
    Returns:
        tuple: card
    """
    # also add to the seen cards
    card = game.deck.popleft() # pop the first card
    dinpos = {"A": 0, "J": 10, "Q": 11, "K": 12}
    if card[0] in dinpos:
        game.deck_index[dinpos[card[0]]] -= 1 # we just decrement the index
    else:
        game.deck_index[int(card[0]) - 1] -= 1
    # make sure we keep track in a set
    game.seen_cards.add(card)
    return card


def DealHand(game) -> List[Tuple[str, int]]: # O(2) ~ O(1)

    """Deal a hand from the deck.
    Args:
        game (GameState): game state
    Returns:
        list: hand
    """
    return [DealCard(game) for _ in range(2)]


def PrettyPrintCard(card: Tuple[str, int]) -> str: # O(1)

    """Pretty print a card.
    Args:
        card (tuple): card
    Returns:
        str: pretty printed card
    """
    # S = S, ♥ = H, ♦ = D, ♣ = C
    symbol = {
        'S': 'Spades', # '♠
        'H': 'Hearts', # '♥
        'D': 'Diamonds', # '♦
        'C': 'Clubs', # '♣
    }
    print(f"{card[0]} of {symbol[card[1]]}")
