from random import randint

from NumberTheoryTools import *
from itertools import permutations, product

def sharp(a):
    return a // rad(a)

def partial(a):
    return sum((a // p)*n for p, n in zip(*prime_factors_of(a)))

DUAL_PARTIALS = {1: {0}}
# for p in PRIMES: DUAL_PARTIALS[p] = {1}

def dual_partial(a):
    def _dual_partial(a, b):
        if not DUAL_PARTIALS.get(a):
            DUAL_PARTIALS[a] = dual_partial(a)
        if not DUAL_PARTIALS.get(b):
            DUAL_PARTIALS[b] = dual_partial(b)
        return {a * db - b * da for da, db in product(DUAL_PARTIALS[a], DUAL_PARTIALS[b])}

    if DUAL_PARTIALS.get(a):
        return DUAL_PARTIALS[a]
    if isprime(a):
        DUAL_PARTIALS[a] = {1}
        return DUAL_PARTIALS[a]
    pairs = list(zip(*prime_factors_of(a)))
    factors = []
    for p, n in pairs: factors += [p] * n
    perms = set(permutations(factors))
    pairs = set()
    for perm in perms:
        pairs |= set((prod(perm[:n]), prod(perm[n:])) for n in range(1, len(perm)))
    result = set()
    for pair in pairs:
        result.update(_dual_partial(*pair))
    DUAL_PARTIALS[a] = result
    return result

if __name__ == '__main__':
    # a, b = randint(1, 1000), randint(1, 1000)
    a, b = 3, 125
    print(f"a = {a}, b = {b}, a + b = {a + b}")
    rad_a, rad_b, rad_c = rad(a), rad(b), rad(a + b)
    print(f"rad a = {rad_a}, rad b = {rad_b}, rad(a + b) = {rad_c}")
    print("#"*100)
    S, T = dual_partial(a), dual_partial(b)
    U, V = dual_partial(a * b), dual_partial(a + b)
    for s, t, u, v in product(S, T, U, V):
        print(f"dualP a = {s}, dualP b = {t}, dualP(a * b) = {u}, dualP(a + b) = {v}, deltaP = {v - s - t}")
        L = lcm(u, u + s * (v - s - t))
        M = Fraction(L * rad_a * rad_b * rad_c, a * b * (a + b))
        K = Fraction(L, a * b)
        print(f"L(a, b) = {L}, K(a, b) = {K}, M(a, b) = {M}")
        print(f"K(a, b) / M(a, b) = {Fraction(K, M)}")
        print(f"{Fraction(K, M) / ((a + b) / (rad_a * rad_b * rad_c))}")
        print("="*100)
