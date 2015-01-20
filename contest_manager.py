import socket
import sys
import os

sys.path.append("../../")

import b_globals
import b_functions

player1_name = sys.argv[1]
player2_name = sys.argv[2]
board_size = int(sys.argv[3])
ships = [b_globals.CARRIER,b_globals.BATTLESHIP,b_globals.SUBMARINE,b_globals.DESTROYER,b_globals.CRUISER]

#Start Server
HOST = "127.0.0.1"
PORT = 50000
ADDR = (HOST,PORT)
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(5)

#Get Player Ports
player1_port = b_functions.get_player_port(player1_name)
if(player1_name == player2_name):
    player2_port = player1_port+10000
player2_port = b_functions.get_player_port(player2_name)

print int(player1_port)
print int(player2_port)


#Start Placement Shims
data = "START_PLACER;"+str(board_size)
os.system("players/placer_shim.py "+player1_name+" "+player1_port)
sock.sendto(data.encode("utf-8"), (HOST,player1_port))
os.system("players/placer_shim.py "+player2_name+" "+player2_port)
sock.sendto(data.encode("utf-8"), (HOST,player2_port))

#Send Request For Ship Placement
for i in range(len(ships)):
    data = "PLACE;"+ships[i][0]+","+ships[i][1]
    sock.sendto(data.encode("utf-8"), (HOST,player1_port))
    sock.sendto(data.encode("utf-8"), (HOST,player2_port))

#Listen For Data From Placer Shims
p1_placed = False
p2_placed = False
while True:
    conn, client = sock.accept()
    data = conn.recv(BUFFER)
    data = data.split(';')
    items = data[1].split(',')
    
    if(data[0] == "SHIPS_PLACED"):
        if(conn[1] == player1_port): p1_placed = True
        if(conn[1] == player2_port): p2_placed = True
    
    if data == "DIE": break

##Shooter Loop
#while True:
#    conn, client = sock.accept()
#    data = conn.recv(BUFFER)

  
sock.close()
    


