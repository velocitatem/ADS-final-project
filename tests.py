"""
IN this file we will write our tests
"""
from main import CalculateHandValue
import unittest as ut

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


if __name__ == '__main__':
    ut.main()
