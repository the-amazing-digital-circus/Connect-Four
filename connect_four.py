#
# connect_four.py
#
# Playing the game
#

from board import Board
from player import Player
from random_player import RandomPlayer
from ai_player import AIPlayer
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(p, b):
    """ Processes a player's move on a board, specifying who's turn it is,
    storing and applying the move to the board, printing the board, and
    declaring a win, tie, or neither
    input p: Player object
    input b: Board object
    """
    
    # String representation of the player's turn
    print(f"{p}'s turn")
    
    # Store the input column of the player
    move = p.next_move(b)
    
    # Add the player's checker to the column that was input and stored
    b.add_checker(p.checker, move)
    
    # Print a blank line before printing the board
    print()
    print(b)
    
    # Conditional statements to return and print whether if a win, tie, or if
    # the game is not done yet, along with a blank line before that
    if b.is_win_for(p.checker):
        print()
        print(f'{p} won in {p.num_moves} moves.')
        print('Congratulations!')
        return True
    
    elif b.is_full():
        print()
        print("It's a tie!")
        return True
    
    else:
        return False