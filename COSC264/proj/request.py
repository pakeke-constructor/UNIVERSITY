
'''
request.py

File for handling FileRequest packets

Author:
Oliver Garrett
(oga20)

'''


from bithelper import *


MAGIC_NUMBER = 0x497E

TYPE = 1 # type 1 is FileRequest


def make(filename):
    arr = bytearray()
    push16(arr, MAGIC_NUMBER)
    arr.append(TYPE)
    filenameLen = len(filename)
    push16(arr, filenameLen)
    if filenameLen > 1024:
        print("filename length too big")
        exit(1)
    
    for char in filename:
        arr.append(ord(char))

    return arr



def unmake(bytes_) -> tuple([int, int, str]):
    arr = bytearray(bytes_)
    magic = get16(arr, 0)
    type_ = int(arr[2])
    filenameLen = get16(arr, 3)

    status = 1
    if magic != MAGIC_NUMBER or type_ != TYPE:
        status = 0

    fname = ''
    for char in arr[5:]:
        fname += chr(char)

    return (status, filenameLen, fname)


# Testing
if __name__ == "__main__":
    print("FileRequest: Running tests:")
    for x in ["djkfkdfkdfjkalndwoiejd.png", "q", "UUUUUUUUUU......ffff.cls"]:
        assert unmake(make(x))[-1] == x, str((unmake(make(x)), x))
    print("FileRequest: Tests passed.")

