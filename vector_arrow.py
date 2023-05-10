import matplotlib.pyplot as plt
import numpy as np


def plot_arrow2d(vector2d, origin=[0, 0], **Options):
    return plt.arrow(
        origin[0],
        origin[1],
        vector2d[0],
        vector2d[1],
        head_width=0.05,
        head_length=0.1,
        length_includes_head=True,
        **Options
    )


p1 = np.array([1, 2])
p2 = np.array([3, 4])

plot_arrow2d(p1, color="b")
plot_arrow2d(p2, color="g")

plt.axis([0, 5, 0, 5])

plt.grid()
plt.show()
