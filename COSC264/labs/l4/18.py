


import math

def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    maxp = m - o
    return (s % maxp) + o



print (last_fragment_size(10000, 20, 1500))

