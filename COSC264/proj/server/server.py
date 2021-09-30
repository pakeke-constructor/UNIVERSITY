

'''
Server file

Author:
Oliver Garrett
(oga20)

'''

import sys

sys.path.append("D:\\PROGRAMMING\\UNIVERSITY\\COSC264\\proj")
#  Temporary for my computer

import socket
from safesocket import safesocket
import time
import request
import response
import os
import math


MAX_RECV = 4096
TIMEOUT = socket.timeout

socket.setdefaulttimeout(30)

def exit(*a,**ka): input("Halted")

def get_ip():
    return socket.gethostbyname(socket.gethostname())


def init(port):
    global sock
    sock = safesocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((get_ip(), port))
        return sock
    except Exception as e:
        sock.close()
        print(f"Server: Error binding socket on port {port}: \n{e}")
        exit()



def sendbad(sock):
    packet = response.make(0, bytearray())
    sock.sendall(packet)


def gettime():
    return time.strftime('%X %x %Z')


def sendall(newsock, packet):
    iter = math.ceil(len(packet) / MAX_RECV)
    for i in range(iter):
        newsock.sendall(packet[i * MAX_RECV : (i + 1) * MAX_RECV])


def loop(sock):
    try:
        (newsock, addr) = sock.safeaccept()
        newsock.settimeout(1)
    except BaseException as e:
        print("Server: accept refused to work" + str(e))
        exit()

    t1 = gettime()
    print(f"Server: Accepted connection from {addr} at {t1}")
    
    try: 
        success, fnamelen, fname = request.unmake(newsock.recv(MAX_RECV))
    except socket.timeout as e:
        print(f"Server: client stopped responding. Resetting\n")
        newsock.close()
        return

    if success != 1:
        print("Server: client packet is incorrect")
        return sendbad(sock)

    if fnamelen != len(fname):
        print("Server: filename does not agree with filename length")
        return sendbad(sock)

    if not os.path.exists(fname):
        print("Server: non existant file")
        return sendbad(sock)

    with open(fname, "rb") as f:
        t = time.time()
        byts = f.read()
        packet = response.make(1, byts)
        t1 = time.time()
        print("Server: time taken to read: " + str(t1-t))
        try:
            # previously: newsock.sendall(packet)
            sendall(newsock, packet)
            print(f"Server: File successfully sent to {addr} at {gettime()}\n")
        except socket.timeout as e:
            print(f"Server: client stopped responding\n")
            newsock.close()
            


def run(sock):
    try:
        sock.listen()
    except:
        print("Server: Listen failed.")
        sock.close()
        exit()

    print("Server: Listening on ")
    print("Server: waiting for clients:\n")
    
    while True:
        loop(sock)



def main():
    inp = sys.argv[1]

    if (not inp.isdigit()):
        print("Server: Wrong input format. Expected integer.")

    port = int(inp)
    if not (1024 <= port <= 64000):
        print("Server: input error: expected a port number between 1024 and 64000 inclusive.")
        exit(-1)

    sock = init(port)
    print(f"Server: Running server on {get_ip()}, {port}")
    run(sock)


if __name__ == "__main__":
    main()


