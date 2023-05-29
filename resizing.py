import cv2
from matplotlib import pyplot as plt
import tensorflow as tf

img = cv2.imread('data/toad.jpg')
plt.imshow(img)
plt.show()

#resizing the test data
resize = tf.image.resize(img, (256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()