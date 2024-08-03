#!/usr/bin/python3.6
# -*coding:utf-8 -*

# importing libraries
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

# defining surface and axes
def fct(xx, yy):
	return 2 - xx**2 - yy**2

plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection ='3d')

# Plot 1
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

X, Y = np.meshgrid(x, y)
Z1 = fct(X, Y)
ax.plot_surface(X, Y, Z1, color='r', alpha=0.5, rstride=1, cstride = 1)

# Plot 2
x = np.linspace(0, 1, 100)
y = 0*np.ones(100)
z = fct(x, y)

ax.add_collection3d(pl.fill_between(x, 0, z, color='r', alpha=0.3), zs=0, zdir='y')

# Plot 3
x = np.linspace(0, 1, 100)
y = np.ones(100)
z = fct(x, y)

ax.add_collection3d(pl.fill_between(x, 0, z, color='r', alpha=0.3), zs=1, zdir='y')

# Plot 4
x = np.linspace(0, 1, 100)
y = 0*np.ones(100)
z = fct(x, y)

ax.add_collection3d(pl.fill_between(x, 0, z, color='r', alpha=0.3), zs=0, zdir='x')

# Plot 5
x = np.linspace(0, 1, 100)
y = np.ones(100)
z = fct(x, y)

ax.add_collection3d(pl.fill_between(x, 0, z, color='r', alpha=0.3), zs=1, zdir='x')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()