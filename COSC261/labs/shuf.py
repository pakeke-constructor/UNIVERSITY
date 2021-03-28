
def allowed(s,t,st):
    s,t=s[::-1],t[::-1]
    s_i=0
    t_i=0
    sB,tB=1,1
    if len(s)==0 or len(t)==0: return True
    for e in st:
        if tB and e==t[t_i]:
            t_i+=1
            tB = t_i<len(t)

        if sB and e==s[s_i]:
            s_i+=1
            sB = s_i<len(s)

    return s_i==(len(s)-1) and t_i==(len(t)-1)



def p(st):
    if len(st) <= 0:
        return []
    if len(st) <= 1:
        return [st]

    new=[]
    c=st[0]
    ar=p(st[1:])
    for e in ar:
        for i in range(len(e)):
            new.append(e[i:]+c+e[:i])   
            new.append(e[:i]+c+e[i:])    

    return new


print(p('strtrtrtr'))


def shuffle(s,t):
    n=set()
    for e in p(s+t):
        if allowed(s,t,e):
            n.add(e)
    return n
