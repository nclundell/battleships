import socket

HOST = "127.0.0.1"
PORT = 50000
BUFFER = 1024

sock = socket.socket()

sock.connect((HOST, PORT))

data = "Die Server, Die!"
sock.sendto(data.encode("utf-8"), (HOST,PORT))