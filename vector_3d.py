import matplotlib.pyplot as plt
import numpy as np

u = np.array([3, 4, 5])
v = np.array([1, 2, 3])

x_coords, y_coords, z_coords = zip(u, v)

subplot3d = plt.subplot(111, projection="3d")
subplot3d.scatter(x_coords, y_coords, z_coords)
subplot3d.set_zlim3d([0, 9])

plt.show()
