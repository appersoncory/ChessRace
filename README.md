# ChessRace

## Description

ChessRace is a chess variant game implemented in Python. In this game, players are engaged in a unique challenge where they race their kings to the top row of the chess board. The game incorporates traditional chess pieces and rules, with an added twist to make the gameplay more exciting and strategic.

![image](https://github.com/appersoncory/ChessRace/assets/84872642/68ac4f0d-9c18-4fa4-9845-ac97aadb9f9a)


## Features

- **Customizable Chess Board**: A dictionary-based board setup allowing for flexible configuration of pieces.
- **Game State Management**: The game state is consistently tracked and updated, providing feedback on whether the game is unfinished, won, or tied.
- **Move Validation**: Implements rules for each piece's valid moves and ensures moves do not put the king in check.
- **Turn Management**: Alternates turns between players, ensuring that the correct player is making a move.
- **Check Status**: Validates that no move results in the player's own king or opponent's king being in check.

## How to Play

1. **Initialize the Game**: Run the `main()` function in your Python environment to initialize a new game.
2. **Enter Moves**: Players will be prompted to enter their moves in turns until the game reaches a conclusive state.
3. **Game End**: The game ends when a king reaches the top row or other defined endgame conditions are met. The final game state will be displayed.

## Installation

1. Clone this repository to your local machine.
   git clone https://github.com/appersoncory/ChessVar.git
2. Navigate to the cloned directory.
3. Run the main function in your Python environment.

## Usage

```python
from ChessVar import ChessVar

def main():
 game = ChessVar()
 # Follow prompts to play the game
 # ...

if __name__ == "__main__":
 main()
