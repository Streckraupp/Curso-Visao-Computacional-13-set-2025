import cv2
import numpy as np
from matplotlib import pyplot as plt

imagepath = "jardimdejacares.jpg"
image = cv2.imread(imagepath)
if image is None:
	raise FileNotFoundError(f"Image {imagepath} not found or could not be loaded.")
print(image.shape)
rbg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(rbg, cmap=None)
plt.show()

