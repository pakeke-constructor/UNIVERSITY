
# Largest common substring
String match problem with DP:


Lets say we match strings "tim" and "them".
We can compute using brute force recursion:
```py
def lcs(s1, s2):
    if s1=='' or s2=='':
        return ''

    if s1[-1] == s2[-1]: ## There was a match
        return lcs(s1[:-1], s2[:-1]) + s1[-1]

    return max(
        lcs(s1[1:], s2),
        lcs(s1, s2[1:]),
    key=len) 

```

Note however, that we can arrange the strings into 2 big arrays
to compute the LCS.
Each bucket in the array represents the largest length of the string

Note that the first row and coloumn are zero because there
is no string matched


    ||   t i m
=======================
    || 0 0 0 0
 t  || 0 X X X
 h  || 0 X X X
 e  || 0 X X X
 m  || 0 X X X
======================

We can fill each row/col up with the best matched substring for
that string pair.
i.e. `i = j = 2`, for example, is the best match for the substring 'ti', 'th'.


Here is the recurrance relation:
```py
for str   a[i], b[j]:

L(i, j) = {
    0   :   i = 0 or j = 0
    L(i-1, j-1) + 1          :   a[i] == b[j]
    max(L(i,j-1), L(i-1,j))  :   a[i] != b[j]
}

Explanation:
```
If a[i] == b[i] then the chars match, so we take the biggest string before that.
else we take the max out of the two branches before.
```

