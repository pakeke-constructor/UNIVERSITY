

class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"


def max_value_brute(items, capacity, n=0):
    'brute force algorithm'
    if capacity < 0:
        return -99999999999999999 # dont choose this one
    if len(items) == n + 1:
        return 0
    
    return max(
        items[n].value + max_value_brute(items, capacity - items[n].weight, n+1),
        max_value_brute(items, capacity, n+1)
    )



def max_value(items, capacity):
    array = []
    for _ in range(len(items) + 1):
        array.append([(0,[]) for _ in range(capacity + 1)])
    
    for i in range(1, len(items) + 1):
        for w in range(1, capacity + 1):
            value = items[i-1].value
            weight = items[i-1].weight
            if w - weight < 0:
                soln1 = (0,[])
            else:
                tup = array[i-1][w-weight]
                soln1 = (value + tup[0], tup[1] + [items[i-1]])
            soln2 = (array[i-1][w][0], array[i-1][w][1])
            array[i][w] = max(soln1, soln2, key=lambda x: x[0])
    return array[len(items)][capacity]


# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(maximum)
print(selected_items)
# Check the returned item list with a hidden function
check_item_list(items, selected_items, maximum)






def max_value(items, capacity):
    # V[i, w] = max( Vi + V[i-1, w-Wi] , V[i-1, w] )
    arr = [([0] * (capacity + 1)) for _ in range(len(items) + 1)]
    
    for i in range(1,len(items) + 1):
        for w in range(1,capacity + 1):
            vi = items[i-1].value
            wi = items[i-1].weight
            if w - wi < 0:
                c1 = 0
            else:
                c1 = vi + arr[i-1][w-wi]
            c2 = arr[i-1][w]
            arr[i][w] = max(c1,c2)
    return arr[len(items)][capacity]




def max_value(items, capacity):
    # V[i, w] = max( Vi + V[i-1, w-Wi] , V[i-1, w] )
    arr = [([(0,[])] * (capacity + 1)) for _ in range(len(items) + 1)]
    
    for i in range(1,len(items) + 1):
        for w in range(1,capacity + 1):
            item = items[i-1]
            vi = items[i-1].value
            wi = items[i-1].weight
            if w - wi < 0:
                c1 = (0,[])
            else:
                c1 = (vi + arr[i-1][w-wi][0], arr[i-1][w-wi][1] + [item])
            c2 = arr[i-1][w]
            
            if c2[0] > c1[0]:
                arr[i][w] = c2
            else:
                arr[i][w] = c1
    return arr[len(items)][capacity]



