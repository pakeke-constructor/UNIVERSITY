
def convert(x, base):
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
    
    while len(coeffs) > 0 and coeffs[0] == 0:
        coeffs.pop(0)

    return coeffs

