

def sorted_array(arr, key, p):
    ret = [0] * len(arr)
    for a in arr:
        ret[p[key(a)]] = a
        p[key(a)] += 1
    return ret


def counting_sort(arr, key):
    return sorted_array(arr, key, key_positions(arr, key))


def key_positions(arr, key):
    k = key(max(arr, key=key))
    rang = range(k+1)
    c = list(rang)
    for i in rang:
        c[i] = 0
    for a in arr:
        c[key(a)] += 1
    summ = 0
    for i in rang:
        c[i], summ = summ, summ + c[i]
    return c


def radix_sort(arr, d):
    for i in range(d):
        arr = counting_sort(arr, key=lambda x: int(x/(10**i))%10)
        print(arr)
    return arr



