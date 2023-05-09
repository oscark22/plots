import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 30)

# show multiple subplots.
plt.subplot(2, 2, 1)
plt.plot(x, x)
plt.subplot(2, 2, 2)
plt.plot(x, x**2)
plt.subplot(2, 1, 2)
plt.plot(x, x**3)

plt.show()
