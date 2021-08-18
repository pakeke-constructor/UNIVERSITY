
import sys
import socket
import os
import client

def isip(ip):
    return ip.replace(".", "").isdigit()


def main():
    ipv4 = sys.argv[1]
    if not isip(ipv4):
        try:
            ipv4 = socket.getaddrinfo(ipv4)
        except:
            print(f"Abandoned: Malformed or non existant domain: {ipv4}")
            exit(-1)

    portn = sys.argv[2]
    if not (portn.isdigit() and (1024 <= int(portn) <= 64000)):
        print("Abandoned: Port number not an intger between 1024 and 64000")
        exit(-2)

    filename = sys.argv[3]
    if  os.path.isfile(filename):
        print(f"Abandoned: Overwriting file: {filename}")
        exit(-3)

    client.init(ipv4, portn, filename)
    client.run()



