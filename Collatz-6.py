import math
import numpy as np
from math import gcd
import matplotlib.pyplot as plt
import csv

from pydantic.v1.class_validators import all_kwargs

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

    def eval_eventual(self):
        while self.TERMS[-1] > 1:
            self.eval_to(len(self.TERMS) - 1)

if __name__ == '__main__':
    alpha, beta, gamma = 3, 2, 1
    tail = 0b110110100001001011
    # tail = 0b1
    # for head in range(1 << 6):
    #     b = (head << tail.bit_length()) + tail
    #     if b % 2 == 0: continue
    #     a = Collatz(alpha, beta, gamma, b)
    #     a.eval_eventual()
    #     # print(a.REDUCES)
    #     print(b, bin(b), head, bin(head), a.REDUCES)
    # for i in range(50):
    #     print("="*50)
    #     for j in range(50):
    #         if (2*j + 1) % 3 == 0: continue
    #         a = Collatz(alpha, beta, gamma, 2*(2*j+1)*(3**i)+1)
    #         a.eval_eventual()
    #         print(a.REDUCES)

    a = Collatz(alpha, beta, gamma, 37)
    a.eval_eventual()
    print(a.REDUCES)