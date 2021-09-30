import socket
from socket import socketpair   # https://docs.python.org/3/library/socket.html
import threading

HEADER = 64
PORT = 5009                                          # typically unused port so a safe bet
SERVER = socket.gethostbyname(socket.gethostname())  # more elegant way to get your local ip address as apposed to hard codeing an ip
ADDR = (SERVER,PORT)                                 # Binding address needs to be in a tuple as so
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # AF_INET == Internet domain notation. SOCK_STREAM == stream of data. 
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:                                               # will only happen once we receive once we get some data.
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # handle Disconnection Cleanly
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg Received".encode(FORMAT))
    
    conn.close()

        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()                                      # receives address and connection Socket object to allow us to send info back.
        thread = threading.Thread(target=handle_client, args=(conn,addr)) # p3 only 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")   # will show us all the active connection on the server. -1 because the "start thread" will be running 



print("[STARTING] Server is starting ...")
start()