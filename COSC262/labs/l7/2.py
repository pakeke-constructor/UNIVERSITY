


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

print(change_greedy(82, [1, 10, 25, 5]))
[(3, 25), (1, 5), (2, 1)]
print(change_greedy(80, [1, 10, 25]))
[(3, 25), (5, 1)]
print(change_greedy(82, [10, 25, 5]))
None
