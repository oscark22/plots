import matplotlib.pyplot as plt
import numpy as np


def plot_vectors3d(ax, vectors3d, z0=0, **Options):
    for v in vectors3d:
        x, y, z = v
        ax.plot(
            [x, x],
            [y, y],
            [z0, z],
            color="gray",
            linestyle="--",
            linewidth=0.5,
            marker="o",
        )
    x_coords, y_coords, z_coords = zip(*vectors3d)
    ax.scatter(x_coords, y_coords, z_coords, **Options)


subplot3d = plt.subplot(projection="3d")

a = np.array([1, 3, 4])
b = np.array([2, 1, 5])

plot_vectors3d(subplot3d, [a, b])

plt.show()
