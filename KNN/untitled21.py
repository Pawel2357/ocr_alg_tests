# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18-ocXfb55aUcCMS4HoHz5ruHi-XWQSt5
"""

import tensorflow as tf

from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images_flat = train_images.reshape(train_images.shape[0], 28*28)

test_images_flat = test_images.reshape(test_images.shape[0], 28*28)

28*28

train_images_flat

# Define the number of sample images to display
num_samples = 5

import matplotlib.pyplot as plt

for i in range(num_samples):
  plt.subplot(1, num_samples, i + 1)
  plt.imshow(train_images[i], cmap='gray')
  plt.title(f"Label: {train_labels[i]}")
  plt.axis('off')

plt.show()

from sklearn.neighbors import KNeighborsClassifier

k = 3

knn = KNeighborsClassifier(n_neighbors=k)



#train_images[0]

knn.fit(train_images_flat, train_labels)

test_pred = knn.predict(test_images_flat)

test_pred

test_labels

