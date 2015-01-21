 #@author Nathan Lundell
 #@date January 2015
 #Functions for Battleships simulator

import os
import sys
from b_globals import *

def command_args(argv):
    if(len(argv)<5 or len(argv)>6):
        print "Error in arguments."
        sys.exit(0)
    
    if(argv[1] == "-c" or argv[1] == "-d"):
        p1Placer = argv[1]
    else:
        print "Error in arguments."
        sys.exit(0)
    
    p1Player = argv[2]
        
    if(argv[3] == "-c" or argv[3] == "-d"):
        p2Placer = argv[3]
    else:
        print "Error in arguments."
        sys.exit(0)
        
    p2Player = argv[4]
    
    if(len(argv) >= 6):
        rounds = argv[5]
    else:
        rounds = 50
        
    return p1Placer, p1Player, p2Placer, p2Player, rounds
    
def pause():
    print "\n"
    raw_input("Press enter to continue")
    
def clear():
    os.system("clear")

def custom_placer_path(player):
    return "players/"+player+"/"+player+"_placer.py"

def custom_shooter_path(player):
    return "players/"+player+"/"+player+"_shooter.py"

def custom_placer_check(player):
    try:
        with open(custom_shooter_path(player)) as f: return True
    except IOError as e: return False

def custom_shooter_check(player):
    try:
        with open(custom_shooter_path(player)) as f: return True
    except IOError as e: return False

def print_board(board, board_size):
    for i in range(board_size):
        print board[i],"\n"
 
def valid_board(board, board_size):
    
    return True

def check_game_over(p1_board, p2_board, board_size):
    p1_dead = True
    p2_dead = True
    for i in range(board_size):
        for j in range(board_size):
            if(p1_board[i][j] != WATER and p1_board[i][j] != MISS and p1_board[i][j] != HIT and p1_board[i][j] != KILL):
                p1_dead = False
            if(p2_board[i][j] != WATER and p2_board[i][j] != MISS and p2_board[i][j] != HIT and p2_board[i][j] != KILL):
                p2_dead = False
    
    if(p1_dead == False and p2_dead == False):
        return "NONE"
    if(p1_dead and p2_dead):
        print "Tie Game!"
        return "TIE"
    if(p1_dead):
        print "Player 1 Wins!"
        return "P1"
    if(p2_dead):
        print "Player 2 Wins!"
        return "P2"
                
    
    
