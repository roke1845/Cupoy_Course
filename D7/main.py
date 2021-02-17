import numpy as np

array1 = np.array([[10, 8], [3, 5]])

array2 = np.linalg.inv(array1)
np.dot(array2, array1)

w, v = np.linalg.eig(array1)

u, s, vh = np.linalg.svd(array1)