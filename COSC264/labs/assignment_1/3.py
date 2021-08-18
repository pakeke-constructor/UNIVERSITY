



def get16(pkt, i):
    assert i < (len(pkt) - 1), "ahem"
    return (pkt[i] << 8) | pkt[i+1]

def get32(pkt, i):
    return ((get16(pkt, i) << 16) | get16(pkt, i + 2))


def check(pkt, checksum):
    x = 0
    for i in range(0, 20, 2):
        x += get16(pkt, i)

    while x > 0xFFFF:
        x0 = x & 0xFFFF
        x1 = x >> 16
        x = x0 + x1

    return x == 0xFFFF


def basicpacketcheck (pkt):
    if len(pkt) < 20:
        return 1
    if ((pkt[0] & 0b_1111_0000) >> 4) != 4:
        return 2  
    if not check(pkt, get16(pkt, 10)):
        return 3
    if get16(pkt, 2) != len(pkt):
        return 4
    return True
    

def destaddress(pkt):
    ret = []
    for i in range(16, 20):
        ret.append(str(pkt[i]))
    return (get32(pkt, 16), '.'.join(ret))

print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))

