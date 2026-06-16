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
    # a, b = 3, 4
    a, b = 2, (3**10)*109
    # a, b = 3, 125
    c, d = a + b, a * b
    print(f"a = {a}, b = {b}, a + b = {c}, a * b = {d}")
    rad_a, rad_b, rad_c = rad(a), rad(b), rad(c)
    sharps = a * b * c // (rad_a * rad_b * rad_c)
    print(f"rad a = {rad_a}, rad b = {rad_b}, rad(a + b) = {rad_c}")
    print(f"rad(abc) = {rad_a*rad_b*rad_c}, a#b#c# = {sharps}")
    print("#"*100)
    S, T, U = dual_partial(a), dual_partial(b), dual_partial(c)
    for s, t, u in product(S, T, U):
        delta = u - s - t
        v = t * a - s * b
        print(f"dualP a = {s}, dualP b = {t}, dualP(a * b) = {v}, dualP(a + b) = {u}, deltaP = {delta}")
        L = lcm(v, v + a * delta)
        M = Fraction(L, sharps)
        K = Fraction(L, d)
        print(f"L(a, b) = {L}, K(a, b) = {K}, M(a, b) = {M}")
        print(f"K(a, b) / M(a, b) = {Fraction(K, M)}")
        print("="*100)
