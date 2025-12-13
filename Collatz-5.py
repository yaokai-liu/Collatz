import math
import numpy as np
from math import gcd
import matplotlib.pyplot as plt
import csv

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def modInverse(a, b):
    if b == 0: return 1, 0
    s, t = modInverse(b, a % b)
    return t, s - (a // b) * t



csvfile = open('table-(3,2,1).csv', mode='w', newline='')
writer = csv.writer(csvfile, delimiter=',')
writer.writerow(["delta \ k"] + [k for k in range(1, 10)])
alpha, beta, gamma = 3, 2, 1
for delta in range(1, 100):
    sigma = alpha - (beta**delta)
    inv_alpha, _ = modInverse(alpha, abs(sigma))
    pairs = []
    for k in range(1, 11):
        s = ((inv_alpha**k)*gamma)%sigma
        # print(f"alpha^-{k} * gamma = {s * gamma} [mod (alpha - beta^{delta})][mod {sigma}]")
        a_0 = (alpha**k) * s / sigma - gamma/sigma
        a_negK = (beta**(k*delta)) * s / sigma - gamma/sigma
        # print(f"a_0 = s * gamma/sigma * alpha^{k} - gamma/sigma = {a_0}")
        # print(f"a_-k = s * gamma/sigma * beta^(delta*{k}) - gamma/sigma = {a_negK}")
        a_0 = round(a_0)
        a_negK = round(a_negK)
        pairs.append((a_0, a_negK))
    writer.writerow([delta] + pairs)

csvfile.close()