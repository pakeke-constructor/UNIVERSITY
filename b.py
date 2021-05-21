

u='''
x=400 y=340
x=240 y=540
x=100 y=3
'''



def paz(st):
    ret= []
    for l in st.split("\n"):
        ret.append(tuple(l.replace("x","").replace("=","").replace("y","").split(" ")))
    return ret

def pth(st):
    tups = paz(st)
    while ('',) in tups:
        tups.remove(("",))

    eggs = []
    yeez=[]

    assert X!=0 or Y!=0
    for (X,Y) in tups:
        if abs(X)>abs(Y):
            eggs += [X/(abs(X)) for _ in range(abs(X))]
            ye = [0 for _ in range(abs(X))]
            for i in range(abs(Y)):
                ye[int(i*abs(X)/abs(Y))] = Y/abs(Y)
            yeez += ye
        else:
           yeez += [Y/abs(Y) for _ in range(abs(Y))]
           e = [0 for _ in range(abs(Y))]
           for i in range(abs(X)):
                ye[int(i*abs(Y)/abs(X))] = Y/abs(X)
           eggs += e

    return 
pth(u)