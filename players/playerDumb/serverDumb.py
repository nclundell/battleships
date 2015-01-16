import socket

HOST = "127.0.0.1"
PORT = 50000
ADDR = (HOST,PORT)
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print "Server started, listening on port",PORT

sock.listen(5)
while True:
    conn, client = sock.accept()
    data = conn.recv(BUFFER)
    print "Message from",client,": ",data
    if data == "Die Server, Die!": break
sock.close()
    


