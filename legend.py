import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.4, 1.4, 500)
plt.plot(x, x**2, "r--", label="Square function")
plt.plot(x, x**3, "b--", label="Cube function")
plt.legend(loc="upper left")

plt.show()
