import enum
from game_core import CalculateHandValue
class GameState():
    def __init__(self):
        self.deck = []
        self.seen_cards = []
        self.dealer_hand = []
        self.player_hand = []
    def dealerHandValue(self):
       return CalculateHandValue(self.dealer_hand);

    def playerHandValue(self):
        return CalculateHandValue(self.player_hand)

