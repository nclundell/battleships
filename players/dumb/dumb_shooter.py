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
        self.shot_count = 0
        self.shot_records = []
        self.kills = []
        self.wins = 0
    
    def make_shot(self):
        if(self.shot_count == 0):
            self.shot_count += 1
            return [0,0]
        if(self.last_col == board_size-1):
            self.last_row += 1
            self.last_col = 0
        else:
            self.last_col += 1
        
        self.shot_count += 1    
        return [self.last_row, self.last_col]
    
    def mark_shot(self,shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.shot_records.append(self.shot_count)
        self.kills = []
        self.shot_count = 0
        self.last_row = 0
        self.last_col = 0