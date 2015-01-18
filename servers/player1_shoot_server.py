import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1])
ADDR = (HOST,PORT)
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print "Player 1 shooting erver started, listening on port",PORT

sock.listen(5)
while True:
    conn, client = sock.accept()
    data = conn.recv(BUFFER)
    print "Message from",client,": ",data
    if data == "Die Server, Die!": break
sock.close()
    


