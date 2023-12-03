# BlackJack Game

This project is a Python implementation of the popular card game, BlackJack. The game is played in the command line interface and uses a dealer AI to simulate the dealer's decisions during the game. The dealer AI can operate in two modes: aggressive and conservative.

## Key Algorithms and Data Structures

### Dealer AI

The dealer AI is implemented in the `DealerAI` function in the `game_core.py` file. The AI uses a decision tree to map out the possible outcomes of the game and decide whether to hit or stand based on the current state of the game. The decision tree is built using the `build_tree` function, which recursively adds nodes to the tree until a certain threshold is reached. The threshold is set to 17, as per the rules of BlackJack.

The AI then finds all the "good" paths in the decision tree, i.e., paths that do not result in a bust, using the `find_good_paths` function. It calculates the ratio of good paths to total paths and the odds of the next card falling into the good paths. Based on these calculations and the current AI mode, the AI decides whether to hit or stand.

### Game State

The game state is represented by the `GameState` class in the `game_state.py` file. The class maintains the current state of the game, including the deck of cards, the dealer's hand, the player's hand, and the AI mode. It also provides methods for dealing cards, calculating hand values, and determining the winner of the game.


## Running the Game

To run the game, execute the `main.py` file. You can choose the mode for the dealer AI by passing the `--mode` argument with either `aggressive` or `conservative` as the value. The game will then start and you can play by following the prompts in the command line interface.