import math
import sys
from math import gcd
import matplotlib.pyplot as plt

sys.set_int_max_str_digits((2**16)-1)

def modInverse(a, b):
    if b == 0: return 1, 0
    s, t = modInverse(b, a % b)
    return t, s - (a // b) * t

def int2str(num: int, base: int) -> list:
    if num == 0:
        return [0]
    base_bits = []
    while num:
        base_bits.append(num % base)
        num //= base
    return list(reversed(base_bits))

class Collatz:

    def __init__(self, alpha, beta, gamma, startswith):
        assert (gcd(alpha, beta) == 1) and (gcd(alpha, gamma) == 1) and (gcd(beta, gamma) == 1)
        assert startswith % beta != 0
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.startswith = startswith
        self.TERMS = [startswith]
        self.REDUCES = [0]
        self.ACCUMULATIONS = [0]
        self.COMPLEMENTS = [0]

    def __eval_till__(self, step: int):
        for m in range(len(self.TERMS) - 1, step + 1):
            last = self.TERMS[m]
            term = last * self.alpha + self.gamma
            red = 0
            while term % self.beta == 0:
                red += 1
                term = term // self.beta
            self.TERMS.append(term)
            self.REDUCES.append(red)
            self.COMPLEMENTS.append(self.alpha * self.COMPLEMENTS[-1] + (self.beta ** self.ACCUMULATIONS[-1]))
            self.ACCUMULATIONS.append(self.ACCUMULATIONS[-1] + red)

    def term_at(self, step):
        self.__eval_till__(step)
        return self.TERMS[step]

    def reduce_at(self, step):
        self.__eval_till__(step)
        return self.REDUCES[step]

    def accumulation_at(self, step):
        self.__eval_till__(step)
        return self.ACCUMULATIONS[step]

    def complement_at(self, step):
        self.__eval_till__(step)
        return self.COMPLEMENTS[step]

    def pack_at(self, step):
        return self.term_at(step) * (self.beta ** self.accumulation_at(step))

    def reduced_complement_at(self, step):
        if step == 0: return self.startswith
        return self.complement_at(step) / (self.alpha ** (step - 1))

    def real_term_at(self, step):
        return (self.gamma * self.complement_at(step)) / ((self.beta**self.accumulation_at(step)) - (self.alpha**step))

    def eval_to(self, step):
        self.__eval_till__(step)

if __name__ == '__main__':
    alpha, beta, gamma = 2, 7, 1
    a = Collatz(alpha, beta, gamma, 4567)
    a.eval_to(1000)
    # for i in range(1000):
    #     print(a.pack_at(i) == a.startswith * (a.alpha ** i) + a.gamma * a.complement_at(i))
    for i in range(1, 1000):
        print(f"a[{i}] = {a.term_at(i)}, D[{i}] = {a.reduce_at(i)}, A[{i}] = {a.accumulation_at(i)}")
        print(f"a[{i}] = {a.real_term_at(i)}")
    plt.plot(range(1, 1000), a.REDUCES[1:1000])
    # plt.plot(range(1, 1000), [a.real_term_at(i) for i in range(1, 1000)])
    plt.plot(range(1, 1000), [a.real_term_at(i) for i in range(1, 1000)])
    plt.show()
    # s, _ = modInverse(alpha, beta)
    # s %= beta
    # for i in range(1, 9):
    #     print(f"{alpha}^-{i} == {(s**i) % beta} mod({beta})")
    # for n in range(1, 100):
    #     a = -gamma * sum(s**i for i in range(1, n+1))
    #     print(f"{n}: -{gamma} / {alpha} * sum({alpha}^-j for j in [0, {n-1}]) == {a % beta} mod({beta})")
    #     print((a * (alpha**n) + gamma * sum(alpha**i for i in range(0, n))) // beta)
