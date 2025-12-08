import math
import random
import numpy as np
import matplotlib.pyplot as plt


def real_terms(alpha, beta, gamma, reduces: list[int]):
    terms = [0]
    calA = 0
    frakA = 0
    for i in range(1, len(reduces)):
        frakA  = frakA * alpha + (beta**calA)
        calA += reduces[i%len(reduces)]
        term = gamma * frakA / ((beta**calA) - (alpha**i))
        terms.append(term)

    return terms

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
    x, y = np.linspace(0, 4, 1001), np.linspace(0, 4, 1001)
    # period = [4, 3, 2, 1]
    # for i in range(1, len(period) // 3):
    #     reduces= period[:3 * i] * 100
    #     terms = real_terms(3, 2, 1, reduces)
    #     plt.plot(range(3*i), terms[len(terms) - 3*i:])
    X, Y = np.meshgrid(x, y)
    terms = np.zeros(X.shape)
    for i in range(len(x)):
        for j in range(len(y)):
            reduce = [X[i, j], Y[i, j], 6 - X[i, j] - Y[i, j]]
            # if ((reduce[0] + reduce[1] + 6) - 3*math.log2(3)) < 1e-5:
            #     terms[i, j] = 0
            # else:
            #     terms[i, j] = loop_term(3, 2, 1, 1, list(reduce))
            terms[i, j] = loop_term(3, 2, 1, 1, list(reduce))

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(X, Y, terms)
    ax.set_zlim([-5, 5])
    plt.show()
    print(terms[500, 500])
    # print(terms)
