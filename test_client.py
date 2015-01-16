import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1])
BUFFER = 1024

sock = socket.socket()

sock.connect((HOST, PORT))

data = "Die Server, Die!"
sock.sendto(data.encode("utf-8"), (HOST,PORT))