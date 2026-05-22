from math import gcd
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

def src_value_le_N(init_N, pre_reduces: list):
    beta_cal_A = 1
    frak_A = 0
    L = len(pre_reduces)
    for i in range(0, L):
        frak_A += beta_cal_A * (alpha**(L-i-1))
        beta_cal_A *= beta**(pre_reduces[i])
    A = alpha ** L
    B = gamma * frak_A
    C = init_N * beta_cal_A
    return  A, B, C

if __name__ == '__main__':
    import csv
    N = 1<<14
    init_N = 5
    index = -1
    rows = []
    need_break = False
    size = 15
    base_vector = [1] * size
    csv_filename = f"numbers_under_{N}_{size}_{init_N}.csv"
    headers = ["number", "vector"]
    while not need_break:
        # print(base_vector)
        A, B, C = src_value_le_N(init_N, base_vector)
        if A * N + B < C :
            for i in range(-1, -size - 1, -1):
                if base_vector[i] > 2:
                    base_vector[i] = 1
                    if i == -size:
                        need_break = True
                        break
                    base_vector[i-1] += 1
                    break
            index = -1
        else:
            if (C - B) % A == 0:
                rows.append([(C - B) // A, base_vector.copy()])
            base_vector[index] += 1
    rows.sort(reverse=False, key=lambda x: x[0])
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
