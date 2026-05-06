import math
import random
from fractions import Fraction

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
    # pre_reduce = [6, 36, 162, 1926] # alpha, beta, gamma = 7, 5, 1
    # pre_reduce = [4, 8, 8, 108, 608, 8108] # alpha, beta, gamma = 5, 2, 1
    pre_reduce = [1, 2, 2]
    N = collatz_preitem(1, pre_reduce)
    print(N)
