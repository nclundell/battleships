 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import socket
import functions

#Get/Check Command Line Arguments
p1Placer, p1Player, p2Placer, p2Player, rounds = functions.command_args(sys.argv)

#Check for Placer File
p1Placer_path = functions.custom_placer_path(p1Player)
p2Placer_path = functions.custom_placer_path(p2Player)

p1Placer = functions.custom_placer_check(p1Placer, p1Player, p1Placer_path)
p2Placer = functions.custom_placer_check(p2Placer, p2Player, p2Placer_path)

functions.pause_and_clear()

#Start Sockets with Placers

#Initialize Boards
p1_own_board = [["W"]*10 for i in range(10)]
p1_opp_board = [["W"]*10 for i in range(10)]
p2_own_board = [["W"]*10 for i in range(10)]
p2_opp_board = [["W"]*10 for i in range(10)]
    
#Send Boards to Players for Ship Placement

#Get Boards From Placers

#Check boards for valid placement
if(functions.valid_board(p1_own_board) != True):
    print "There is an error with ship placement for %s" %p1Player
else:
    print "Board for %s is valid." %p1Player

if(functions.valid_board(p2_own_board) != True):
    print "There is an error with ship placement for %s" %p2Player
else:
    print "Board for %s is valid." %p2Player

functions.pause_and_clear()
 
functions.print_board(p1_own_board)
    
#Start Round
        

    
