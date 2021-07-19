

# final questions
# final questions
# final questions
# final questions
# final questions



def convert(x, base=2):
    if type(x) != int:
        return -1
    if type(base) != int:
        return -2
    if x < 0:
        return -3
    if base < 2:
        return -4
    
    xp = 0
    while x > (base ** xp):
        xp += 1
    
    coeffs = []
    while xp >= 0:
        coeffs.append(x // (base ** xp))
        x = (x % (base**xp))
        xp -= 1

    return ''.join(map(str,coeffs))


def revert(st):
    n=0
    for i,k in enumerate(st[::-1]):
        if k == "1":
            n += (2**i)
    return n


HEX = '0123456789ABCDEF'
assert len(HEX) == 16, "wat"


def hexstring(arg):
    coeffs = convert(arg, 16)
    ret = ''.join(map(lambda x: HEX[x], coeffs))
    return "0x" + ret



M0_4 = revert('1111' + '0' * (32-4))
M4_9 = revert('000011111' + '0' * (32-9))
M9   = revert(("0" * 9) + ("1" * (32-9)))

NON  = revert("0"*32)


def decodedate(x):
    day = (x & M4_9) >> (32-9)
    month = (x & M0_4) >> (32-4)
    yr = (x & M9)

    return '.'.join(map(str,(day + 1, month + 1, yr)))




def encodedate(day, month, yr):
    #  <month : 4>  <day : 5>  <yr : 23> 
    if not(1 <= day <= 31 and 1 <= month <= 12):
        return -1
    day -= 1
    month -= 1

    day <<= (32-9)
    month <<= (32-4)
    return day | month | yr


