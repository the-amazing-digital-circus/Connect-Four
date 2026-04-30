#
# board.py
#
# A Connect Four Board class
#

class Board:
    """ A class that represents the Connect 4 playing board, represented with
    the dimensions of the board and the state of its slots
    """
    
    # Constructor for the board with dimensions
    def __init__(self, height, width):
        """ Creates a playing board with height and width dimensions
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    # Return the Board object represented as a string
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        s += '-' * (self.width * 2 + 1) + '\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)
        return s
    
    def add_checker(self, checker, col):
        """ Adds a checker, either O or X to a column until it cannot fall
        in the column anymore
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        # Iterates over the rows from the bottom, from the lowest row to row 0
        for r in range(self.height - 1, -1, -1):
            
            # Only updates the slot once an empty slot is found, then breaks
            if self.slots[r][col] == ' ':
                self.slots[r][col] = checker
                break

    def reset(self):
        """ Sets all slots on the board to empty slots
        """
        # Reuse line from constructor method that just creates empty slots
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self, col):
        """ Returns a Boolean value based on whether if it is possible to add
        a checker to a column or not
        """
        
        # Check if the column even exists on the board
        if col < 0 or col > self.width - 1:
            return False
        
        # Check if the top slot is empty, and if it isn't, the column is full
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True

    def is_full(self):
        """ returns True if the called Board object is completely full of 
        checkers, and returns False otherwise
        """
        
        # Iterate over every column and check if they can have checkers added
        # to them, if not, then it is full
        for c in range(self.width):
            if self.can_add_to(c):
                return False
        return True
    
    def remove_checker(self, col):
        """ Removes the top-most checker from col
        """
        
        # Iterate over slots from the top of col until a slot with a checker
        # is detected, then setting that slot to an empty slot and ending loop
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next 4 rows in this column contain checker
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col] == checker and \
                self.slots[row + 2][col] == checker and \
                self.slots[row + 3][col] == checker:
                    return True
        
        # if we make it here, there were no vertical wins
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win that goes down from left to right for
        the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next 4 slots to the bottom right contain checker
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col + 1] == checker and \
                self.slots[row + 2][col + 2] == checker and \
                self.slots[row + 3][col + 3] == checker:
                    return True
                
        # if we make it here, there were no diagonally down wins
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win that goes up from left to right for the
        specified checker
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next 4 top right slots contain the checker
                if self.slots[row][col] == checker and \
                self.slots[row - 1][col + 1] == checker and \
                self.slots[row - 2][col + 2] == checker and \
                self.slots[row - 3][col + 3] == checker:
                    return True
        
        # if we make it here, there were no diagonally up wins
        return False
    
    def is_win_for(self, checker):
        """ Uses previous helper functions to check if there is a win 
        condition met by the specified checker, returning a Boolean value
        """
        
        # Call the previous methods that check for wins, and if anything is
        # true then there is a win condition met
        if self.is_horizontal_win(checker) or self.is_vertical_win(checker) \
        or self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker):
            return True
        
        # if we make it here, there was no 4 in a row
        else:
            return False