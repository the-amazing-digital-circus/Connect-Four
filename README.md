# Connect-Four
A project that can play Connect Four directly in your terminal. You can play with another person (as long as they're next to you, not online), against yourself, or with AI players with varying difficulty.

## Overview
This project demonstrates textbook object-oriented-programming, using classes to represent important components of the game; playing boards and player types.

For information on how to play Connect Four, please see: https://en.wikipedia.org/wiki/Connect_Four.

## Board
By default, the board dimensions are 6x7, but one can change this by modifying line 28 in [`/connect_four.py`](./connect_four.py) by changing `Board(6, 7)` to the desired dimensions.

The board object has logic for adding the checker (`X`, `O`) to a column and stopping the action if the column is full. It also is where win conditions are detected, based on the alignment of checkers in the current game state.

## Players
There are three objects. [`/player.py`](./player.py) contains the `Player` superclass, which holds the player's checker (`X` or `O`) and has logic for prompting the player's next move on turn.

[`/random_player.py`](./random_player.py) contains a class that inherits from the `Player` superclass. It automatically moves, placing a checker in a random available column.

[`/ai_player.py`](./ai_player.py) contains a class that inherits from the `Player` superclass, and involves a player that automatically makes gameplay decisions using a lookahead algorithm. It determines the score of every possible move based on simulated future outcomes, and chooses the move that leads to a win condition, and avoids choosing moves that result in a losing state.

## Installation & Usage
This project requires Python to be installed. 

When you've done that, you can download the files by cloning the repository. Cloning the repository requires <a href="https://git-scm.com" target="_blank">Git</a>.

In your terminal:
```bash
git clone https://github.com/lifelinh/Connect-Four.git
```
Alternatively, you can download the repository files under the releases.

Next, start the program using IPython in terminal after navigating to the directory that contains the repository files.
```bash
ipython
%run connect_four.py
```
After that, the game can be played with the `connect_four()` function, which takes parameters `player1, player2`. `player1` will always move first.

<details>
  <summary>player1</summary>
  
  The input must be one of three classes: `Player(checker)`, `RandomPlayer(checker)`, or `AIPlayer(checker, tiebreak, lookahead)`. `checker` must be a string, either `"X"` or `"O"`.

  If using `AIPlayer`, `tiebreak` must either be `"LEFT"`, `"RIGHT"`, or "`RANDOM`"; this determines what move will be chosen if several are equally scored by the algorithm. It is defaulted to `"RANDOM"`. `lookahead` must be an integer; it determines how many steps the algorithm will simulate to determine scoring for its move options.
 
</details>

<details>
  <summary>player2</summary>

  The input must be one of three classes: `Player(checker)`, `RandomPlayer(checker)`, or `AIPlayer(checker, tiebreak, lookahead)`. `checker` must be a string that is the counterpart of the string chosen for `player1`; that is, "O" if `player1`'s checker is "X", and "X" if `player1`'s checker is "O".
</details>

Terminal output will prompt the player to select a column to place their tile in, if the `Player` class is used. If only `RandomPlayer` or `AIPlayer` are used, the two will automatically move against each other until the game concludes.

### Example
To go second against an AI player using checker `"O"` that chooses the left most tile if moves are equally scored, and simulates 3 moves to check move viability, the function call would be
```bash
connect_four(AIPlayer("O", "LEFT", 3), Player("X"))
```

The AI player is subject to taking long times to move if a large lookahead value is chosen. If a game is taking too long and you would like to terminate it, press `Ctrl` + `C` to interrupt the process.

### Stopping Usage
To close the program, first press `Ctrl` + `C` if a game is running, and type `exit` to leave the interactive shell.

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

> This was originally created for and submitted as an assignment to demonstrate object-oriented-programming knowledge for [CAS CS 111](https://www.bu.edu/academics/cas/courses/cas-cs-111/): Introduction to Computer Science 1 at Boston University during the Summer-2 2024 semester.