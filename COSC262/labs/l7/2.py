


def change_greedy(amount, coinage):
    coins = []
    for coin in sorted(coinage, reverse=True):
        num = 0
        while amount >= coin:
            num += 1
            amount -= coin
        if num:
            coins.append((num, coin))
    
    if amount > 0:
        return None
    return coins


b='''
21
21
21
21
5
7
7
7
7
5
7
7
7
7
7
7
7
7
7
7
14
14
14
14
14
14
14
14
14
14
10
10
10
10
10
10
10
10
10
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
'''


a='''
21
21
21
21
5
7
7
7
7
5
7
7
7
7
7
7
7
7
7
7
14
14
14
14
14
14
14
14
14
14
10
10
10
10
10
10
10
10
10
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
'''


k = b.split("\n")
kk=a.split("\n")
i=0
print(len(k))
print(len(kk))
for c in kk:
    if k[i] != c:
        print(c)
    i+=1 
