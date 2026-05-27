import math
from math import prod, gcd, lcm, inf
from fractions import Fraction


def val(a, b):
    exp = 0
    while a ** exp < b: exp += 1
    return exp

def prime_factors_of(a):
    if a <= 1: return []
    factors, primes = [], [2]
    if a % 2 == 0: factors.append(2)
    if a % 3 == 0: factors.append(3)
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            if a % i == 0 and i not in factors:
                factors.append(i)
    return factors


def LCM(array):
    l = 1
    for a in array:
        l = lcm(l, a)
    return l


def rad(a):
    return prod(prime_factors_of(a))


def euler_phi(a):
    factors = prime_factors_of(a)
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
    prime_factors = prime_factors_of(a)
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