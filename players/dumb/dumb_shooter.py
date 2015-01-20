#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Target and Shoot for @player

import sys

sys.path.append("../../")

from b_globals import *

class dumb_shooter:
    def __init__(self, board, boardSize):
        self.board = board
        self.boardSize = boardSize
        
    def target(board):
        make_shot(1,1)
    
    def make_shot(h,w):
        return 0