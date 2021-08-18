
import socket


sock = None

file = None


def init(ipv4, port, filename):
    global sock
    global file
    file = filename
    sock = socket.socket()
    sock.bind((ipv4, port))
    try:
        sock.connect((ipv4, port))
    except:
        sock.close()
        print("Client: Socket connection failed")
        exit(-4)


def run():
    pass


