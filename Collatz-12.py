import pandas as pd

import matplotlib.pyplot as plt
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
ValChrs = {a: min(beta**v for v in range(1, Ord + 1) if ((beta ** v) * a - gamma) % alpha == 0) for a in range(1, alpha)} \
    if gamma % alpha != 0 else {a : 0 for a in range(1, alpha)}
ValChrs.update({0: 0} if gamma % alpha != 0 else {0 : 1})
print(f"valuation of remainders modulo alpha: {ValChrs}")
print("#"*100)

def CollatzChr(a):
    return ValChrs[a%alpha] * a

SrcValueTable = dict()

def SourceValue_1(B, m):
    result = []
    Beta = beta**Phi_1
    for t in B:
        if t % alpha == 0: continue
        chr_t = CollatzChr(t)
        max_k = int(logn((alpha * m - gamma)/chr_t, Beta)) + 1
        A = SrcValueTable.get(t) or []
        dA = [int(((Beta**k)*chr_t - gamma)/alpha) for k in range(len(A), max_k)]
        dA = [a for a in dA if a <= m]
        A += dA
        SrcValueTable[t] = A
        result += A
    return result

def SourceValue(b, n, m):
    B = [b]
    for i in range(n):
        new_values = SourceValue_1(B, m)
        if not (set(new_values) - set(B)): break
        else: B = new_values
    return B

def AllSourceValue(b, m):
    all_values = [b]
    B = [b]
    while True:
        new_values = SourceValue_1(B, m)
        if not (set(new_values) - set(B)): break
        else: B = new_values
        all_values += new_values
    return all_values


if __name__ == '__main__':
    csv_filename = "source_values_results-1-5.csv"
    headers = ["range", "source value count(1)", "source value count(2)", "density(1)", "density(2)", "den1/den2"]
    df = pd.read_csv(csv_filename)
    range_data = df["range"].values.tolist()
    full_cover_data = df["density(1)"].values.tolist()
    plt.plot(range_data, full_cover_data)
    # plt.axhline(y=CollatzChr(5)/CollatzChr(1), color='r', linestyle='--', linewidth=1.5, label='Baseline')
    plt.show()
