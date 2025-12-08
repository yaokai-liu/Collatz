import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10000)
plt.plot(x, [math.ceil(i*math.log2(3)) for i in x])
plt.plot(x, [math.ceil(i) for i in x])
plt.show()
