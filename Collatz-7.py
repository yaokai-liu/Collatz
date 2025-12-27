import math
import random
from fractions import Fraction
from random import randint

import numpy as np
from math import gcd
import matplotlib.pyplot as plt
import csv

from IPython.core.events import pre_execute, pre_run_cell

alpha, beta, gamma = 3, 2, 1

def collatz_preitem(init_N, pre_reduces: list):
    cal_A = 0
    frak_a = 0
    for i in range(0, len(pre_reduces)):
        frak_a += Fraction((beta**cal_A), (alpha**i))
        cal_A += pre_reduces[i]
    N = Fraction((beta**cal_A), (alpha**len(pre_reduces))) * init_N - Fraction(gamma, alpha) * frak_a
    return N

def pre_reduce_from_num(a: int, b: int, len: int):
    pre_reduce = []
    for i in range(len):
        pre_reduce.append((a % b) + 1)
        a //= b
    return pre_reduce

def F_trans(pre_reduce, adds: dict):
    return [r + adds[i] if adds.get(i) else r for i, r in enumerate(pre_reduce)]

if __name__ == '__main__':
    # pre_reduce = pre_reduce_from_num(12345, 3, 10)
    pre_reduce = [1, 3, 1, 2, 3, 4]
    N = collatz_preitem(1, pre_reduce)
    print(N)
    I = ar=random.sample(range(len(pre_reduce)),2)
    l, k = max(I), min(I)
    k = max(k, l - k)
    for t in range(1, 10):
        m = 2 * (3 ** l) * t
        for s in range(1, 10):
            n = 2 * (3 ** k) * s
            adds = {l: m, k: n}
            new_pre_reduce = F_trans(pre_reduce, adds)
            N_new = collatz_preitem(1, new_pre_reduce)
            b = N + s * (2**sum(pre_reduce[:k])) + t * (2**sum(pre_reduce[:l]))
            print(adds, N_new, N_new%3 == b%3)
    # deltas = range(1, 10)
    # for i in range(len(pre_reduce)):
    #     values = []
    #     for delta in deltas:
    #         b = pre_reduce[i]
    #         pre_reduce[i] = delta
    #         N = collatz_preitem(1, pre_reduce)
    #         values.append(float(abs(N - 123)))
    #         pre_reduce[i] = b
    #     print(f"pre[{i}] = {pre_reduce[i]}", values)
    #     plt.plot(deltas, values, label=f'{i}')
    # plt.yscale("log")
    # plt.legend()
    # plt.show()
