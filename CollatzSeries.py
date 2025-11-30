import random
import matplotlib.pyplot as plt


def real_terms(alpha, beta, gamma, reduces: list[int]):
    terms = [0]
    calA = 0
    frakA = 0
    for i in range(1, len(reduces)):
        frakA  = frakA * alpha + (beta**calA)
        calA += reduces[i]
        term = gamma * frakA / ((beta**calA) - (alpha**i))
        terms.append(term)

    return terms

if __name__ == '__main__':
    period = [random.randint(2, 8) for i in range(2)]
    # period = [4, 3, 2, 1]
    # for i in range(1, len(period) // 3):
    #     reduces= period[:3 * i] * 100
    #     terms = real_terms(3, 2, 1, reduces)
    #     plt.plot(range(3*i), terms[len(terms) - 3*i:])
    reduces = period * 100
    terms = real_terms(3, 2, 1, reduces)
    print(terms)
    plt.plot(range(1, len(terms)), terms[1:])
    plt.show()
