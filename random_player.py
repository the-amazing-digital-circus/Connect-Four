#
# random_player.py
#
# A RandomPlayer for use in Connect Four
#

import random
from player import Player

class RandomPlayer(Player):
    """ Subclass inheriting from the Player class that represents an automated
    player that makes random moves in possible rows
    """
    
    def next_move(self, board):
        """ Specialization of the next_move method defined in the superclass so
        that the next_move is a random choice
        input board: Board object
        """
        # Use a list comprehension to create a list only including columns
        # where a column can have a checker added to it
        choices = [c for c in range(board.width) if board.can_add_to(c) == True]
        
        # Accumulate the number of moves
        self.num_moves += 1
        
        # Pick a random column from the list created by the list comprehension
        return random.choice(choices)