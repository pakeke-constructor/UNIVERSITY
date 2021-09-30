
'''
response.py

File for handling FileResponse packets

Author:
Oliver Garrett
(oga20)

'''


from bithelper import *
import random

MAGIC_NUMBER = 0x497E

TYPE = 2 # type 2 is FileResponse


def make(status, data : bytes):
    # if status is 0, failed, if status is 1, success!
    arr = bytearray()
    datalen = len(data)
    push16(arr, MAGIC_NUMBER)
    arr.append(TYPE)
    arr.append(status)

    push32(arr, datalen)
    return arr + data



def unmake(bytes_) -> tuple([int, int, bytearray]):
    arr = bytearray(bytes_)
    magic = get16(arr, 0)
    
    type_ = int(arr[2])
    if type_ != TYPE or magic != MAGIC_NUMBER:
        status = 0
    else:
        status = int(arr[3])
    datalen = get32(arr, 4)

    return (status, datalen, arr[8:])




# Testing
if __name__ == "__main__":
    print("FileResponse: Running tests:")
    for x in range(100):
        status = random.randint(0,20)
        data = bytearray(''.join(chr(random.randint(0,50)) for _ in range(10))
                        ,encoding='utf-8')
        assert unmake(make(status, data)) == (status, len(data), data), \
                (unmake(make(status, data)), (status, len(data), data))

    print("FileResponse: Tests passed")

