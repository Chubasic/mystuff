from socket import *

HOST = 'localhost'
PORT = 4444
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    print("Received ", data.decode('UTF-8'))
    reply = input("Reply:")
    conn.sendall(bytes(reply, 'UTF-8'))

conn.close()
