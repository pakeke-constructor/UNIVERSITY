

import math
def total_number_bits (maxUserDataBitsPerPacket_b,
        overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b

    packets = math.ceil(M / S)
    return packets * O + messageLength_b

print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))

