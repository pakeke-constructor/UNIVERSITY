


def per_from_ber (bitErrorProb, packetLen_b):
    return 1 - (1-bitErrorProb) ** packetLen_b



def prob(P, trials):
    return (P ** trials) * (1-P)

def average_trials (P):
    x = 0
    for i in range(1000_000):
        x += i * prob(P, i)
    return 1 + x


def avg_trials_from_ber (bit_error_probability, packetLength_b):
    err = per_from_ber(bit_error_probability, packetLength_b)
    return average_trials(err)


print ("{:.3f}".format(avg_trials_from_ber(0.001, 2000)))


