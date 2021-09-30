

'''
client.py

Client python file

Author:
Oliver Garrett (oga20)

'''

from safesocket import safesocket 
import socket
import request
import response
import os
import sys
import time


MAX_RECV = 4096

IP = socket.gethostbyname(socket.gethostname())


def init(ipv4, port):
    sock = safesocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ipv4, port))
        return sock
    except BaseException as e:
        sock.close()
        print("Client: Socket connection failed")
        print("Error: " + str(e))
        exit(-4)


def request_file(sock, fname):
    if os.path.exists(fname):
        return False    
    packet = request.make(fname)
    sock.sendall(packet)
    return True


def getdata(sock):
    try:
        rpacket = sock.recv(MAX_RECV)
    except socket.timeout:
        print("Client: Socket timed out; server is likely busy or down.")
        exit(-5)
    return rpacket

def start(sock):
    rpacket = getdata(sock)
    status, dlen, data = response.unmake(rpacket)
    if not status:
        print("Client: Server file not available or malformed packet.")
        exit(-5)

    return dlen, data


def write(sock, file):
    response = getdata(sock)
    file.write(response)
    return len(response)


def run(sock, fname):
    print("Client: started...")
    success = request_file(sock, fname)

    if not success:
        print("Client: File already exists, will not overwrite")
        exit(-7)

    print("Client: Success in requesting file")
    data_left, filedata = start(sock)
    data_left -= len(filedata)

    with open(fname, "ab+") as file:
        file.write(filedata)

        while data_left > 0:
            datalen = write(sock, file)
            data_left -= datalen



def isip(ip):
    return ip.replace(".", "").isdigit()


def main():
    ipv4 = sys.argv[1]
    if not isip(ipv4):
        try:
            ipv4 = socket.getaddrinfo(ipv4)
        except:
            print(f"Client: Malformed or non existant domain: {ipv4}")
            exit(-1)

    portn = sys.argv[2]
    if not (portn.isdigit() and (1024 <= int(portn) <= 64000)):
        print("Client: Port number not an intger between 1024 and 64000")
        exit(-2)

    filename = sys.argv[3]
    if  os.path.isfile(filename):
        print(f"Client: Aborted! Overwriting file: {filename}")
        exit(-3)

    sock = init(ipv4, int(portn))
    run(sock, filename)

if __name__ == "__main__":
    main()



