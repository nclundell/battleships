#@author Nathan Lundell
#@date January 2015
#@player Dumb
#
#Ship Placer for @player

import sys

sys.path.append("../../")

from b_globals import *

class Placer:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = [["W"]*boardSize for i in range(boardSize)]

    def placeShip(length, marker):
        for i in range (self.boardSize):
            if self.board[i][0] == WATER:
                h=i
                v=0
                for j in range(length):
                    self.board[i][j] = marker
                break
        return h,v,"horizontal"

    def returnBoard():
        return self.board