



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


def getlen(pkt):
    return get16(pkt, 2)

def getheaderlen(pkt):
    return (pkt[0] & 0b1111) * 4

def payload(pkt):
    return pkt[getheaderlen(pkt):]

print("\n")

print(payload(bytearray(b'F\x00\x00\x1e\x00\x00\x00\x00@\x06h\x86\x11"3DUfw\x88\x00\x00\x00\x00\x13\x14\x15\x16\x17\x18')))
# bytearray(b'\x13\x14\x15\x16\x17\x18')

print("\n")

print(payload(bytearray(b'E\x00\x00\x17\x00\x00\x00\x00@\x06i\x8d\x11"3DUfw\x88\x10\x11\x12')))
# bytearray(b'\x10\x11\x12')
