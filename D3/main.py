import numpy as np

v1 = 20000
v0 = 20

print(20*np.log10(v1/v0))

v1_30 = 10**(30/20)*v0
v1_50 = 10**(50/20)*v0
print(v1_30/v1_50)