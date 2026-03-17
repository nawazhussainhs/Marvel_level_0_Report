import numpy as np
import matplotlib.pyplot as plt

data = np.load("encoded_array.npy")

img = data.T

left  = img[:, ::2]
right = img[:, 1::2]

merged = np.hstack((left, right))

left_half  = merged[:, :100]
right_half = merged[:, 100:]

decoded = np.vstack((left_half, right_half))

plt.imshow(decoded, cmap="gray")
plt.axis("off")
plt.show()