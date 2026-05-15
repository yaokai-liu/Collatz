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


def CollatzChr(a):
    if a % beta == 0:
        raise ValueError(a)
    if gamma % alpha == 0:
        if a % alpha == 0:
            return beta * a
        else:
            return inf
    else:
        if a % alpha == 0:
            return inf
        else:
            return min(
                (beta ** v) * a for v in range(1, ord(alpha, beta) + 1) if ((beta ** v) * a - gamma) % alpha == 0)

if __name__ == '__main__':
    Phi_1 = Phi(1)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_yscale('log')
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    A = [Fraction(1, alpha)*(beta**(x*Phi_1))*CollatzChr(1) - Fraction(gamma, alpha) for x in range(5)]
    B = [Fraction(1, alpha)*(beta**(x*Phi_1))*CollatzChr(247) - Fraction(gamma, alpha) for x in range(5)]
    for a in A + B:
        if a % alpha == 0:
            continue
        X = range(1, 101)
        Y = [Fraction(1, alpha)*(beta**(x*Phi_1))*CollatzChr(a) - Fraction(gamma, alpha) for x in X]
        ax.plot(X, Y, label=f'{a}')
    ax.legend()
    plt.show()
