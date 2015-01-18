 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import socket
import os
import b_functions

#Clear Screen
b_functions.clear()

#Get/Check Command Line Arguments
p1Placer, p1Name, p2Placer, p2Name, rounds = b_functions.command_args(sys.argv)

#Check for Placer File
p1Placer_path = b_functions.custom_placer_path(p1Name)
p2Placer_path = b_functions.custom_placer_path(p2Name)

p1Placer = b_functions.custom_placer_check(p1Placer, p1Name, p1Placer_path)
p2Placer = b_functions.custom_placer_check(p2Placer, p2Name, p2Placer_path)

b_functions.pause()
b_functions.clear()

#Initialize Boards
p1_own_board = [["W"]*10 for i in range(10)]
p1_opp_board = [["W"]*10 for i in range(10)]
p2_own_board = [["W"]*10 for i in range(10)]
p2_opp_board = [["W"]*10 for i in range(10)]

#Server/Client Variables
p1Port = b_functions.get_player_port(p1Name)
p2Port = b_functions.get_player_port(p2Name)

#Start Sockets with Placers
b_functions.start_placer_server(1, p1Port)
b_functions.pause()
#os.system("test_client.py && echo 'Starting Server'",b_functions.get_player_port(p1Name))
#Send Boards to Players for Ship Placement

#Get Boards From Placers

#Check boards for valid placement
if(b_functions.valid_board(p1_own_board) != True):
    print "There is an error with ship placement for %s" %p1Name
else:
    print "Board for %s is valid." %p1Name

if(b_functions.valid_board(p2_own_board) != True):
    print "There is an error with ship placement for %s" %p2Name
else:
    print "Board for %s is valid." %p2Name

b_functions.pause()
b_functions.clear()
 
b_functions.print_board(p1_own_board)
    
#Start Round
        

    
