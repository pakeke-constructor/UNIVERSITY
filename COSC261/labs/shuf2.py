

'''




'''


def shuffl(s1, s2):
    if len(s1) == 0:
        return [s2]
    if len(s2) == 0:
        return [s1]

    ar_a = [s1[0] + e for e in shuffle(s1[1:], s2)]
    ar_b = [s2[0] + e for e in shuffle(s2[1:], s1)]

    return ar_a + ar_b



def shuffle(s1, s2):
    return set(shuffl(s1,s2))

def shuffle_language(la, lb):
    ret = set()
    for e in la:
        for j in lb:
            ret = ret.union(shuffle(e,j))
    return ret


print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
['abcd', 'abe', 'acbd', 'acdb', 'aeb', 'cabd', 'cadb', 'cdab', 'eab']
print(sorted(shuffle_language({}, {'aa', 'ab', 'bb'})))
[]



