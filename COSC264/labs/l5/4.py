



import math
def number_tdma_users (s_s, g_s, u_s):
    return math.floor((s_s) / (u_s + g_s))


print (number_tdma_users(100, 1, 5))

