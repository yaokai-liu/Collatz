import math
import numpy as np
from math import gcd
import matplotlib.pyplot as plt


alpha, beta, gamma = 3, 2, 1

D = np.linspace(0, 10, 11)
A_0 = range(1, 100)
for delta in D:
    sigma = gamma / (alpha - beta**delta)
    for k in range(1, 100):
        A_k =  [(a+sigma) * ((beta**(delta*k)) / (alpha**k)) - sigma for a in A_0]
        plt.plot(A_0, A_k)
plt.yscale("log")
plt.ylim(1, 1e100)
plt.show()
