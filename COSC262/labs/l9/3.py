

def lcs(s1, s2, mem=None):
    if mem is None:
        mem = {}
    
    if s1 == '' or s2 == '':
        return ''

    if s1[-1] == s2[-1]: # last chars match
        return lcs(s1[:-1], s2[:-1], mem) + s1[-1]

    soln1=None
    if (s1[:-1], s2) in mem:
        soln1 = mem[(s1[:-1],s2)]
    else:
        soln1 = lcs(s1[:-1], s2, mem)
    
    soln2=None
    if (s1,s2[:-1]) in mem:
        soln2 = mem[(s1,s2[:-1])]
    else:
        soln2 = lcs(s1, s2[:-1], mem)
    
    solution = max(soln1, soln2, key=len)
    mem[(s1,s2)] = solution
    return solution

def lcs(s1, s2, cache=None):
    if cache is None:
        cache = {}

    if s1 == "" or s2 == "":
        return ""

    if s1[-1]==s2[-1]:
        return lcs(s1[:-1],s2[:-1],cache) + s1[-1]
    
    if (s1[:-1], s2) in cache:
        soln1 = cache[(s1[:-1],s2)]
    else:
        soln1 = lcs(s1[:-1], s2, cache)
    
    if (s1,s2[:-1]) in cache:
        soln2 = cache[(s1,s2[:-1])]
    else:
        soln2 = lcs(s1, s2[:-1], cache)
    
    solution = max(soln1, soln2, key=lambda x: len(x))
    cache[(s1,s2)] = solution
    return solution
    

# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))
 
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))