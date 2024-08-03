#!/usr/bin/python3.6
# -*coding:utf-8 -*

import numpy as np 
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5, 5, 15), np.linspace(-5,5, 15))

u = x/np.sqrt(x**2 + y**2)
v = -y/np.sqrt(x**2 + y**2)

plt.quiver(x, y, u, v)
plt.show()