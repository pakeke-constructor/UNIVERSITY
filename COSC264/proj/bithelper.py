
"""
bithelper.py

This module is used to aid in the process of creating, reading, and
modifying byte-like objects. (Primarily python bytearrays)

Author:
Oliver Garrett
oga20

"""

def is_valid(var, bits):
    return (var < (2 ** bits)) and (var >= 0)

START_16 = 0b1111_1111_0000_0000
END_16   = 0b0000_0000_1111_1111


def push16(bytearr, num):
    assert is_valid(num, 16), f"Number `{num}` not valid, must be 16 bit"
    bytearr.append((num & START_16) >> 8)
    bytearr.append(num & END_16)


FULLBYTE = 0b1111_1111
MASK_32 = [24, 16, 8, 0]


def push32(bytearr, num):
    assert is_valid(num, 32), "Number not valid, must be 32 bit"
    for mshift in MASK_32:
        mask = FULLBYTE << mshift
        bytearr.append((num & mask) >> mshift)


def get16(bytearr, i):
    assert i < (len(bytearr) - 1), "Byte array too short"
    return (bytearr[i] << 8) | bytearr[i+1]


def get32(bytearr, i):
    return ((get16(bytearr, i) << 16) | get16(bytearr, i + 2))


def ins16(bytearr, num, index):
    assert index < len(bytearr) - 1, "Index too big"
    assert is_valid(num, 16), f"Number `{num}` not valid, must be 16 bit"
    bytearr[index] = ((num & START_16) >> 8)
    bytearr[index + 1] = (num & END_16)


def ins32(bytearr, num, index):
    assert index < len(bytearr) - 3, "Index too big"
    assert is_valid(num, 32), f"Number `{num}` not valid, must be 32 bit"
    ins16(bytearr, num >> 16, index)
    ins16(bytearr, num & END_16, index + 2)


