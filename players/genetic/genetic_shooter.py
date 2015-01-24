#@author Nathan Lundell
#@date January 2015
#@player genetic
#
#Target and Shoot for @player

import sys

sys.path.append("../../")

from b_globals import *

class genetic_shooter:
    def __init__(self):
        self.shot_board = [[WATER]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0
        self.shot_count = 0
        self.shot_records = []
        self.wins = 0
    
    def make_shot(self): 
        return [self.last_row, self.last_col]
    
    def mark_shot(self, shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.shot_board = [["W"]*self.board_size for i in range(self.board_size)]
        self.shot_records.append(self.shot_count)
        self.shot_count = 0
        self.last_row = 0
        self.last_col = 0