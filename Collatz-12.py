import math
from math import log as logn, sqrt

from NumberTheoryTools import *

alpha, beta, gamma = 3, 2, 1

def Psi(alpha, beta, gamma):
    delta = val(2, beta + 1) - 1 if alpha % 2 == 0 else 0

    def psi(p):
        return maxpow(p, gamma * (2 ** delta)) * maxpow(p, beta ** (ord(p, beta)) - 1)

    return prod(Fraction(1, psi(p)) for p in prime_factors_of(alpha))


def Phi(k):
    fac = int((alpha ** k) * Psi(alpha, beta, gamma))
    primes = prime_factors_of(Fraction(alpha ** k, gamma))
    orders = [ord(p, beta) for p in primes]
    return fac * LCM(orders)


def IntPhi(k):
    fac = int((alpha ** k) * Psi(alpha, beta, gamma))
    primes = prime_factors_of(Fraction(alpha ** k, gamma))
    orders = [ord(p, beta) for p in primes]
    return (fac * LCM(orders)).numerator

Ord = ord(alpha, beta)
Phi_1 = IntPhi(1)
print(f"ord(alpha, beta): {Ord}, Phi_1: {Phi_1}, beta**Phi_1: {beta**Phi_1}")
ChrPows = {a: min(beta ** v for v in range(1, Ord + 1) if ((beta ** v) * a - gamma) % alpha == 0) for a in range(1, alpha)} \
    if gamma % alpha != 0 else {a : 0 for a in range(1, alpha)}
ChrPows.update({0: 0} if gamma % alpha != 0 else {0 : 1})
print(f"beta part of Collatz character: {ChrPows}")
print("#"*100)

def CollatzChr(a):
    return ChrPows[a%alpha] * a

Src1ValueTable = dict()
def Source1Value(B, m):
    result = set()
    Beta = beta**Phi_1
    for t in B:
        if t % alpha == 0: continue
        chr_t = CollatzChr(t)
        max_k = int(logn((alpha * m - gamma)/chr_t, Beta)) + 1
        A = Src1ValueTable.setdefault(t, [])
        dA = [int(((Beta**k)*chr_t - gamma)/alpha) for k in range(len(A), max_k)]
        A += dA
        Src1ValueTable[t] = A
        result.update(a for a in A if a <= m)
    return result

def SourceNValue(B, n, m):
    for i in range(n):
        new_values = Source1Value(B, m) - set(B)
        if not new_values: break
        else: B = new_values
    return B

def AllSourceValue(B, m):
    all_values = B
    while True:
        new_values = Source1Value(B, m) - set(B)
        if not new_values: break
        else: B = new_values
        all_values |= new_values
    return all_values

def Source1ValueCountPred(a, m):
    if a % alpha == 0: return 0
    r = math.log(alpha * m + gamma, beta) - math.log(CollatzChr(a), beta)
    return r / Phi_1

import csv
def dump_value_by_value(a1, a2, _range):
    rows = []
    for m in _range:
        print(f"range: {m}")
        values1 = Source1Value({a1}, m)
        values2 = Source1Value({a2}, m)
        density1 = len(values1) / m
        density2 = len(values2) / m
        den_by_den = len(values1) / len(values2)
        rows.append([m, len(values1), len(values2), density1, density2, den_by_den])
    csv_filename = f"source_1_values_results-{a1}-{a2}.csv"
    headers = ["range", "source 1 value count(1)", "source 1 value count(2)", "density(1)", "density(2)", "den1/den2"]
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt
    # csv_filename = "source_values_results-13-53.csv"
    # headers = ["range", "source value count(1)", "source value count(2)", "density(1)", "density(2)", "den1/den2"]
    # df = pd.read_csv(csv_filename)
    # range_data = df["range"].values.tolist()
    # full_cover_data = df["den1/den2"].values.tolist()
    # plt.plot(range_data, full_cover_data)
    # plt.axhline(y=CollatzChr(53)/CollatzChr(13), color='r', linestyle='--', linewidth=1.5, label='Baseline')

    # Y = np.array([7, 15, 27, 27, 27, 27, 27, 27, 255, 447, 703, 703, 703, 1819, 1819, 4255, 4255, 4255, 9663, 9663, 26623, 26623, 60975, 60975])
    # X = np.array([2**(k/2) for k in range(4, 28)])
    # fig, ax = plt.subplots(figsize=(7, 4.5))
    # # ax.set_xscale('log')
    # ax.grid(True, which="both", linestyle="--", alpha=0.5)
    # slope, intercept = np.polyfit(X, Y, 1)
    # print(slope, intercept)
    # Y_pred = slope * X + intercept
    # ax.plot(X, Y)
    # ax.plot(X, Y_pred, color='red', linewidth=2)
    # plt.show()

    csv_filename = f"count_rational_results-5-13.csv"
    headers = ["layer", "source value count (1)", "source value count (2)", "rational"]
    df = pd.read_csv(csv_filename)
    range_data = df["layer"].values.tolist()
    full_cover_data = df["rational"].values.tolist()
    plt.plot(range_data, full_cover_data)
    plt.axhline(y=1, color='r', linestyle='--', linewidth=1.5, label='Baseline')
    plt.axhline(y=2, color='r', linestyle='--', linewidth=1.5, label='Baseline')

    plt.show()
