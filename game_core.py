from game_util import CalculateHandValue as CalculateHandValueR
from game_util import GetIdealCards, ProbabilityOfCard, ProbabilityOfCardValue

def CalculateHandValue(hand : list) -> int: # O(n)

    """Calculate the value of the hand.
    Args:
        hand (list): list of cards [where a card is a tuple of (suit, value)]
    Returns:
        int: value of the hand
    This is a simple adapter function that converts the list to a tuple.
    """
    return CalculateHandValueR(tuple(hand))



class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree(node, deck_index, threshold=17):
    """Build the decision tree.
    We map out the possible outcomes of the game.
    """
    if node.value >= threshold or node.value > 21:
        return
    for card_value in range(1, 14):
        if deck_index[card_value - 1] > 0:
            new_deck_index = deck_index.copy()
            new_deck_index[card_value - 1] -= 1  # remove the card from the deck index
            if card_value == 1:  # if the card is an Ace
                for ace_value in [1, 11]:
                    new_value = node.value + ace_value  # calculate the new hand value
                    child = Node(new_value)
                    node.children.append(child)
                    build_tree(child, new_deck_index, threshold)
            else:
                new_value = node.value + min(card_value, 10)  # calculate the new hand value
                child = Node(new_value)
                node.children.append(child)
                build_tree(child, new_deck_index, threshold)



def find_good_paths(node, path=[]):
    if node.value > 21:
        return []
    if not node.children:
        return [path]
    paths = []
    for child in node.children:
        paths += find_good_paths(child, path + [child.value])
    return paths

def all_paths_count(node, path=[]):
    if not node.children:
        return 1
    count = 0
    for child in node.children:
        count += all_paths_count(child, path + [child.value])
    return count


def DealerAI(game):
    from game_state import Players, AIMODE # dep loop
    if game.AI_MODE == AIMODE.NEURAL:
        # load a .dot file
        pass


    # Get the dealer's hand value
    dealer_hand_value = game.handValue(Players.DEALER)

    # Build the decision tree
    root = Node(dealer_hand_value)
    build_tree(root, game.deck_index)


    paths = find_good_paths(root)
    paths = [path for path in paths if len(path) > 1]
    if len(paths) == 0:
        return False
    pthlen = all_paths_count(root)
    good_paths_ratio = len(paths) / pthlen

    # now just gotta get the odds of next card falling into the good paths
    next_card_odds = 0
    for path in paths:
        next_card_odds += ProbabilityOfCardValue(abs(dealer_hand_value - path[0]), game)

    next_card_odds /= len(paths)

    hit = (next_card_odds * good_paths_ratio) > 0.4
    if game.AI_MODE == AIMODE.CONSERVATIVE:
        return next_card_odds > 0.4 and good_paths_ratio > 0.5
    elif game.AI_MODE == AIMODE.AGGRESSIVE:
        return next_card_odds > 0.5
    else:
        raise ValueError("Invalid AI mode")

