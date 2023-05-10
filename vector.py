import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([3, 4])
v2 = np.array([8, 2])

x_coords, y_coords = zip(v1, v2)

plt.scatter(x_coords, y_coords, color=["r", "b"])
plt.axis([1, 9, 1, 9])
plt.grid()

plt.show()
