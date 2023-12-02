"""
IN this file we will write our tests
"""
from game_core import CalculateHandValue
from parts import ShuffleDeck
from game_core import DealerAI
from game_state import GameState, Players
import unittest as ut
from game_state import AIMODE


class BlackJack(ut.TestCase):

    def test_hand_value(self):
        hand = [('A', 'H'), ('J', 'H')]
        self.assertEqual(CalculateHandValue(hand), 21)
        hand = [('A', 'H'), (8, 'C')]
        self.assertEqual(CalculateHandValue(hand), 19)
        hand = [('A', 'H'), (4, 'C'), (9, 'D')] # there is something called soft ace
        self.assertEqual(CalculateHandValue(hand), 14)
        # what if we have a hand with 2 aces?
        hand = [('A', 'H'), ('A', 'C'), (4, 'D'), (9, 'D')]
        self.assertEqual(CalculateHandValue(hand), 15) # 1 + 1 + 4 + 9 = 15

    def test_random_shuffle(self):
        testDeck = [('A', 'H'), ('A', 'C'), (4, 'D'), (9, 'D'), (8, 'C'), ('J', 'H')]
        decks = [ShuffleDeck(
            testDeck.copy()
        ) for _ in range(3)]
        # test if the decks are different
        self.assertNotEqual(decks[0], decks[1])
        self.assertNotEqual(decks[1], decks[2])
        self.assertNotEqual(decks[0], decks[2])


    def dealer(self, mode):

        missess = 0
        avg_proximity = 0
        busts = 0
        # simulate games, dealer should not bust
        for case in range(100):
            game = GameState(mode=mode)
            # dealt by default
            # play until dealer stands
            # compare dealer choice to reality
            # if dealer stands, dealer should not bust
            k = 0
            while DealerAI(game.copy()):
                print("dealer hit", k)
                k+=1
                game.dealCard(Players.DEALER)
            # see if dealer chould have gone farther
            if game.handValue(Players.DEALER) > 21:
                busts += 1
            next = game.deck[0]
            print(next, game.handValue(Players.DEALER))
            # would the dealer have busted?
            could_have_continued = False
            if game.handValue(Players.DEALER) + CalculateHandValue([next]) > 21:
                could_have_continued = True
            if could_have_continued:
                missess += 1
            avg_proximity += game.handValue(Players.DEALER) - 21
        avg_proximity /= 100
        print(f"missess: {missess}, busts: {busts}, avg proximity: {avg_proximity}")
        return busts, missess, avg_proximity


    def test_ai_dealer_AG(self):
        # Create a game state
        # Set the dealer's hand to a specific value
        busts, missess, avg_proximity = self.dealer(AIMODE.AGGRESSIVE)
        self.assertLessEqual(missess, 80)

    def test_ai_dealer_CO(self):
        busts, missess, avg_proximity = self.dealer(AIMODE.CONSERVATIVE)
        self.assertLessEqual(busts, 10)



if __name__ == '__main__':
    ut.main()
