import enum

import parts
from game_core import CalculateHandValue, DealerAI
from game_util import GenerateCards
from parts import DealCard, ShuffleDeck, DealHand, PrettyPrintCard
import enum


class Players(enum.Enum):
    DEALER = 0
    PLAYER = 1


class GameState:

    def __init__(self):
        self.deck = ShuffleDeck(GenerateCards())
        self.seen_cards = set()
        (self.dealer_hand,
         self.player_hand) = DealHand(self), DealHand(self)
        self.seen_cards.remove(self.dealer_hand[0])

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

    def prettyPrint(self):
        print("Dealer's hand: ")
        for card in self.dealer_hand:
            PrettyPrintCard(card)
        print()
        print("Player's hand: ")
        for card in self.player_hand:
            PrettyPrintCard(card)
        print()
        print("Dealer's hand value: ", self._dealerHandValue())
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