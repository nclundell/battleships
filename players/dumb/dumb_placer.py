#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Ship Placer for @player

import sys

sys.path.append("../../")

from b_globals import *

class dumb_placer:
    def __init__(self, board):
        self.board = board

    def place_ship(length, marker):
        for i in range (length, marker):
            if self.board[i][0] == WATER:
                for j in range(length):
                    self.board[i][j] = marker
                    
    def return_board():
        return self.board[:][:]