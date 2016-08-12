from socket import *

HOST = 'localhost'  # in order to get the client to work host had to be filled in
PORT = 4444
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))
while True:
    message = input("Message : ")
    sock.send(bytes(message, 'UTF-8'))
    print("Awaiting reply")
    reply = sock.recv(1024)
    print("Received :", reply.decode('UTF-8'))
sock.close()

