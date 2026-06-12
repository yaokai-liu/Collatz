import math
from fractions import Fraction

def trin(a: int):
    string = ''
    while a:
        string += str(a % 3)
        a //= 3
    return string[::-1]

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
    pre_reduce = [1, 3] # 131
    N = collatz_preitem(11, pre_reduce)
    print(N)
    # new_Ns = []
    # for k in range(len(pre_reduce)):
    #     for s in range(20):
    #         add = (3**k) * 2 * s
    #         new_pre_reduce = F_trans(pre_reduce, {k: add})
    #         new_N = collatz_preitem(1, new_pre_reduce)
    #         # print(k, add, new_N)
    #         new_N = int(new_N)
    #         new_Ns.append((new_N, bin(new_N), k, add))
    # new_Ns.sort(key=lambda p: p[0])
    # for i in new_Ns:
    #     print(i)
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
