

TOTAL = 160 # 160 bits in packet header


def is_valid(var, bits):
    return (var < (2 ** bits)) and (var >= 0)

START_16 = 0b1111_1111_0000_0000
END_16   = 0b0000_0000_1111_1111


def push16(bytearr, num):
    assert is_valid(num, 16), f"Number `{num}` not valid, must be 16 bit"
    bytearr.append((num & START_16) >> 8)
    bytearr.append(num & END_16)


def ins16(bytearr, num, index):
    assert is_valid(num, 16), f"Number `{num}` not valid, must be 16 bit"
    bytearr[index] = ((num & START_16) >> 8)
    bytearr[index + 1] = (num & END_16)





FULLBYTE = 0b1111_1111
MASK_32 = [
    24,
    16,
    8,
    0
]


def push32(bytearr, num):
    assert is_valid(num, 32), "Number not valid, must be 32 bit"
    for mshift in MASK_32:
        mask = FULLBYTE << mshift
        bytearr.append((num & mask) >> mshift)


def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, 
            headerchecksum, sourceaddress, destinationaddress):

    ret = bytearray()

    if version != 4 and version > 0:
        return 1
    if not (is_valid(hdrlen, 4) or (hdrlen < 5)):
        return 2
    if not is_valid(tosdscp, 6):
        return 3
    if not is_valid(totallength, 16):
        return 4
    if not is_valid(identification, 16):
        return 5
    if not is_valid(flags, 3):
        return 6
    if not is_valid(fragmentoffset, 13):
        return 7
    if not is_valid(timetolive, 8):
        return 8
    if not is_valid(protocoltype, 8):
        return 9
    if not is_valid(headerchecksum, 16):
        print(headerchecksum)
        return 10
    if not is_valid(sourceaddress, 32):
        return 11
    if not is_valid(destinationaddress, 32):
        return 12
    
    version <<= 4
    ret.append(version | hdrlen)

    tosdscp <<= 2
    ret.append(tosdscp)

    push16(ret, totallength)
    push16(ret, identification)

    flags <<= 13
    push16(ret, flags | fragmentoffset)

    ret.append(timetolive)
    ret.append(protocoltype)

    push16(ret, headerchecksum)
    push32(ret, sourceaddress)
    push32(ret, destinationaddress)

    return ret



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




def getchecksum(version, hdrlen, tosdscp, totallength, identification,
            flags, fragmentoffset, timetolive, protocoltype, 
            sourceaddress, destinationaddress):
    pkt = composepacket(version, hdrlen, tosdscp, totallength, identification,
                flags, fragmentoffset, timetolive, protocoltype, 0,
                sourceaddress, destinationaddress)
    
    if not isinstance(pkt, bytearray):
        return False, pkt
    
    x = 0
    for i in range(len(pkt) // 2):
        x += get16(pkt, i * 2)

    while x > 0xffff:
        x0 = x & 0xffff
        x1 = x >> 16
        x = x0 + x1
    
    x = ~x
    if x < 0:
        return True, x + (2**16)
    return True, x



def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive,
            protocoltype, sourceaddress, destinationaddress, payload):
    totallength = hdrlen * 4 + len(payload)
    ok, checksum = getchecksum(4, hdrlen, tosdscp, totallength, identification,
            flags, fragmentoffset, timetolive, protocoltype,
            sourceaddress, destinationaddress)

    if not ok:
        return checksum

    pkt = composepacket(4, hdrlen, tosdscp, totallength, identification,
            flags, fragmentoffset, timetolive, protocoltype, checksum,
            sourceaddress, destinationaddress)

    if not isinstance(pkt, bytearray):
        return pkt
    
    ins16(pkt, checksum, 10)
    
    padding = bytearray([0] * ((hdrlen * 4) - 20))
    pkt = pkt + padding + payload

    bcheck = basicpacketcheck(pkt)
    if bcheck is not True:
        return bcheck

    return pkt


print(revisedcompose(6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899,
bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])) ==\
bytearray(b'F`\x00\x1e\x12g\x00\x16@\x06\x11e"3DUfw\x88\x99\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15'))

print(revisedcompose(16,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))

