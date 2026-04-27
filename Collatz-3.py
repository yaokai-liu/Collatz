import math
import random
from random import randint
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

def fraction_power(base, exponent):
    return Fraction(base**exponent, 1) if exponent > 0 else Fraction(1, base**abs(exponent))

def loop_term(alpha, beta, gamma, index, reduces: list):
    index %= len(reduces)
    calA = 0
    frakA = 0
    for i in range(index, index+len(reduces)):
        frakA  = frakA * alpha + fraction_power(beta, calA)
        calA += reduces[i%len(reduces)]
    term = Fraction(gamma * frakA, (fraction_power(beta, calA) - fraction_power(alpha, len(reduces))))
    return term

if __name__ == '__main__':
    i = 1
    x = []
    times = []
    terms = []
    while i < 2000:
        x.append(randint(1, 11))
        term = loop_term(3, 2, 1, 1, x)
        terms.append(term)
        times.append(i)
        # print(term)
        i+=1
    plt.plot(times, terms)
    plt.show()
