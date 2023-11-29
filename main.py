"""ADS Final Project
A black-jack implementation in Python.
Using:
+ Pygame
"""
import pygame
from game_state import GameState, Players

def main_cli():

    game = GameState()
    game.prettyPrint()


    turn = Players.PLAYER
    while True:
        # making this relatively branchless
        print(f"{turn.name}'s turn")
        hit = input("Hit or Stand? (h/s): ").lower() == "h" if turn == Players.PLAYER else game.dealerChoice()
        print(f"{turn.name} {'hits' if hit else 'stands'}")
        if hit:
            game.dealCard(turn)
            game.prettyPrint()
            if game.handValue(turn) > 21:
                print(f"{turn.name} busts!")
                break
        else:
            turn = Players.DEALER if turn == Players.PLAYER else Players.PLAYER
            continue





if __name__ == '__main__':
    main_cli()
