#
# ai_player.py
# 
# An AI Player for use in Connect Four
#

import random
from connect_four import * # to use the connect_four and process_move functions

class AIPlayer(Player):
    """ Subclass for an intelligent AI player that uses look ahead algorithms
    to make the best choice in a Connect 4 game, with inheritance from the
    Player superclass
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructor for the AI player, with options for modifying how far
        the player looks ahead, and what to pick in case there are equally
        good options
        """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ Overwrite the __repr__ method that would've been inherited, and
        print out additional information such as the tiebreak and lookahead
        """
        
        return f'Player {self.checker} ({self.tiebreak}, {self.lookahead})'
    
    def max_score_column(self, scores):
        """ Chooses the best column according to the score for the move, and
        the appropriate one according to tiebreaker if there are multiple 
        moves tied as best
        """
        
        # Get the highest value in the list, which will be used as the 
        # condition for the list comprehension
        max_score = max(scores)
        
        # Create a list of indices of the maximum score
        indices = [i for i in range(len(scores)) if scores[i] == max_score]
        
        # Pick first, last, or random index depending on the tiebreak attribute
        if self.tiebreak == 'LEFT':
            return indices[0]
        
        if self.tiebreak == 'RIGHT':
            return indices[-1]
        
        if self.tiebreak == 'RANDOM':
            return random.choice(indices)
        
    def scores_for(self, board):
        """ Creates a list of the move score in every column after the looking
        ahead algorithm works on the board
        """
        
        # Create a list of scores depending on the width of the board
        scores = [50] * board.width
        
        for c in range(board.width):
            # A full column has a score of -1, nothing can be added to it.
            if not board.can_add_to(c):
                scores[c] = -1
        
            # Continue with other options for rows that aren't empty
            else: 
                # If it's neither a win or loss, and the lookahead is 0, the score
                # is to be 50
                if self.lookahead == 0:
                    scores[c] = 50
                
                # Simulate a move if the lookahead is not 0
                else:
                    board.add_checker(self.checker, c)
                    
                    # If the AI player already won, the score is 100.
                    if board.is_win_for(self.checker):
                        scores[c] = 100
                
                    # If the AI player lost, then the score is 0
                    elif board.is_win_for(self.opponent_checker()):
                        scores[c] = 0
                
                    # Simulating a move and checking the opponent's scores 
                    # after the above conditions have been examined
                    else:
                        opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                        opp_scores = opp.scores_for(board)
                
                        # A loss for the opponent is a win for the player, and 
                        # a win for the opponent is the worst move. Any other 
                        # situation is 50 for both players.
                        if max(opp_scores) == 0:
                            scores[c] = 100
                        
                        elif max(opp_scores) == 100:
                            scores[c] = 0
                        
                        else:
                            scores[c] = 50
                     
                    # Must remove the checker after testing the column for 
                    # scores
                    board.remove_checker(c)
                    
        return scores
    
    def next_move(self, board):
        """ Specialization of the next_move method from the superclass, so
        that the AIPlayer automatically makes the next move rather than asking
        for input
        """
        
        # Accumulate the number of moves for every time the method is used
        self.num_moves += 1
        
        # Return the proper move as the input when in a game
        return self.max_score_column(self.scores_for(board))
        
        