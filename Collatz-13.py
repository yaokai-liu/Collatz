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
def SourceValue_1(B, m):
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


if __name__ == '__main__':
    _range = [2**k for k in range(4, 28)]
    for m in _range:
        full = set(i for i in range(1, m, 2))
        values = AllSourceValue(1, m)
        s = min(full - values)
        # print(full - values)
        print(s)
