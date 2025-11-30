import math
import numpy as np

table = np.asarray([[f"{(3 ** j) // (2 ** i)}, {(3 ** j) % (2 ** i)}" if (3 ** j) >= (2 ** i) else "" for j in range(100)] for i in range(int(100 * math.log2(3)))])
# table = np.asarray([[f"{(3 ** j) / (2 ** i)}" if (3 ** j) >= (2 ** i) else "" for j in range(100)] for i in range(int(100 * math.log2(3)))])
# np.savetxt("table.csv", table, delimiter="\t")
print(table)