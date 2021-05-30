

def Lrecurrance(cache, a, b, i, j):
    '''
    recurrance relation function for LCS
    '''
    if a[i-1] == b[j-1]:
        cache[i][j] = cache[i-1][j-1] + 1
        return cache[i][j]
    cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    return cache[i][j]


def drecurrance(cache, a, b, i, j):
    """
    recurrance function for edit testing
    """
    if i == j and j == 0:
        cache[i][j] = 0
    elif i == 0:
        cache[i][j] = j
    elif j == 0:
        cache[i][j] = i
    elif a[i-1] == b[j-1]:
        cache[i][j] = cache[i-1][j-1]
    else:
        cache[i][j] = 1 + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])



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
    ii = len(a) + 1
    jj = len(b) + 1
    cache = [[None for _ in range(jj)] for _ in range(ii)]

    for i in range(ii):
        cache[i][0] = 0
    for j in range(jj):
        cache[0][j] = 0

    for i in range(1,ii):
        for j in range(1,jj):
            Lrecurrance(cache, a, b, i, j)

    return differences(cache, a, b)


def differences(cache, a, b):
    '''
    for c in s:
        if lcs not empty and lcs[0] == c:
            lcs.popleft()
        else:
            Mark c as 'extra'
    '''
    i = len(a)
    j = len(b)
    left = ''
    right = ''

    while  i>0 and j>0:
        if a[i-1] == b[j-1]:
            left = a[i-1] + left
            right = b[j-1] + right
            i, j = i-1, j-1
        else:
            if cache[i][j-1] > cache[i-1][j]:
                right = "[[" + b[j-1] + "]]" + right
                j -= 1
            else:
                left = "[[" + a[i-1] + "]]" + left
                i -= 1
    while i > 0:
        left = "[[" + a[i-1] + "]]" + left
        i -= 1
    
    while j > 0:
        right = "[[" + b[j-1] + "]]" + right
        j -= 1

    return (left, right)

def edits(tab, a, b):
    "rets the changes that need to be made from table"
    i = len(a)
    j = len(b)
    rets = []

    while i>0 or j>0:
        if i>0 and j>0 and a[i-1]==b[j-1]:
            ret = ("C", a[i-1], b[j-1])
            j -= 1
            i -= 1
        else:
            edit = min(tab[i][j-1], tab[i-1][j], tab[i-1][j-1])

            if i > 0 and j > 0 and tab[i-1][j-1] == edit:
                aaa, bbb = lcs(a[i-1], b[j-1])
                ret = ("S", aaa, bbb)
                i -= 1
                j -= 1
            elif i > 0 and tab[i-1][j] == edit:
                ret = ("D", a[i-1], "")
                i -= 1
            else:
                ret = ("I", "", b[j-1])
                j -= 1
        rets.append(ret)
    rets.reverse()
    return rets


def line_edits(a,b):
    '''
    gets largest common substring
    '''
    a = a.splitlines()
    b = b.splitlines()
    ii = len(a) + 1
    jj = len(b) + 1
    d = [[None for _ in range(jj)] for _ in range(ii)]

    for i in range(ii):
        for j in range(jj):
            drecurrance(d, a, b, i, j)

    return edits(d, a, b)

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)






















"""


EDIT_TYPES = {
    (-1,0) : "D", # deletion
    (0,-1) : "I", # insertion
    (-1,-1): "S"  # substitution
}

TYPES_EDIT = {
    "D" : (-1,0),
    "I" : (0,-1),
    "S" : (-1,-1)
}

EDIT_PARSE = {
    'D' : lambda line1, line2 : ("D", line1, ''),
    'I' : lambda line1, line2 : ("I", '', line2),
    'S' : lambda line1, line2 : ("S", line1, line2)
}

EDIT_TYPES_KEYS = [
     (-1,0),# D   
     (-1,-1),# S
    (0,-1),# I
]

old = '''
best = min(EDIT_TYPES_KEYS, key=lambda tup: d[i+tup[0]][j+tup[1]])
        assert best in EDIT_TYPES_KEYS, "EH?"
        st.append(EDIT_PARSE[EDIT_TYPES[best]](
            a[i-1] if i > 0 else '', b[j-1] if j > 0 else ''
        ))
'''

newer = '''
        minn = float('inf')
        best, ret = None, None
        line1, line2 = a[i-1], b[j-1]
        if d[i-1][j] < minn:
            minn, best, ret = d[i-1][j], "D", ("D", line1, "")
        if d[i][j-1] < minn:
            minn, best, ret = d[i][j-1], "I", ("I", '', line2)
        if d[i-1][j-1] < minn:
            minn, best, ret = d[i-1][j-1], "S", ("S", line1, line2)
        tup = TYPES_EDIT[best]
        i += tup[0]
        j += tup[1]
'''


def edits(d, a, b):
    "gets the edits for changing of list A to B."
    st = []
    i = len(d) - 1
    j = len(d[0]) - 1

    while i > 0 or j > 0:
        if (i > 0 and j > 0) and a[i-1] == b[j-1]:
            st.append(("C", a[i-1], b[j-1]))
            i -= 1
            j -= 1
            continue
        best = min(EDIT_TYPES_KEYS, key=lambda tup: d[i+tup[0]][j+tup[1]])
        assert best in EDIT_TYPES_KEYS, "EH?"
        st.append(EDIT_PARSE[EDIT_TYPES[best]](
            a[i-1] if i > 0 else '', b[j-1] if j > 0 else ''
        ))
        i += best[0]
        j += best[1]
    return st[::-1]
"""
