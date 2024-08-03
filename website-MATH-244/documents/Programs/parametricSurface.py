#!/usr/bin/python3.6
# -*coding:utf-8 -*

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Example 2
param = np.linspace(-3.14, 3.14, 100)
u, v = np.meshgrid(param, param)
a, b = 2, 2
X = (a + np.sin(v))*np.cos(u)
Y = (a + np.sin(v))*np.sin(u)
Z = u + np.cos(v)


# Display the mesh
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-4, 4)
ax.set_ylim3d(-4, 4)
ax.set_zlim3d(-4, 4)
ax.plot_surface(X, Y, Z, color = 'r', alpha = 0.3, rstride = 2, cstride = 2)

# Display curve u = 0
u = 0
v = np.linspace(0, 6.3, 50)
X = 2 + np.sin(v)
Y = 0 * v 
Z = np.cos(v)
ax.plot(X, Y, Z, color='b')

# Display curve v = 0
v = 0 
u = np.linspace(-3.14, 3.14, 50)
X = 2*np.cos(u)
Y = 2*np.sin(u)
Z = u + 1
ax.plot(X, Y, Z, color='g')

plt.show()