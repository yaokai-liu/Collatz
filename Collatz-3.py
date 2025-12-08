import math
import numpy as np
import matplotlib.pyplot as plt

def loop_term(alpha, beta, gamma, index, reduces: list):
    index %= len(reduces)
    calA = 0
    frakA = 0
    for i in range(index, index+len(reduces)):
        frakA  = frakA * alpha + (beta**calA)
        calA += reduces[i%len(reduces)]
    term = gamma * frakA / ((beta**calA) - (alpha**len(reduces)))
    return term

if __name__ == '__main__':
    x = np.linspace(1, 2, 500)
    y = np.asarray([math.log2(3) - i for i in x])
    terms = []
    for i in range(len(x)):
        term = loop_term(3, 2, 1, 1, [x[i], y[i]])
        terms.append(term)
    plt.plot(x, terms)
    plt.show()
