#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Target and Shoot for @player

import sys

sys.path.append("../../")

from b_globals import *

class dumb_shooter:
    def __init__(self):
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.last_row = 0
        self.last_col = 0
        self.kills = 0
        self.wins = 0
    
    def make_shot(self, shot_count):
        if(shot_count == 0):
            return [0,0]
        if(self.last_col == board_size-1):
            self.last_row += 1
            self.last_col = 0
        else:
            self.last_col += 1
          
        return [self.last_row, self.last_col]
    
    def mark_shot(self,shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.kills = 0
        self.last_row = 0
        self.last_col = 0
