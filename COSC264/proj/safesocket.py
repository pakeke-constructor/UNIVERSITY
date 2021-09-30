
'''
Safesocket file

Automatically closes sockets on python exit.

Author:
Oliver Garrett
(oga20)

'''


import socket
import atexit

class safesocket(socket.socket):
    '''
    safesocket class.
    Automatically closes sockets when python exits
    '''
    # A list of all sockets
    sbuffer = []

    def __init__(self, *a, **ka):
        super().__init__(*a, **ka)
        safesocket.sbuffer.append(self)
        self.setblocking(True)

    def safeaccept(self):
        '''
        Modifies accept
        '''
        (newsock, addr) = super().accept()
        safesocket.sbuffer.append(newsock)
        newsock.setblocking(True)
        return newsock, addr


def clearbuffer():
    for s in safesocket.sbuffer:
        s.close()

atexit.register(clearbuffer)

