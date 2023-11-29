"""ADS Final Project
A black-jack implementation in Python.
Using:
+ Pygame
"""
import pygame
from parts import DealCard, ShuffleDeck, DealHand, PrettyPrintCard
from game_core import CalculateHandValue
from game_state import GameState
deck = None
seen_cards = set()


def winner(playerHand: list, dealerHand: list) -> str:
    """Select the winner.
    Args:
        playerHand (list): player's hand
        dealerHand (list): dealer's hand

    Returns:
        str: winner

    1. If the player's hand is greater than 21, the player busts and automatically loses.
    2. If the dealer's hand is greater than 21, the dealer busts and automatically loses.
    3. If the player's hand is greater than the dealer's hand, the player wins.
    4. If the dealer's hand is greater than the player's hand, the dealer wins.
    5. If the player's hand is equal to the dealer's hand, it is a tie.
    """
    playerValue = CalculateHandValue(playerHand)
    dealerValue = CalculateHandValue(dealerHand)

    if playerValue > 21:
        return 'Dealer'
    elif dealerValue > 21:
        return 'Player'
    elif playerValue > dealerValue:
        return 'Player'
    elif dealerValue > playerValue:
        return 'Dealer'
    else:
        return 'Tie'











def main_cli():

    game = GameState()



    playerHand = DealHand(deck)
    dealerHand = DealHand(deck)
    # remove one of them from the deck
    # one of them has to be face down
    seen_cards.remove(dealerHand[0])

    # this is all from the perspective of the player
    print('Your hand is:')
    for card in playerHand:
        PrettyPrintCard(card)
    print('Value of your hand:', CalculateHandValue(playerHand))

    print('The dealer\'s hand is:')
    PrettyPrintCard(dealerHand[0])
    print('The dealer\'s second card is face down.')


    while True:
        print('Do you want to hit or stand?')
        print('1. Hit')
        print('2. Stand')
        print('3. Quit')
        choice = input('Enter your choice: ')


        if choice == '3':

            break


        if choice == '1':
            playerHand.append(DealCard(deck))
            print('Your hand is:')
            for card in playerHand:
                PrettyPrintCard(card)
            print('Value of your hand:', CalculateHandValue(playerHand))
            if CalculateHandValue(playerHand) > 21:
                print('You busted!')
                break
        elif choice == '2':
            pass
        if DealerAI(dealerHand):
            dealerHand.append(DealCard(deck))
            print('The dealer\'s hand is:')
            for card in dealerHand:
                PrettyPrintCard(card)
            print('Value of the dealer\'s hand:', CalculateHandValue(dealerHand))
            if CalculateHandValue(dealerHand) > 21:
                print('The dealer busted!')
                break

        if CalculateHandValue(playerHand) == 21:
            print('You got a blackjack!')
            break


    print('The winner is:', winner(playerHand, dealerHand))


def CanContinueGame(dealerHand: list, playerHand: list) -> bool:
    """
    Check if the game can continue based on the dealer's and player's hands.

    Args:
        dealerHand (list): The dealer's hand.
        playerHand (list): The player's hand.

    Returns:
        bool: True if the game can continue, False otherwise.
    """
    dealerValue = CalculateHandValue(dealerHand)
    playerValue = CalculateHandValue(playerHand)

    # Game can't continue if either player or dealer has a value > 21 (bust) or exactly 21 (blackjack)
    if playerValue >= 21 or dealerValue >= 21:
        return False

    dealerNeeds = 21 - dealerValue
    playerNeeds = 21 - playerValue

    # find cards that can help the dealer and player win
    dealerIdealCards = ideal_cards(dealerValue)
    playerIdealCards = ideal_cards(playerValue)

    # look at only the card values since that is what matters




    return True


def main():
    pygame.init()
    pygame.display.set_caption('Black Jack')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # create ui elements
    # create a deck
    global deck

    deck = ShuffleDeck([(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in range(2, 11)] + [(value, suit) for suit in ['S', 'H', 'D', 'C'] for value in ['J', 'Q', 'K', 'A']])
    playerHand = DealHand(deck)
    dealerHand = DealHand(deck)
    # remove one of them from the deck
    # one of them has to be face down
    seen_cards.remove(dealerHand[0])
    # Game loop
    running = True
    # follow same structure as main_cli
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




main_cli()
