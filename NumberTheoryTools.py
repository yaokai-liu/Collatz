import math
from math import prod, gcd, lcm, inf
from fractions import Fraction
import json

with open("primes.json", mode="r") as f:
    pairs = json.load(f)
    PRIMES = list(pairs.values())
def generate_primes_below(a):
    need_sort = False
    for i in range(PRIMES[-1] + 2, int(a) + 100, 2):
        if i in PRIMES: continue
        is_prime = True
        for p in PRIMES:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            need_sort = True
            PRIMES.append(i)
    if need_sort: PRIMES.sort()
    count = int(a / math.log(a, math.e))
    while PRIMES[count] < a: count += 1
    return count + 1

def val(a, b):
    exp = 1
    while b % (a ** exp) == 0: exp += 1
    return exp - 1

def isprime(a):
    if a <= 1: return False
    if a in PRIMES : return True
    count = generate_primes_below(int(math.sqrt(a)))
    for p in PRIMES[:count]:
        if a % p == 0: return False
    return True


def prime_factors_of(a):
    if a <= 1: return []
    if isprime(a): return [a], [1]

    factors, valuations = [], []
    count = generate_primes_below(a // 2 + 2)
    for p in PRIMES[:count]:
        if a % p == 0: factors.append(p), valuations.append(val(p, a))
    return factors, valuations


def LCM(array):
    l = 1
    for a in array:
        l = lcm(l, a)
    return l


def rad(a):
    return prod(prime_factors_of(a)[0])


def euler_phi(a):
    factors = prime_factors_of(a)[0]
    rem = int(Fraction(a, rad(a)))
    return rem * prod((p - 1) for p in factors)


def ord(a, b):
    for i in range(1, euler_phi(a) + 1):
        if b ** i % a == 1:
            return i
    raise ValueError("No solution")


def maxpow(a, b):
    return a ** (val(a, b))

def rel(a, b):
    return b / maxpow(a, b)

def raf(a, b):
    prime_factors = prime_factors_of(a)[0]
    return prod(maxpow(p, b) for p in prime_factors)

def ram(a, b):
    return b / raf(a, b)

def log(a, b, c):
    order = ord(a, b)
    for i in range(1, order + 1):
        if b ** i % a == c:
            return i
    return inf

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y