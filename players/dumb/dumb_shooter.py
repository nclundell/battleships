#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Target and Shoot for @player

import sys

sys.path.append("../../")

from b_globals import *

class dumb_shooter:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[WATER]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0
        self.shot_count = 0
        self.wins = 0
    
    def make_shot(self):
        if(self.shot_count == 0):
            self.shot_count += 1
            return [0,0]
        if(self.last_col == self.board_size-1):
            self.last_row += 1
            self.last_col = 0
        else:
            self.last_col += 1
        
        self.shot_count += 1    
        return [self.last_row, self.last_col]
    
    def mark_shot(self, shot, result):
        self.board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.board = [["W"]*self.board_size for i in range(self.board_size)]
        self.shot_count = 0
        self.last_row = 0
        self.last_col = 0