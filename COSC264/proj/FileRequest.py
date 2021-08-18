
from bithelper import *

MAGIC_NUMBER = 0x497E

TYPE = 1 # type 1 is FileRequest


def make(filenameLen, filename):
    arr = bytearray()
    push16(arr, MAGIC_NUMBER)
    arr.append(TYPE)
    push16(arr, filenameLen)
    if filenameLen > 1024:
        print("filename length too big")
        exit(1)
    
    for char in filename:
        arr.append(char)

    return arr



def unmake(bytes_) -> tuple(int, int, str):
    arr = bytearray(bytes_)
    magic = get16(arr, 0)
    if magic != MAGIC_NUMBER:
        print("FileRequest: recieved packet not equal to magic number")
        exit(2)
    
    type_ = int(arr[2])

    filenameLen = get16(arr, 3)

    fname = ''
    for char in arr[4:]:
        fname += char

    return (type_, filenameLen, fname)



