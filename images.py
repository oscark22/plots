from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open("my_square_function.png"))

# show saved image.
plt.imshow(img)
plt.axis("off")

plt.show()
