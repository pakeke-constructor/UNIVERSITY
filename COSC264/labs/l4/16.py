

import math

def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    maxp = m - o
    return math.ceil(s / maxp)

print (number_fragments(10000, 100, 1000))

