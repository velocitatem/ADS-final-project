"""ADS Final Project
A black-jack implementation in Python.
Using:
+ Pygame
"""
from game_state import GameState, Players
from colorama import Fore, Style, init

init(autoreset=True)

def main_cli():
    print(Fore.GREEN + "Welcome to BlackJack Game!")
    print("Rules: Try to get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.")

    game = GameState()
    game.prettyPrint(show_house_card=False)

    turn = Players.PLAYER
    stood_status = {
        Players.PLAYER: False,
        Players.DEALER: False
    }
    while True:
        if stood_status[Players.PLAYER] and stood_status[Players.DEALER]:
            break
        print(Fore.YELLOW + f"\n{turn.name}'s turn")
        hit = input("Hit or Stand? (h/s): ").lower() == "h" if turn == Players.PLAYER else game.dealerChoice()
        print(f"{turn.name} {'hits' if hit else 'stands'}")
        if hit:
            game.dealCard(turn)
            game.prettyPrint()
            if game.handValue(turn) > 21:
                print(Fore.RED + f"{turn.name} busts!")
                break
        else:
            stood_status[turn] = True
            turn = Players.DEALER if turn == Players.PLAYER else Players.PLAYER
            continue

    winner = game.winner()
    if winner is None:
        print(Fore.CYAN + "\nDraw!")
    else:
        print(Fore.GREEN + f"\n{winner.name} wins!")

    print(Fore.GREEN + "\nThank you for playing BlackJack! See you next time.")

if __name__ == '__main__':
    # use argparse to parse the command line arguments
    # let the user select what mode to play in
    # --mode [aggressive, conservative]
    # also give a help message where we explain the modes and the game
    # add a --gui flag to play in gui mode (experimental)
    # argparse:...
    main_cli()