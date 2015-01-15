 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import os
import socket

#Get/Check Command Line Arguments
#print sys.argv
if(len(sys.argv)<5 or len(sys.argv)>6):
    print "Error in arguments."
    sys.exit(0)
    
if(sys.argv[1] == "-c" or sys.argv[1] == "-d"):
    p1Placer = sys.argv[1]
else:
    print "Error in arguments."
    sys.exit(0)
p1Player = sys.argv[2]

if(sys.argv[3] == "-c" or sys.argv[3] == "-d"):
    p2Placer = sys.argv[3]
else:
    print "Error in arguments."
    sys.exit(0)
p2Player = sys.argv[4]

if(sys.argv[5]):
    rounds = sys.argv[5]
else:
    rounds = 50
    
#Check for Placer File
p1Placer_path = "players/player"+p1Player+"/place"+p1Player+".py"
p2Placer_path = "players/player"+p2Player+"/place"+p2Player+".py"

if(p1Placer == "-c"):
    try:
        with open(p1Placer_path) as f: print "Found "+p1Placer_path
    except IOError as e:
        print "Error: %s not found." % p1Placer_path
        p1Placer = "-d"
        print "Using default ship placer for %s" %p1Player
else:
    print "Using default ship placer for %s" %p1Player

if(p2Placer == "-c"):
    try:
        with open(p2Placer_path) as f: print "Found "+p2Placer_path
    except IOError as e:
        print "Error: %s not found." % p2Placer_path
        p2Placer = "-d"
        print "Using default ship placer for %s" %p2Player
else:
    print "Using default ship placer for %s" %p2Player

raw_input("Press enter to continue")
os.system("clear")

#Start Sockets with Placers

#Initialize Boards
p1_own_board = [["W"]*10 for i in range(10)]
p1_opp_board = [["W"]*10 for i in range(10)]
p2_own_board = [["W"]*10 for i in range(10)]
p2_opp_board = [["W"]*10 for i in range(10)]
    
#Send Boards to Players for Ship Placement


#Check boards for valid placement
a_count = 0
b_count = 0
s_count = 0
d_count = 0
c_count = 0

for i in range(10):
    for j in range(10):
        board_val = p1_own_board[i][j]
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
    print "There is an error with ship placement for %s" %p1Player
    



    

    
