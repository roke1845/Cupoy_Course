import numpy as np

array1 = np.array(range(30))
b = array1.reshape(5,6,order="F")
print(b)

print(np.where(b%6==1))