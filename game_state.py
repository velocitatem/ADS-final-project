import enum

import parts
from game_core import CalculateHandValue, DealerAI
from game_util import GenerateCards
from parts import DealCard, ShuffleDeck, DealHand, PrettyPrintCard
import enum


class AIMODE(enum.Enum):
    AGGRESSIVE = 0
    CONSERVATIVE = 1
    NEURAL = 2

class Players(enum.Enum):
    DEALER = 0
    PLAYER = 1


class GameState:

    def __init__(self, mode=AIMODE.AGGRESSIVE):
        self.deck = ShuffleDeck(GenerateCards())
        self.deck_index = self.secondary_deck_representation()
        self.seen_cards = set()
        (self.dealer_hand,
         self.player_hand) = DealHand(self), DealHand(self)
        self.AI_MODE = mode
        print("MODE: ", self.AI_MODE.name)
        self.seen_cards.remove(self.dealer_hand[0])

    def secondary_deck_representation(self):
        # index based representation of the deck
        # each pos has count of cards
        return [4] * 13

    def copy(self):
        game = GameState()
        game.AI_MODE = self.AI_MODE
        game.deck = self.deck.copy()
        game.seen_cards = self.seen_cards.copy()
        return game

    def dealCard(self, player):
        if player == Players.DEALER:
            self.dealer_hand.append(DealCard(self))
        elif player == Players.PLAYER:
            self.player_hand.append(DealCard(self))
        else:
            raise ValueError("Invalid player")

    def _dealerHandValue(self):
        return CalculateHandValue(self.dealer_hand);

    def _playerHandValue(self):
        return CalculateHandValue(self.player_hand)

    def handValue(self, player):
        return self._dealerHandValue() \
            if player == Players.DEALER \
            else self._playerHandValue()

    def prettyPrint(self, show_house_card=True):
        print("Dealer's hand: ")
        for card in self.dealer_hand if show_house_card else self.dealer_hand[1:]:
            PrettyPrintCard(card)
        print()
        print("Player's hand: ")
        for card in self.player_hand:
            PrettyPrintCard(card)
        print()
        print("Dealer's hand value: ", self._dealerHandValue() if show_house_card else "??")
        print("Player's hand value: ", self._playerHandValue())
        print()

    def getPrintMatrix(self):
        return [
            [parts.PrettyPrintCard(card) for card in self.dealer_hand],
            [parts.PrettyPrintCard(card) for card in self.player_hand],
        ]
    def winner(self) -> Players or None:

        """Select the winner. Returns None if there is no winner.
        Returns:
            Players or None: winner
        """
        playerValue = self._playerHandValue()
        dealerValue = self._dealerHandValue()
        if playerValue > 21:
            return Players.DEALER
        elif dealerValue > 21:
            return Players.PLAYER
        elif playerValue > dealerValue:
            return Players.PLAYER
        elif dealerValue > playerValue:
            return Players.DEALER
        else:
            return None

    def isBust(self, player) -> bool:
        return self.handValue(player) > 21

    def isBlackjack(self, player) -> bool:
        return self.handValue(player) == 21

    def isTie(self) -> bool:
        return self._dealerHandValue() == self._playerHandValue()

    def dealerChoice(self) -> bool:
        # use DealerAI
        return DealerAI(self)