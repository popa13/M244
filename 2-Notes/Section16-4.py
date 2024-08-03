

import numpy as np 
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.arange(-5, 5, 0.5), np.arange(-5,5, 0.5))
P = -y / np.sqrt(x**2 + y**2)
Q = x / np.sqrt(x**2 + y**2)
plt.quiver(x, y, P, Q)
plt.show()