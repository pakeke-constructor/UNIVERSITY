
import socket
import time
import sys

sock = None

socket.setdefaulttimeout(30)


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def init(port):
    global sock
    sock = socket.socket()
    try:
        sock.bind((get_ip(), port))
    except Exception as e:
        sock.close()
        print(f"Server: Error binding socket on port {port}: \n{e}")
        exit()


CLIENTS = []


def loop():
    (newsock, addr) = sock.accept()
    ftime = time.strftime('%l:%M%p %Z on %b %d, %Y')
    print(f"Accepted connection from {addr} at {ftime}")
    CLIENTS.append(newsock)

    return


def run():
    try:
        sock.listen()
    except:
        print("Server: Listen failed.")
        sock.close()
        exit()

    while 1:
        loop()



