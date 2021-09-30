

def ip2Int (dd):
    digits=dd.split('.')
    intIp=0
    cnt=0
    for num in reversed(digits):
        intIp += int(num) * 256 **(cnt)
        cnt +=1
    return intIp


def packetSwitching (numberRouters, messageSize_b, userDataSize_b,
            overheadSize_b, processingTime_s, dataRate_bps, propagationDelay_s):
    N  =  numberRouters
    M  =  messageSize_b
    S  =  userDataSize_b
    O  =  overheadSize_b
    P  =  processingTime_s
    R  =  dataRate_bps
    T  =  propagationDelay_s
    
    pts = M/S # is an int
    PS = S + O

    ret = P + (T*(N-1)) + (PS * pts)/R
    print(ret)
    return ret


'''

Scott Kilkelly
Toby Oliver
Frank Reading
Jordan Sadeghi
Samuel Thomas
Yang Lu
Errah Cabrera
Emma Pulusea


'''


    
# print(abs(packetSwitching(3, 10000, 1000, 100, 0.001,
#  1000000, 0.02)-0.0973)<0.0001)




FULLBYTE = 0b1111_1111
MASK_32 = [24, 16, 8, 0]


def push32(bytearr, num):
    for mshift in MASK_32:
        mask = FULLBYTE << mshift
        bytearr.append((num & mask) >> mshift)



def IPToString (addr):
    arr = bytearray()
    push32(arr, addr)
    return '.'.join(map(lambda s: str(s), arr))    


def fragmentOffsets (fragmentSize_bytes, overheadSize_bytes, messageSize_bytes):
    F  =  fragmentSize_bytes
    O  =  overheadSize_bytes
    M  =  messageSize_bytes

    I = 0
    ret = []

    while (M > 0):
        ret.append(I)
        M -= (F - O)
        I += (F - O)

    return ret   




def queueingDelay (packetSize_bits, dataRate_bps, flagCurrentTransmission, numberInQueue):
    L    =  packetSize_bits
    R    =  dataRate_bps
    flag =  flagCurrentTransmission
    N    =  numberInQueue
    
    NN = (N+1) - 0.5

    if flag:
        return NN*L / R
    else:
        return 0



print(abs(packetSwitching(3, 10000, 1000, 100, 0.001, 1000000, 0.02)-0.0973)<0.0001)


