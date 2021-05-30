
def Lrecurrance(L, a, b, i, j):
    '''
    recurrance relation function for LCS
    '''
    if a[i-1] == b[j-1]:
        L[i][j] = L[i-1][j-1] + 1
        return L[i][j]
    L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[i][j]


def best_string(L, a, b):
    """
    gets the best matching string from a recurrance
    table L, and two strings a, b
    """
    st = ''
    i = len(L) - 1
    j = len(L[0]) - 1

    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            st = a[i-1] + st
            i -= 1
            j -= 1
        else:
            if L[i-1][j] > L[i][j-1]:
                i -= 1
            else:
                j -= 1
    return st


def lcs(a,b):
    '''
    gets largest common substring
    '''
    # a[i]
    # b[j]
    # L[i][j]
    I = len(a) + 1
    J = len(b) + 1
    L = [[None for _ in range(J)] for _ in range(I)]

    for i in range(I):
        L[i][0] = 0
    for j in range(J):
        L[0][j] = 0

    for i in range(1,I):
        for j in range(1,J):
            Lrecurrance(L, a, b, i, j)

    return best_string(L, a, b)



