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

Src1ValueTable = dict()

def SourceValue_1(B, m):
    result = []
    Beta = beta**Phi_1
    for t in B:
        if t % alpha == 0: continue
        chr_t = CollatzChr(t)
        max_k = int(logn((alpha * m - gamma)/chr_t, Beta)) + 1
        A = Src1ValueTable.get(t) or []
        dA = [int(((Beta**k)*chr_t - gamma)/alpha) for k in range(len(A), max_k)]
        A += dA
        Src1ValueTable[t] = sorted(A, reverse=True)
        result += [a for a in A if a <= m]
    return set(result)

def SourceValue(b, n, m):
    B = {b}
    for i in range(n):
        new_values = SourceValue_1(B, m) - set(B)
        if not new_values: break
        else: B = new_values
    return B

def AllSourceValue(b, m):
    all_values = {b}
    B = {b}
    while True:
        new_values = SourceValue_1(B, m) - set(B)
        if not new_values: break
        else: B = new_values
        all_values |= new_values
    return all_values

import csv
def dump_den_by_den(a1, a2, _range):
    csv_filename = f"source_values_results-{a1}-{a2}.csv"
    headers = ["range", "source value count(1)", "source value count(2)", "density(1)", "density(2)", "den1/den2"]
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
    for m in _range:
        values1 = AllSourceValue(a1, m)
        values2 = AllSourceValue(a2, m)
        density1 = len(values1) / m
        density2 = len(values2) / m
        den_by_den = len(values1) / len(values2)
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([m, len(values1), len(values2), density1, density2, den_by_den])


if __name__ == '__main__':
    dump_den_by_den(1, 5, range(65536, 65536*4, 40))
    dump_den_by_den(5, 13, range(65536, 65536*4, 40))
    dump_den_by_den(5, 53, range(65536, 65536*4, 40))
    dump_den_by_den(5, 85, range(65536, 65536*4, 40))
    dump_den_by_den(5, 341, range(65536, 65536*4, 40))
    dump_den_by_den(5, 1365, range(65536, 65536*4, 40))
    dump_den_by_den(13, 53, range(65536, 65536*4, 40))
