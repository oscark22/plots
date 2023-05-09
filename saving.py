import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x**2)

# saving the figure with call to savefig.
plt.savefig("my_square_function.png", transparent=True)
