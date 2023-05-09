import matplotlib.pyplot as plt

plt.plot(
    [0, 100, 100, 0, 0, 100, 50, 0, 100], [0, 0, 100, 100, 0, 100, 130, 100, 0], "b--"
)
plt.axis([-10, 110, -10, 140])
plt.show()
