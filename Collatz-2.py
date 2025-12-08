import math
import numpy as np

# table = np.asarray([[f"{(3 ** j) // (2 ** i)}, {(3 ** j) % (2 ** i)}" if (3 ** j) >= (2 ** i) else "" for j in range(100)] for i in range(int(100 * math.log2(3)))])
# table = np.asarray([[f"{(3 ** j) / (2 ** i)}" if (3 ** j) >= (2 ** i) else "" for j in range(100)] for i in range(int(100 * math.log2(3)))])
# np.savetxt("table.csv", table, delimiter="\t")
# print(table)


def loop_term(alpha, beta, gamma, index, reduces: list):
    index %= len(reduces)
    calA = 0
    frakA = 0
    for i in range(index, index+len(reduces)):
        frakA  = frakA * alpha + (beta**calA)
        calA += reduces[i%len(reduces)]
    term = gamma * frakA / ((beta**calA) - (alpha**len(reduces)))
    return term

if __name__ == '__main__':
    # reduces = [3/4, 3/4, 3/4, 3/4]
    reduces = [1, 2, 2]
    print(loop_term(3, 2, 1, 0, reduces))