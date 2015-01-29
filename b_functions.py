 #@author Nathan Lundell
 #@date January 2015
 #Functions for Battleships simulator

import os
import sys
import time
import random
from b_globals import *

def command_args(argv):
    p1_name = argv[1]
    p2_name = argv[2]

    if(len(argv) == 4 ):
        rounds = int(argv[3])
    else:
        rounds = 50
        
    if(len(argv) > 4):
        print "Error in arguments given!"
        sys.exit()
        
    return p1_name, p2_name, rounds
    
def pause():
    print "\n"
    raw_input("Press enter to continue")

def sleep(s):
    time.sleep(s)

def clear():
    os.system("clear")

def custom_placer_path(player):
    return "players/"+player+"/"+player+"_placer.py"

def custom_shooter_path(player):
    return "players/"+player+"/"+player+"_shooter.py"

def player_exists(player):
    for p in players:
        if player == p:
            return True
    print "Player "+player+" not found!"
    return False

def custom_placer_check(player):
    try:
        with open(custom_shooter_path(player)) as f:
            print player+" placer found!"
            return True
    except IOError as e:
        print player+" placer not found.  Using default placer."
        using_defaults = True
        return False

def custom_shooter_check(player):
    try:
        with open(custom_shooter_path(player)) as f:
            print player+" shooter found!"
            return True
    except IOError as e:
        print player+" shooter not found.  Using default shooter."
        using_defaults = True
        return False

def print_board(board):
    for i in range(board_size):
        print board[i],"\n"
    pause()
 
def valid_board(board):
    #Currently Does Not Check For Diagonals
    ship_counts = [0]*len(ships)
    for i in range(board_size):
        for j in range(board_size):
            if(board[i][j] != WATER):
                ship_counts[board[i][j]] += 1
    for s in range(len(ships)):
        if (ship_counts[s] != ships[s]):
            return False
    return True

def mark_kill(ship, ship_board, shot_board):
    for i in range(board_size):
        for j in range(board_size):
            if(ship_board[i][j] == ship):
                shot_board[i][j] = KILL
                ship_board[i][j] = KILL

def is_sunk(ship, ship_board, shot_board):
    hits_needed = ships[ship]
    for i in range(board_size):
        for j in range(board_size):
            if(ship_board[i][j] == ship and shot_board[i][j] == HIT):
                hits_needed -= 1
    if(hits_needed == 0):
        return True
    return False

def average_shot_count(shot_counts):
    total = 0
    for i in range(len(shot_counts)):
        total += shot_counts[i]
    return total/len(shot_counts)

def export_shot_records(p1_name, p2_name, shot_records):
    filename = "results/"+p1_name+"VS"+p2_name
    shots = open(filename, 'w+')
    for i in range(len(shot_records)):
        shots.write(str(shot_records[i])+"\n")
    shots.close()
    

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
        if(print_games):
            print "\nTie Game!"
        return "TIE"
    if(p1_dead):
        if(print_games):
            print "\nPlayer 1 Wins!"
        return "P1"
    if(p2_dead):
        if(print_games):
            print "\nPlayer 2 Wins!"
        return "P2"

def get_rand_float(num):
    return random.uniform(0, )
    
    
