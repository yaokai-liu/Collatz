import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

p = [3, 3, 3]
q = [4, 4, 2]

M = np.array([
    [-p[0],  q[0],    0],
    [    0, -p[1], q[1]],
    [ q[2],     0, -p[2]]
])

B = np.array([2, 2, 2])

box_min, box_max = 0, 20

num_points = 500000
random_points = np.random.uniform(box_min, box_max, (num_points, 3))

Mr_points = random_points @ M.T
inside_mask = np.all((Mr_points > 0) & (Mr_points <= B), axis=1)

feasible_points = random_points[inside_mask]

if len(feasible_points) < 4:
    raise ValueError("points are too few.")

hull = ConvexHull(feasible_points)
vertices = feasible_points[hull.vertices]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

faces = []
for simplex in hull.simplices:
    faces.append(feasible_points[simplex])

polygon_collection = Poly3DCollection(faces, alpha=0.3, edgecolor='none', linewidths=0.5)
polygon_collection.set_facecolor('cyan')
ax.add_collection3d(polygon_collection)

r0, r1, r2 = np.meshgrid(np.arange(box_min, box_max), np.arange(box_min, box_max), np.arange(box_min, box_max))
grid_points = np.vstack([r0.ravel(), r1.ravel(), r2.ravel()]).T
inside_grid = grid_points[np.all(grid_points @ M.T <= B, axis=1)]
ax.scatter(inside_grid[:, 0], inside_grid[:, 1], inside_grid[:, 2], color='blue', s=2, alpha=0.5, label='Integer Points')

for r_0 in range(box_min, box_max + 1):
    for r_1 in range(box_min, box_max + 1):
        for r_2 in range(box_min, box_max + 1):
            r = np.array([r_0, r_1, r_2])
            if np.all(M @ r <= B)and np.all(M @ r > 0):
                if np.any(r != 0):
                    # integer_solutions.append(r)
                    print(f"r = {r.tolist()}, gamma = {M @ r}")

ax.set_xlabel('$r_0$', fontsize=12)
ax.set_ylabel('$r_1$', fontsize=12)
ax.set_zlabel('$r_2$', fontsize=12)
ax.set_title(f'Feasible Polyhedron of $Mr \\leq {B}$ (n=3)', fontsize=14)

all_xyz = feasible_points
ax.set_xlim(all_xyz[:, 0].min() - 1, all_xyz[:, 0].max() + 1)
ax.set_ylim(all_xyz[:, 1].min() - 1, all_xyz[:, 1].max() + 1)
ax.set_zlim(all_xyz[:, 2].min() - 1, all_xyz[:, 2].max() + 1)

plt.legend()
plt.show()
