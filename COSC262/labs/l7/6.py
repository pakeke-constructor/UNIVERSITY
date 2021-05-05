


def fractional_knapsack(cap, items):
    tot = 0
    for (name, val, weight) in sorted(items, key=lambda x:x[1]/x[2], reverse=True):
        frac = val / weight
        am = min(1, cap/weight)
        cap -= am*weight
        tot += am*val
    return tot


aa=[('A',
140,
2),

('B',
150,
3),

('C',
160,
4),

('D',
180,
3)
]

print(
fractional_knapsack(7, aa))

# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))

