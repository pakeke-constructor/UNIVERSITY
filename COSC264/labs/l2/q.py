
def prob(P, trials):
    return (P ** trials) * (1-P)

def average_trials (P):
    x = 0
    for i in range(100000):
        x += i * prob(P, i)
    return 1 + x


print ("{:.3f}".format(average_trials(0.2)))

