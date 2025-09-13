import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("jardimdejacares.jpg")
print(image.shape)
rbg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(rbg, cmap=None)
plt.show()
