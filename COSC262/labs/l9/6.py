

def get_ji(D, i, j, a,b):
    if i==j and i==0:
        return 0
    if j == 0:
        return i
    if i == 0:
        return j
    if a[i-1] == b[j-1]:
        return D[i-1][j-1]
    return 1 + min(
        D[i-1][j], D[i][j-1], D[i-1][j-1]
    )




def edit_distance(a, b):
    D = [[0] * (len(b)+1) for _ in range(len(a)+1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            D[i][j] = get_ji(D, i, j,a,b)

    i=0
    for l in D:
        if i > 3:
            print(l)
        i+=1
    return D[-1][-1]

edit_distance(
    "GCAGTC",
    "ATTCCCG"
)


def get_i(seq,cache,i,j):
    if i==0 or all(all(seq[j-1] >= seq[i-1] for j in range(i)) for i in range(j)):
        return 1
    else:
        return 1+ max(cache)

def LIS(seq):
    Lj = 0
    cache = [0] * len(seq)
    
    for i in range(len(seq)):
        for j in range(i):
            cache[i] = get_i(seq, cache, i, j)
    
    return cache[-1]










