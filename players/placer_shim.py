import sys
import socket

sys.path.append("../")
import b_functions

#Get Player Name
if(sys.argv[1]):
    with open("playerList.csv") as players_csv:
        player_reader = csv.reader(players_csv)
        for listing in player_reader:
            if(sys.argv[1] == listing[0]):
                player_name = sys.argv[1]
        print "Player",sys.argv[1],"does not exist."
        sys.exit(0)
else:
    print "Error: No player name given."
    sys.exit(0)

sys.path.append('player'+player_name+"/")
import placer

#Setup Communications
HOST = "127.0.0.1"
PORT = sys.argv[2]
ADDR = (HOST,PORT)
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(5)

while True:
    conn, client = sock.accept()
    data = conn.recv(BUFFER)
    data = data.split(';')
    items = data[1].split(',')
    
    if(data[0] == "START_PLACER"):
        Player = Placer(items[0])
    
    #Place Ship, Return Placement Details
    if(data[0] == "PLACE"):
        #Place Ships
        ship_length = items[0]
        ship_marker = items[1]
        h,v,ship_direction = player.placeShip(ship_length, ship_marker)
        data = "SHIP_PLACED;"+ship_length+","+ship_marker+","+ship_direction+","+h+","+v
        sock.sendto(data.encode("utf-8"), (HOST,50000))
        b_functions.print_board(player.board)
        
    if (data[0] == "DIE"):
        break
    
sock.close()

