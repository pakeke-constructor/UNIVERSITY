


#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#



DEFAULT_PRICE = 1000 # $ per sq m

def is_outlier(price, st_dev, mean):
    return abs(price - mean) > (3 * st_dev)


def extrapolate(x, x1, y1, x2, y2):
    assert x1 != x2, "Extrapolation area values are equal: " + str(x1) + ", " + str(x2)

    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2
    return m * x + c



def makeStruct(areas, prices):
    '''
    returns a dictionary object that holds the prices
    of the respective houses in arrays.
    '''
    struct = {
        #  area : [price]
    }

    for i in range(len(areas)):
        arr = struct.get(areas[i], [])
        struct[areas[i]] = arr
        arr.append(prices[i])

    return struct



def removeOutliers(struct : dict):
    for area, price_array in struct.items():
        if len(price_array) > 1:
            mean = statistics.mean(price_array)
            stdev = statistics.stdev(price_array)
            newarr = []
            for price in price_array:
                if not is_outlier(price, stdev, mean):
                    newarr.append(price)
            if newarr:
                struct[area] = newarr


def singleShift(area, house_area, house_price):
    return (house_price / house_area) * area


def valuation(area, areas, prices):
    assert len(areas) == len(prices), "Len of prices differs from len of areas."

    if len(areas) == 0:
        return 1000 * area
    elif len(areas) == 1:
        return (prices.pop() / areas.pop()) * area

    struct = makeStruct(areas, prices)
    removeOutliers(struct)

    old_areas = areas
    old_prices = prices
    areas = []
    prices = []
    for i in range(len(old_areas)):
        if old_areas[i] in struct:
            areas.append(old_areas[i])
            prices.append(old_prices[i])

    if struct.get(area):
        arr = struct.get(area)
        return statistics.mean(arr)

    tight_upper = None
    tight_lower = None

    for i in range(len(areas)):
        if tight_upper is not None and (area < areas[i] < tight_upper):
            tight_upper = areas[i]
        elif areas[i] > area:
            tight_upper = areas[i]
        if tight_lower is not None and (tight_lower < areas[i] < area):
            tight_lower = areas[i]
        elif areas[i] < area:
            tight_lower = areas[i]
    
    if (tight_lower is None):
        # Then area is a min.
        areas_sorted = list(sorted(set(areas)))
        if len(areas_sorted) < 2:
            # Then there is only 1 size to deal with
            harea = areas_sorted.pop()
            return singleShift(area, harea, statistics.mean(struct[harea]))
        area1, area2 = areas_sorted[0], areas_sorted[1]
        return extrapolate(area, area1, statistics.mean(struct[area1]),
                                 area2, statistics.mean(struct[area2]))
    elif (tight_upper is None):
        # Then area is a max.
        areas_sorted = list(sorted(set(areas)))
        if len(areas_sorted) == 1:
            # Then there is only 1 size to deal with
            harea = areas_sorted.pop()
            return singleShift(area, harea, statistics.mean(struct[harea]))
        area1, area2 = areas_sorted[-1], areas_sorted[-2]
        return extrapolate(area, area1, statistics.mean(struct[area1]),
                                 area2, statistics.mean(struct[area2]))
    
    return extrapolate(
        area,
        tight_lower, statistics.mean(struct[tight_lower]),
        tight_upper, statistics.mean(struct[tight_upper])
    )


def valuationWrapper(area, areas, prices):
    return round(min(max(
        valuation(area, areas, prices), 1e3
    ), 1e6))




'''
1200
5
1500
500
1000
2000
2500
5
30000
10000
20000
40000
50000

'''


if __name__ == '__main__':
    fptr = sys.stdout # open(os.environ['OUTPUT_PATH'], 'w')

    reqArea = int(input().strip())

    area_count = int(input().strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    result = valuationWrapper(reqArea, area, price)

    fptr.write(str(round(result)) + '\n')

    fptr.close()





