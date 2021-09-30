
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#

def getdate(st):
    st = st.split("/")
    if len(st[0]) < 2:
        st[0] = "0" + st[0]
    if len(st[1]) < 2:
        st[1] = "0" + st[1]
    st = "/".join(st)
    date = datetime.strptime(st, '%d/%m/%Y %H:%M:%S')
    return date


def getval(i):
    

def calcMissing(readings):
    # Write your code her
    res = []
    for each in readings:
        print(each)
        splttd = each.split(" ")
        val = splttd[-1]
        spl = ' '.join(splttd[:2])
        # 1/3/2012 16:00:00
        date = getdate(spl)
        if val.contains("Missing_"):
            val = None
        else:
            val = float(val)
        res.append(date, val)

    if res[0][1] is None:
        res[0][1] = res[0][2]

    for (dt, val) in res:
        if val is None:



'''
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
'''

am = "250"

inn = '''1/3/2012 16:00:00   Missing_1
1/4/2012 16:00:00   27.47
1/5/2012 16:00:00   27.728
1/6/2012 16:00:00   28.19
1/9/2012 16:00:00   28.1
1/10/2012 16:00:00  28.15
....
....
....
12/13/2012 16:00:00 27.52
12/14/2012 16:00:00 Missing_19
12/17/2012 16:00:00 27.215
12/18/2012 16:00:00 27.63
12/19/2012 16:00:00 27.73
12/20/2012 16:00:00 Missing_20
12/21/2012 16:00:00 27.49
12/24/2012 13:00:00 27.25
12/26/2012 16:00:00 27.2
12/27/2012 16:00:00 27.09
12/28/2012 16:00:00 26.9
12/31/2012 16:00:00 26.77'''

readings_count = int(am.strip())

readings = []

for l in inn.splitlines():
    readings.append(l)

calcMissing(readings)
