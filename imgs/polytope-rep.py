import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from sympy import var, plot_implicit, Eq

points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)

plt.rcParams.update({'font.size': 26})
plt.figure(figsize=(16, 9), dpi=90)

vertices = points[hull.vertices, :]
print(vertices)

plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(vertices[:, 0], vertices[:, 1], 'ro')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.savefig('v-rep.eps', bbox_inches='tight', pad_inches=0)

plt.figure(figsize=(16, 9), dpi=90)

A = hull.equations[:, :-1]
B = hull.equations[:, -1:]
print(A)
print(B)

for (a, b) in zip(A, B):
    y1 = -b/a[1]
    y2 = (-b-a[0])/a[1]
    plt.plot((0, 1), (y1, y2))

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.savefig('h-rep.eps', bbox_inches='tight', pad_inches=0)
