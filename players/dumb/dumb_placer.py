#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Ship Placer for @player

import sys

sys.path.append("../../")

from b_globals import *

class dumb_placer:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[WATER]*self.board_size for i in range(self.board_size)]

    def place_ship(self, length, marker):
        for i in range (len(self.board[0])):
            if self.board[i][0] == WATER:
                for j in range(length):
                    self.board[i][j] = marker
                break
                    
    def return_board(self):
        return self.board[:][:]
    
    def mark_shot(self, shot, result):
        self.board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.board = [["W"]*self.board_size for i in range(self.board_size)]