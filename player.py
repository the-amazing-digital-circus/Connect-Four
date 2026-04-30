#
# player.py 
#
# A Connect Four Player class 
#

from board import Board

# Write your class below.

class Player:
    """ A class that represents a Player of Connect 4 on the Board object, 
    which tracks the player's checker and the amount of moves
    """
    
    def __init__(self, checker):
        """ Creates the object and assigns the checker to it, and also creates
        an attribute for the number of moves
        """
        
        # Other string for checker that aren't X or O are not valid
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ Return the string representation of a Player object
        """
        return f'Player {self.checker}'
    
    def opponent_checker(self):
        """ Returns the string of the opposite player's checker
        """
        
        # Uses conditional statements to return O if the player is X, and
        # X if the player is O
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Ask for input from the player on what column to place the next
        checker, and gives feedback if the placement is not valid. Also updates
        the num_moves attribute for every move
        """
        
        # Only will accumulate when the method is called
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            
            # Use a return statement to stop the loop when the move is valid
            # as determined by the can_add_to method
            if b.can_add_to(col):
                return col
            
            # If can_add_to is not true, then asks for another input
            else:
                print('Try again!')