import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 200)
fig1, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=True)
fig1.set_size_inches(10, 5)
line1, line2 = ax_top.plot(x, np.sin(3 * x**2), "r-", x, np.cos(5 * x**2), "b-")
(line3,) = ax_bottom.plot(x, np.sin(3 * x), "r-")
ax_top.grid(True)

fig2, ax = plt.subplots(1, 1)
ax.plot(x, x**2)
plt.show()
