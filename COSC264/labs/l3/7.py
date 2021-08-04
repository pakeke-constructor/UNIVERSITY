
import math
def total_number_bits (maxUserDataBitsPerPacket_b,
        overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b

    packets = math.ceil(M / S)
    return packets * O + messageLength_b



def packet_transfer_time (linkLength_km, speedOfLight_kms,
       processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b,
        overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b

    bits = total_number_bits(maxUserDataBitsPerPacket_b, 
                             overheadBitsPerPacket_b, 
                             maxUserDataBitsPerPacket_b)
    
    prox = linkLength_km / speedOfLight_kms
    send = bits / dataRate_bps
    
    return prox * 2 + send * 2 + P * 2


