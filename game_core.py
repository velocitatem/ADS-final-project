from game_util import CalculateHandValue as CalculateHandValueR
from game_util import ProbabilityOfCard, ProbabilityOfCardValue
from bigonavigator import O


@O["n"]
def CalculateHandValue(hand : list) -> int:

    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Retu 0.4.6 rns:
        int: value of the hand
    This is a simple adapter function that converts the list to a tuple.
    """
    return CalculateHandValueR(tuple(hand))


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


DEPTH_LIMIT = 5


@O["n!"]
def build_tree(node, deck_index, threshold=21, depth=0):
    """Build the decision tree.
    We map out the possible outcomes of the game.
    Root node is the dealer's hand value.
    |- Children are poss hand values after the dealer hits again
        |- Children's children are poss hand values after the dealer hits again.
            |- ... until the threshold is reached or the depth limit is reached. The threshold is 21
            21 is the maximum anyone could get (in order to win)
    """
    if node.value >= threshold or depth >= DEPTH_LIMIT:
        return
    new_deck_index = deck_index.copy()
    for card_value in range(1, 14): # 1 to 13
        if deck_index[card_value - 1] > 0:
            new_deck_index[card_value - 1] -= 1  # remove the card from the deck index
            if card_value == 1:  # if the card is an Ace
                for ace_value in [1, 11]:
                    # an ace can hold 2 values, 1 or 11 (depending on the hand)
                    # we have to consider both cases
                    new_value = node.value + ace_value  # calculate the new hand value
                    child = Node(new_value)
                    node.children.append(child)
                    build_tree(child, new_deck_index, threshold, depth + 1)
            else:
                new_value = node.value + min(card_value, 10) # we use 10 cuz JKQ are all 10 - the max possible
                child = Node(new_value)
                node.children.append(child)
                build_tree(child, new_deck_index, threshold, depth + 1)


@O["n"]
def find_good_paths(node, path=[]):

    """Find the paths that are "good" (i.e. the dealer should hit).
    Args:
        node (Node): the node to start from
        path (list): the current path
    Returns:
        list: list of pathDEALERs
    """
    if node.value > 21: # we have not busted but its the end of the path (we have to stop)
        return []
    if not node.children:
        return [path] # recursive base case
    paths = []
    for child in node.children:
        # build the paths
        paths += find_good_paths(child, path + [child.value])
    return paths # return the paths


@O["n"]
def all_paths_count(node, path=[]):

    """
    Returns the number of all paths in the tree.
    The same as the method above but we just count the paths instead of returning them.
    ALL not just good paths
    """
    if not node.children:
        return 1
    count = 0
    for child in node.children:
        count += all_paths_count(child, path + [child.value])
    return count


@O["n!"]
def DealerAI(game):

    """The dealer's AI.
    Args:
        game (GameState): the game state
    Returns:
        bool: True if the dealer should hit, False if the dealer should stand
    """
    from game_state import Players, AIMODE # dep loop
    if game.AI_MODE == AIMODE.NEURAL: # load a .dot file
        pass

    dealer_hand_value = game.handValue(Players.DEALER) # Get the dealer's hand value
    root = Node(dealer_hand_value)
    # Build the decision tree
    build_tree(root, game.deck_index)

    paths = find_good_paths(root) # Find the good paths
    paths = [path for path in paths if len(path) > 0]
    # this was where we had a 1 instead of a 0
    # issue was we were forgetting paths that could win in 1 HIT

    if len(paths) == 0:
        return False
    pthlen = all_paths_count(root)
    good_paths_ratio = len(paths) / pthlen
    # used for further probability eval with conservative mode

    # highest card we need to hit first
    highest_card = max([path[0] for path in paths])
    # we get the highest card that we need to hit
    highest_card = abs(dealer_hand_value - highest_card) # since its just the state representation of the hand value
    # we diff the stuff
    next_card_odds = ProbabilityOfCardValue(highest_card, game)
    print(next_card_odds)
    # then we look at the probability of getting that card or lower
    # this gives use the odds that we won't bust so to say
    if game.AI_MODE == AIMODE.CONSERVATIVE:
        return next_card_odds > 0.6 and good_paths_ratio > 0.5
        # here we want the dealer to always play it very safe
    elif game.AI_MODE == AIMODE.AGGRESSIVE:
        return next_card_odds > 0.5
        # here we want the dealer to play it safe but not too safe
    else:
        raise ValueError("Invalid AI mode")
