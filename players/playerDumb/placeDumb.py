import socket

class Dumb_placer(board, ship, length):
    def __init__(self, board, ship, length):
        self.board = board
        self.ship = ship
        self.length = length
        
    def place():
        for i in range (10):
            if self.board[i][0] == 'W':
                for j in range(self.length):
                    self.board[i][j] = self.ship
                break
        return self.board
