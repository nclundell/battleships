import os
import sys
import csv

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
    raw_input("Press enter to continue")
    
def clear():
    os.system("clear")
    
def custom_placer_path(player):
    return "players/player"+player+"/place"+player+".py"

def custom_placer_check(placer, player, path):
    if(placer == "-c"):
        try:
            with open(path) as f: print "Found "+path
            return "-c"
        except IOError as e:
            print "Placer not found for",player
            return "-d"
    else:
        print "Using default ship placer for %s" %player
        return "-d"

def print_board(board):
    for i in range(10):
        print board[i],"\n"
 
def valid_board(board):
    a_count = 0
    b_count = 0
    s_count = 0
    d_count = 0
    c_count = 0
    
    for i in range(10):
        for j in range(10):
            #Check Diagonals
            if((board[i][j] == board[i+1][j+1]) or (board[i][j] == board[i-1][j-1])):
                print "Error: diagonal ship placement not allowed!"
                return False
            if((board[i][j] == board[i+1][j-1]) or(board[i][j] == board[i-1][j+1])):
                print "Error: diagonal ship placement not allowed!"
                return False
            #Check Out-of-Bounds
            board_val = board[i][j]
            if board_val == "A":
                a_count += 1
            elif board_val == "B":
                b_count += 1
            elif board_val == "S":
                s_count += 1
            elif board_val == "D":
                d_count +=1
            elif board_val == "C":
                c_count += 1
            
    if(a_count != 5 or b_count != 4 or s_count !=3 or d_count != 3 or c_count !=2):
        return False
    return True

def start_server(port):
    return 0

def get_player_port(player):
    with open("players/playerList.csv") as players_csv:
        player_reader = csv.reader(players_csv)
        for listing in player_reader:
            if(listing[0] == player):
                return listing[1]
    print player,"not found.  Using default port 50000"
    return 50000
    
    