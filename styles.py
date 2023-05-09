import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.4, 1.4, 30)

# documentation for more colors and combinations of figures: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
line1, line2, line3 = plt.plot(x, x, "g--", x, x**2, "r:", x, x**3, "b^")

# set properties for the lines being plotted.
plt.setp(line1, linewidth=3.0)

# the attributes can be called both ways. With setp or the set attribute.
# documentation for more properties: https://matplotlib.org/stable/tutorials/introductory/pyplot.html#controlling-line-properties
line1.set_linestyle("dotted")
line3.set_alpha(0.2)

plt.show()
