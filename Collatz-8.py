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
    # pre_reduce = pre_reduce_from_num(12345, 3, 10)
    basic_reduce = [2, 2, 2]
    for i in range(2):
        modify_reduce = [i, 1, 2]
        pre_reduce = [basic_reduce[i] + modify_reduce[i] for i in range(len(basic_reduce))]
        N = collatz_preitem(1, pre_reduce)
        if N.is_integer():
            print(f"{i}:")
            print(f"It's an integer: {N}")
    for i in range(2):
        modify_reduce = [i, 2, 0]
        pre_reduce = [basic_reduce[i] + modify_reduce[i] for i in range(len(basic_reduce))]
        N = collatz_preitem(1, pre_reduce)
        if N.is_integer():
            print(f"{i}:")
            print(f"It's an integer: {N}")

    # basic_reduce = [2, 2]
    # modify_reduce = [1, 2]
    # pre_reduce = [basic_reduce[i] + modify_reduce[i] for i in range(len(basic_reduce))]
    # N = collatz_preitem(1, pre_reduce)
    # if N.is_integer():
    #     print(f"It's an integer: {N}")
