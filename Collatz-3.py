import math
import numpy as np

table = np.asarray([[f"{(2 * (4 ** i) * j + 5 * sum(4 ** k for k in range(0, i)) + 1) % 3}" for j in range(100)] for i in range(50)])
print(table)