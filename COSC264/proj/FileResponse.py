
from bithelper import *

MAGIC_NUMBER = 0x497E

TYPE = 2 # type 2 is FileResponse


def make(status, dataLen, data : bytearray):
    arr = bytearray()
    data_array = bytearray(data)
    push16(arr, MAGIC_NUMBER)
    arr.append(TYPE)
    arr.append(status)

    push32(arr, dataLen)

    for byte in data_array:
        arr.append(byte)

    return arr



def unmake(bytes_) -> tuple(int, int, bytearray):
    arr = bytearray(bytes_)
    magic = get16(arr, 0)
    if magic != MAGIC_NUMBER:
        print("FileResponse: recieved packet not equal to magic number")
        exit(2)
    
    type_ = int(arr[2])
    assert type_ == TYPE, "Incorrect type for FileResponse packet"

    status = int(arr[3])
    dataLen = get32(arr, 4)

    return (status, dataLen, arr[5:])

