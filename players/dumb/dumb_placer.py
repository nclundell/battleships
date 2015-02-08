#@author Nathan Lundell
#@date January 2015
#@player dumb
#
#Ship Placer for @player

import sys

sys.path.append("../../")

from b_globals import *

class DumbPlacer:
    def __init__(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[WATER]*board_size for i in range(board_size)]

    def place_ship(self, length, ship_num):
        for i in range (len(self.ship_board[0])):
            if self.ship_board[i][0] == WATER:
                for j in range(length):
                    self.ship_board[i][j] = ship_num
                break
    
    def mark_shot(self, shot, result):
        self.mark_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[WATER]*board_size for i in range(board_size)]