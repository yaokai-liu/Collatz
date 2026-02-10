from sympy.simplify.radsimp import collect_abs

from Collatz import Collatz
import matplotlib.pyplot as plot

i = 0
a = Collatz(3,2,1, 1008611)
while a.term_at(i) != 1: i += 1

series = a.TERMS

legends = []
for i, n in enumerate(series):
    ascent_chain = list()
    ascent_index = list()
    ascent_chain.append(n)
    ascent_index.append(i)
    for j, m in enumerate(series[i + 1:]):
        if m > ascent_chain[-1]:
            ascent_chain.append(m)
            ascent_index.append(j + i + 1)
    if all(ascent_chain[j] == ascent_chain[0] for j in range(len(ascent_chain))):
        continue
    plot.plot(ascent_index, ascent_chain)
plot.plot(range(len(series)), series)
for x,y in enumerate(series):
    plot.text(x, y, bin(y), fontsize=10)
plot.margins(0.1)
plot.show()
