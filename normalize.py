import numpy as np

x = np.array([1., 2.])
x /= np.sqrt(np.sum(x**2 ,axis=-1))[..., np.newaxis]
print(x)
print(x[0]+x[1])