


TOTAL = 160 # 160 bits in packet header


def is_valid(var, bits):
    return (var < (2 ** bits)) and (var >= 0)

START_16 = 0b1111_1111_0000_0000
END_16   = 0b0000_0000_1111_1111


def push16(bytearr, num):
    assert is_valid(num, 16), f"Number `{num}` not valid, must be 16 bit"
    bytearr.append((num & START_16) >> 8)
    bytearr.append(num & END_16)


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
    if not is_valid(hdrlen, 4):
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



