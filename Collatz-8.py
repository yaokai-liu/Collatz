from fractions import Fraction
from math import prod

alpha, beta, gamma = 3, 2, 1

def fraction_power(base, exponent):
    return Fraction(base**exponent, 1) if exponent > 0 else Fraction(1, base**abs(exponent))

def collatz_preitem(init_N, pre_reduces: list):
    cal_A = 0
    frak_a = 0
    for i in range(0, len(pre_reduces)):
        frak_a += Fraction((beta**cal_A), (alpha**i))
        cal_A += pre_reduces[i]
    N = Fraction((beta**cal_A), (alpha**len(pre_reduces))) * init_N - Fraction(gamma, alpha) * frak_a
    return N

def collatz_Gamma_cal_S(modify_reduces: list, origin_reduces: list):
    cal_S_n = sum(modify_reduces)
    cal_A = 0
    cal_S = 0
    frak_a = 0
    for i in range(0, len(origin_reduces)):
        frak_a += Fraction(fraction_power(beta,cal_A), (alpha**i)) * (fraction_power(beta, cal_S_n) - fraction_power(beta, cal_S))
        cal_A += origin_reduces[i]
        cal_S += modify_reduces[i]
    Gamma = Fraction(gamma, alpha) * frak_a
    return Gamma, cal_S_n

def pre_reduce_from_num(a: int, b: int, len: int):
    pre_reduce = []
    for i in range(len):
        pre_reduce.append((a % b) + 1)
        a //= b
    return pre_reduce

def F_trans(pre_reduce, adds: dict):
    return [r + adds[i] if adds.get(i) else r for i, r in enumerate(pre_reduce)]

if __name__ == '__main__':
    # 31
    # pre_reduce = pre_reduce_from_num(12345, 3, 10)
    basic_reduce = [2] * 100
    modify_reduce = [-1, -1, -1, -1, 0, 0, -1, 0, -1, -1, 0, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 1, -1, -1, -1, 2, 0, 0, 2, 1, -1, -1, 3, 2]
    for j in range(len(modify_reduce) - 1, -1, -1):
        sliced_modify_reduce = modify_reduce[j:]
        pre_reduce = [basic_reduce[i] + sliced_modify_reduce[i] for i in range(len(sliced_modify_reduce))]
        N = collatz_preitem(1, pre_reduce)
        G, cal_S_n = collatz_Gamma_cal_S(sliced_modify_reduce, basic_reduce[:len(sliced_modify_reduce)])
        print(pre_reduce, N, G, 1*fraction_power(beta, cal_S_n))
